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


class RequestBase:
    def __init__(self):
        self.method = ""
        self.request_id = None

    def set_req_info(self, req_info):
        if req_info is not None:
            if req_info.request_id is not None:
                self.request_id = req_info.request_id


class ResponseBase():
    def __init__(self):
        self.status = -1
        self.header = {}
        self.error_data = ""

    def get_requestid(self):
        return self.header.get("x-mns-request-id")


class BatchReceiveMessageRequest(RequestBase):
    def __init__(self, queue_name, batch_size, base64decode = True, wait_seconds = -1):
        RequestBase.__init__(self)
        self.queue_name = queue_name
        self.batch_size = batch_size
        self.base64decode = base64decode
        self.wait_seconds = wait_seconds
        self.method = "GET"


class ReceiveMessageResponseEntry():
    def __init__(self):
        self.dequeue_count = -1
        self.enqueue_time = -1
        self.first_dequeue_time = -1
        self.message_body = ""
        self.message_id = ""
        self.message_body_md5 = ""
        self.priority = -1
        self.next_visible_time = ""
        self.receipt_handle = ""


class BatchReceiveMessageResponse(ResponseBase):
    def __init__(self):
        ResponseBase.__init__(self)
        self.message_list = []


class BatchDeleteMessageRequest(RequestBase):
    def __init__(self, queue_name, receipt_handle_list):
        RequestBase.__init__(self)
        self.queue_name = queue_name
        self.receipt_handle_list = receipt_handle_list
        self.method = "DELETE"


class BatchDeleteMessageResponse(ResponseBase):
    def __init__(self):
        ResponseBase.__init__(self)
