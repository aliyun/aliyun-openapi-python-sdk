# Copyright 2018 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
import json
import os
import threading
import logging
import time

import sys
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.vendored.six import iteritems
from aliyunsdkcore.acs_exception.exceptions import ServerException

from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest
from aliyunsdkram.request.v20150501.CreateUserRequest import CreateUserRequest
from aliyunsdkram.request.v20150501.CreateAccessKeyRequest import CreateAccessKeyRequest
from aliyunsdkram.request.v20150501.DeleteAccessKeyRequest import DeleteAccessKeyRequest
from aliyunsdkram.request.v20150501.ListAccessKeysRequest import ListAccessKeysRequest
from aliyunsdkram.request.v20150501.ListRolesRequest import ListRolesRequest
from aliyunsdkram.request.v20150501.CreateRoleRequest import CreateRoleRequest
from aliyunsdkram.request.v20150501.DeleteRoleRequest import DeleteRoleRequest
from aliyunsdkram.request.v20150501.AttachPolicyToUserRequest import AttachPolicyToUserRequest

# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
if sys.version_info[:2] == (2, 6):
    from unittest2 import TestCase
else:
    from unittest import TestCase

# the version under py3 use the different package
if sys.version_info[0] == 3:
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
else:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer


def request_helper(client, request, **params):
    for key, value in iteritems(params):
        set_name = 'set_' + key
        if hasattr(request, set_name):
            func = getattr(request, set_name)
            func(value)
        else:
            raise Exception(
                "{0} has no parameter named {1}.".format(request.__class__.__name__, key))
    response = client.do_action_with_exception(request)
    return json.loads(response.decode('utf-8'))


def _check_server_response(obj, key):
    if key not in obj:
        raise Exception("No '{0}' in server response.".format(key))


