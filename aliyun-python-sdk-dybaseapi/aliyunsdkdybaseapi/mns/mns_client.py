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

import time
import hashlib
import hmac
import sys
import base64
import string
import platform
from aliyunsdkdybaseapi.mns.pkg_info import version
from aliyunsdkdybaseapi.mns.mns_xml_handler import *
from aliyunsdkdybaseapi.mns.mns_exception import *
from aliyunsdkdybaseapi.mns.mns_request import *
from aliyunsdkdybaseapi.mns.mns_tool import *
from aliyunsdkdybaseapi.mns.mns_http import *

URISEC_QUEUE = "queues"
URISEC_MESSAGE = "messages"

URISEC_TOPIC = "topics"
URISEC_SUBSCRIPTION = "subscriptions"


class MNSClient:
    def __init__(self, host, access_id, access_key, version = "2015-06-06", security_token = "", logger=None):
        self.host, self.is_https = self.process_host(host)
        self.access_id = access_id
        self.access_key = access_key
        self.version = version
        self.security_token = security_token
        self.logger = logger
        self.http = MNSHttp(self.host, logger=logger, is_https=self.is_https)
        if self.logger:
            self.logger.info("InitClient Host:%s Version:%s" % (host, version))

    def set_log_level(self, log_level):
        if self.logger:
            MNSLogger.validate_loglevel(log_level)
            self.logger.setLevel(log_level)
            self.http.set_log_level(log_level)

    def close_log(self):
        self.logger = None
        self.http.close_log()

    def set_connection_timeout(self, connection_timeout):
        self.http.set_connection_timeout(connection_timeout)

    def set_keep_alive(self, keep_alive):
        self.http.set_keep_alive(keep_alive)

    def close_connection(self):
        self.http.conn.close()

#===============================================queue operation===============================================#
    def batch_receive_message(self, req, resp):
        #check parameter
        BatchReceiveMessageValidator.validate(req)

        #make request internal
        req_url =  "/%s/%s/%s?numOfMessages=%s" % (URISEC_QUEUE, req.queue_name, URISEC_MESSAGE, req.batch_size)
        if req.wait_seconds != -1:
            req_url += "&waitseconds=%s" % req.wait_seconds

        req_inter = RequestInternal(req.method, req_url)
        self.build_header(req, req_inter)

        #send request
        resp_inter = self.http.send_request(req_inter)

        #handle result, make response
        resp.status = resp_inter.status
        resp.header = resp_inter.header
        self.check_status(req_inter, resp_inter, resp)
        if resp.error_data == "":
            resp.message_list = BatchRecvMessageDecoder.decode(resp_inter.data, req.base64decode, req_inter.get_req_id())
            if self.logger:
                self.logger.info("BatchReceiveMessage RequestId:%s QueueName:%s WaitSeconds:%s BatchSize:%s MessageCount:%s \
                    MessagesInfo\n%s" % (resp.get_requestid(), req.queue_name, req.wait_seconds, req.batch_size, len(resp.message_list),\
                    "\n".join(["MessageId:%s MessageBodyMD5:%s NextVisibilityTime:%s ReceiptHandle:%s EnqueueTime:%s DequeueCount:%s" % \
                                (msg.message_id, msg.message_body_md5, msg.next_visible_time, msg.receipt_handle, msg.enqueue_time, msg.dequeue_count) for msg in resp.message_list])))

    def batch_delete_message(self, req, resp):
        #check parameter
        BatchDeleteMessageValidator.validate(req)

        #make request internal
        req_inter = RequestInternal(req.method, "/%s/%s/%s" % (URISEC_QUEUE, req.queue_name, URISEC_MESSAGE))
        req_inter.data = ReceiptHandlesEncoder.encode(req.receipt_handle_list)
        self.build_header(req, req_inter)

        #send request
        resp_inter = self.http.send_request(req_inter)

        #handle result, make response
        resp.status = resp_inter.status
        resp.header = resp_inter.header
        self.check_status(req_inter, resp_inter, resp, BatchDeleteMessageDecoder)
        if self.logger:
            self.logger.info("BatchDeleteMessage RequestId:%s QueueName:%s ReceiptHandles\n%s" % \
                (resp.get_requestid(), req.queue_name, "\n".join(req.receipt_handle_list)))

