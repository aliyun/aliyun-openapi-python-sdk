# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8

from aliyunsdkdybaseapi.mns.mns_client import MNSClient
from aliyunsdkdybaseapi.mns.mns_request import *
from aliyunsdkdybaseapi.mns.queue import Queue
from aliyunsdkdybaseapi.mns.mns_tool import MNSLogger

class Account:
    def __init__(self, host, access_id, access_key, security_token = "", debug=False, logger = None):
        """
            @type host: string
            @param host: 访问的url，例如：http://$accountid.mns.cn-hangzhou.aliyuncs.com

            @type access_id: string
            @param access_id: 用户的AccessId, 阿里云官网获取

            @type access_key: string
            @param access_key: 用户的AccessKey，阿里云官网获取

            @type security_token: string
            @param security_token: 如果用户使用STS Token访问，需要提供security_token

            @note: Exception
            :: MNSClientParameterException host格式错误
        """
        self.access_id = access_id
        self.access_key = access_key
        self.security_token = security_token
        self.debug = debug
        self.logger = logger
        self.mns_client = MNSClient(host, access_id, access_key, security_token=security_token, logger=self.logger)

    def set_debug(self, debug):
        self.debug = debug

    def set_log_level(self, log_level):
        """ 设置logger的日志级别
            @type log_level: int
            @param log_level: one of logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR,logging.CRITICAL
        """
        MNSLogger.validate_loglevel(log_level)
        self.logger.setLevel(log_level)
        self.mns_client.set_log_level(log_level)

    def close_log(self):
        """ 关闭日志打印
        """
        self.mns_client.close_log()

    def set_client(self, host, access_id=None, access_key=None, security_token=None):
        """ 设置访问的url

            @type host: string
            @param host: 访问的url，例如：http://$accountid-new.mns.cn-hangzhou.aliyuncs.com

            @type access_id: string
            @param access_id: 用户的AccessId，阿里云官网获取

            @type access_key: string
            @param access_key: 用户的AccessKey，阿里云官网获取

            @type security_token: string
            @param security_token: 用户使用STS Token访问，需要提供security_token；如果不再使用 STS Token，请设置为 ""

            @note: Exception
            :: MNSClientParameterException host格式错误
        """
        if access_id is None:
            access_id = self.access_id
        if access_key is None:
            access_key = self.access_key
        if security_token is None:
            security_token = self.security_token
        self.mns_client = MNSClient(host, access_id, access_key, security_token=security_token, logger=self.logger)

    def get_queue(self, queue_name):
        """ 获取Account的一个Queue对象

            @type queue_name: string
            @param queue_name: 队列名

            @rtype: Queue object
            @return: 返回该Account的一个Queue对象
        """
        return Queue(queue_name, self.mns_client, self.debug)

    def get_client(self):
        """ 获取queue client

            @rtype: MNSClient object
            @return: 返回使用的MNSClient object
        """
        return self.mns_client

    def debuginfo(self, resp):
        if self.debug:
            print("===================DEBUG INFO===================")
            print("RequestId: %s" % resp.header["x-mns-request-id"])
            print("================================================")

    def __resp2meta__(self, account_meta, resp):
        account_meta.logging_bucket = resp.logging_bucket


class AccountMeta:
    def __init__(self, logging_bucket = None):
        """ Account属性
            @note: 可设置属性
            :: logging_bucket: 保存用户操作MNS日志的bucket name
        """
        self.logging_bucket = logging_bucket

    def __str__(self):
        meta_info = {"LoggingBucket" : self.logging_bucket}
        return "\n".join(["%s: %s" % (k.ljust(30),v) for k,v in meta_info.items()])