def find_in_response(response, key=None, keys=None):
    if key:
        _check_server_response(response, key)
        return response[key]
    if keys:
        obj = response
        for key in keys:
            _check_server_response(obj, key)
            obj = obj[key]
        return obj


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        # if sys.version_info[0] == 2:
        #     self.assertRegex = self.assertRegexpMatches
        self._init_env()

    def test_env_available(self):
        # To let test script know whether env is available, to continue the tests
        self._init_env()

    def _init_env(self):
        self._sdk_config = self._init_sdk_config()
        self.access_key_id = self._read_key_from_env_or_config("ACCESS_KEY_ID")
        self.access_key_secret = self._read_key_from_env_or_config("ACCESS_KEY_SECRET")
        self.region_id = self._read_key_from_env_or_config("REGION_ID")
        self.user_id = self._read_key_from_env_or_config("USER_ID")
        self.root_user_id = self._read_key_from_env_or_config("ROOT_UID")
        if 'TRAVIS_JOB_NUMBER' in os.environ:
            self.travis_concurrent = os.environ.get('TRAVIS_JOB_NUMBER').split(".")[-1]
        else:
            self.travis_concurrent = "0"
        self.default_ram_user_name = "RamUserForSDKCredentialsTest" + self.travis_concurrent
        self.default_ram_role_name = "RamROleForSDKTest" + self.travis_concurrent
        self.default_role_session_name = "RoleSession" + self.travis_concurrent
        self.ram_user_id = None
        self.ram_policy_attched = False
        self.ram_user_access_key_id = None
        self.ram_user_access_key_secret = None
        self.ram_role_arn = None

    def _init_sdk_config(self):
        sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
        if os.path.isfile(sdk_config_path):
            with open(sdk_config_path) as fp:
                return json.loads(fp.read())

    def _read_key_from_env_or_config(self, key_name):
        if key_name.upper() in os.environ:
            return os.environ.get(key_name.upper())
        if key_name.lower() in self._sdk_config:
            return self._sdk_config[key_name.lower()]

        raise Exception("Failed to find sdk config: " + key_name)

    def setUp(self):
        TestCase.setUp(self)
        self.client = self.init_client()

    def tearDown(self):
        pass

    def init_client(self, region_id=None):
        if not region_id:
            region_id = self.region_id
        client = AcsClient(self.access_key_id, self.access_key_secret, region_id, timeout=120)
        client.set_stream_logger()
        return client

    @staticmethod
    def get_dict_response(string):
        return json.loads(string.decode('utf-8'), encoding="utf-8")

    def _create_default_ram_user(self):
        if self.ram_user_id:
            return
        response = request_helper(self.client, ListUsersRequest())
        user_list = find_in_response(response, keys=['Users', 'User'])
        for user in user_list:
            if user['UserName'] == self.default_ram_user_name:
                self.ram_user_id = user["UserId"]
                return

        response = request_helper(self.client, CreateUserRequest(),
                                  UserName=self.default_ram_user_name)
        self.ram_user_id = find_in_response(response, keys=['User', 'UserId'])

    def _attach_default_policy(self):
        if self.ram_policy_attched:
            return

        try:
            request_helper(self.client, AttachPolicyToUserRequest(),
                           PolicyType='System', PolicyName='AliyunSTSAssumeRoleAccess',
                           UserName=self.default_ram_user_name)
        except ServerException as e:
            if e.get_error_code() == 'EntityAlreadyExists.User.Policy':
                pass
            else:
                raise e

        self.ram_policy_attched = True

    def _create_access_key(self):
        if self.ram_user_access_key_id and self.ram_user_access_key_secret:
            return

        response = request_helper(self.client, ListAccessKeysRequest(),
                                  UserName=self.default_ram_user_name)
        for access_key in find_in_response(response, keys=['AccessKeys', 'AccessKey']):
            access_key_id = access_key['AccessKeyId']
            request_helper(self.client, DeleteAccessKeyRequest(),
                           UserAccessKeyId=access_key_id,
                           UserName=self.default_ram_user_name)

        response = request_helper(self.client, CreateAccessKeyRequest(),
                                  UserName=self.default_ram_user_name)
        self.ram_user_access_key_id = find_in_response(response, keys=['AccessKey', 'AccessKeyId'])
        self.ram_user_access_key_secret = find_in_response(
            response,
            keys=['AccessKey', 'AccessKeySecret'])

    def _delete_access_key(self):
        request_helper(self.client, DeleteAccessKeyRequest(),
                       UserName=self.default_ram_user_name,
                       UserAccessKeyId=self.ram_user_access_key_id)

    def init_sub_client(self):
        self._create_default_ram_user()
        self._attach_default_policy()
        self._create_access_key()
        client = AcsClient(self.ram_user_access_key_id,
                           self.ram_user_access_key_secret,
                           self.region_id, timeout=120)
        return client

    def _create_default_ram_role(self):
        if self.ram_role_arn:
            return
        response = request_helper(self.client, ListRolesRequest())
        for role in find_in_response(response, keys=['Roles', 'Role']):
            role_name = role['RoleName']
            role_arn = role['Arn']
            if role_name == self.default_ram_role_name:
                self.ram_role_arn = role_arn
                return

        policy_doc = """
        {
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Effect": "Allow",
              "Principal": {
                "RAM": [
                  "acs:ram::%s:root"
                ]
              }
            }
          ],
          "Version": "1"
        }
        """ % self.root_user_id

        response = request_helper(self.client, CreateRoleRequest(),
                                  RoleName=self.default_ram_role_name,
                                  AssumeRolePolicyDocument=policy_doc)
        self.ram_role_arn = find_in_response(response, keys=['Role', 'Arn'])
        # FIXME We have wait for 5 seconds after CreateRole before
        # we can AssumeRole later
        time.sleep(5)

    def _delete_default_ram_role(self):
        request_helper(self.client, DeleteRoleRequest(), RoleName=self.default_ram_role_name)


def disabled(func):
    def _decorator(func):
        pass

    return _decorator


class MyServer:
    _headers = {}
    _url = ''

    def __enter__(self):
        class ServerHandler(SimpleHTTPRequestHandler):

            def do_GET(_self):
                _self.protocol_version = 'HTTP/1.1'
                self._headers = _self.headers
                self._url = _self.path
                _self.send_response(200)
                _self.send_header("Content-type", "application/json")
                _self.end_headers()
                _self.wfile.write(b"{}")

        self.server = HTTPServer(("", 51352), ServerHandler)

        def thread_func():
            self.server.serve_forever()

        thread = threading.Thread(target=thread_func)
        thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            self.server.shutdown()
            self.server = None

    @property
    def headers(self):
        return self._headers

    @property
    def url(self):
        return self._url