###################################################################################################
#----------------------internal-------------------------------------------------------------------#
    def build_header(self, req, req_inter):
        if req.request_id is not None:
            req_inter.header["x-mns-user-request-id"] = req.request_id
        if self.http.is_keep_alive():
            req_inter.header["Connection"] = "Keep-Alive"
        if req_inter.data != "":
            content_md5 = hashlib.md5(req_inter.data).hexdigest()
            try:
                # python2 base64encode
                b64content_md5 = base64.b64encode(content_md5)
            except TypeError:
                # python3 base64encode
                b64content_md5 = base64.b64encode(content_md5.encode('utf-8')).decode('utf-8')
            req_inter.header["content-md5"] = b64content_md5
            req_inter.header["content-type"] = "text/xml;charset=UTF-8"
        req_inter.header["x-mns-version"] = self.version
        req_inter.header["host"] = self.host
        req_inter.header["date"] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        req_inter.header["user-agent"] = "aliyun-sdk-python/%s(%s/%s;%s)" % \
                                         (version, platform.system(), platform.release(), platform.python_version())
        req_inter.header["Authorization"] = self.get_signature(req_inter.method, req_inter.header, req_inter.uri)
        if self.security_token != "":
            req_inter.header["security-token"] = self.security_token

    def get_sign_string(self, source, secret):
        if sys.version_info[0] < 3:
            if isinstance(source, unicode):
                source = source.encode("utf-8")
            if isinstance(secret, unicode):
                secret = secret.encode("utf-8")
            h = hmac.new(secret, source, hashlib.sha1)
            signature = base64.b64encode(h.digest())
        else:
            if isinstance(source, str):
                source = bytes(source, "utf-8")
            if isinstance(secret, str):
                secret = bytes(secret, "utf-8")
            h = hmac.new(secret, source, hashlib.sha1)
            signature = str(base64.encodebytes(h.digest()).strip(), "utf-8")
        return signature

    def get_signature(self, method, headers, resource):
        content_md5 = self.get_element('content-md5', headers)
        content_type = self.get_element('content-type', headers)
        date = self.get_element('date', headers)
        canonicalized_resource = resource
        canonicalized_mns_headers = ""
        if len(headers) > 0:
            x_header_list = list(headers.keys())
            x_header_list.sort()
            for k in x_header_list:
                if k.startswith('x-mns-'):
                    canonicalized_mns_headers += k + ":" + headers[k] + "\n"
        string_to_sign = "%s\n%s\n%s\n%s\n%s%s" % (method, content_md5, content_type, date, canonicalized_mns_headers, canonicalized_resource)
        signature = self.get_sign_string(string_to_sign, self.access_key)
        signature = "MNS " + self.access_id + ":" + signature
        return signature

    def get_element(self, name, container):
        if name in container:
            return container[name]
        else:
            return ""

    def check_status(self, req_inter, resp_inter, resp, decoder=ErrorDecoder):
        if resp_inter.status >= 200 and resp_inter.status < 400:
            resp.error_data = ""
        else:
            resp.error_data = resp_inter.data
            if resp_inter.status >= 400 and resp_inter.status <= 600:
                excType, excMessage, reqId, hostId, subErr = decoder.decodeError(resp.error_data, req_inter.get_req_id())
                if reqId is None:
                    reqId = resp.header["x-mns-request-id"]
                raise MNSServerException(excType, excMessage, reqId, hostId, subErr)
            else:
                raise MNSClientNetworkException("UnkownError", resp_inter.data, req_inter.get_req_id())

    def make_recvresp(self, data, resp):
        resp.dequeue_count = int(data["DequeueCount"])
        resp.enqueue_time = int(data["EnqueueTime"])
        resp.first_dequeue_time = int(data["FirstDequeueTime"])
        resp.message_body = data["MessageBody"]
        resp.message_id = data["MessageId"]
        resp.message_body_md5 = data["MessageBodyMD5"]
        resp.next_visible_time = int(data["NextVisibleTime"])
        resp.receipt_handle = data["ReceiptHandle"]
        resp.priority = int(data["Priority"])

    def process_host(self, host):
        if host.startswith("http://"):
            if host.endswith("/"):
                host =  host[:-1]
            host = host[len("http://"):]
            return host, False
        elif host.startswith("https://"):
            if host.endswith("/"):
                host = host[:-1]
            host = host[len("https://"):]
            return host, True
        else:
            raise MNSClientParameterException("InvalidHost", "Only support http prototol. Invalid host:%s" % host)
