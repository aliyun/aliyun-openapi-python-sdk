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


from aliyunsdkdybaseapi.mns.mns_request import *


class Queue:
    def __init__(self, queue_name, mns_client, debug=False): 
        self.queue_name = queue_name
        self.mns_client = mns_client
        self.set_encoding(True)
        self.debug = debug

    def set_debug(self, debug):
        self.debug = debug

    def set_encoding(self, encoding):
        """ 设置是否对消息体进行base64编码

            @type encoding: bool
            @param encoding: 是否对消息体进行base64编码
        """
        self.encoding = encoding
   
    def batch_receive_message(self, batch_size, wait_seconds = -1, req_info=None):
        """ 批量消费消息

            @type batch_size: int
            @param batch_size: 本次请求最多获取的消息条数

            @type wait_seconds: int
            @param wait_seconds: 本次请求的长轮询时间，单位：秒

            @type req_info: RequestInfo object
            @param req_info: 透传到MNS的请求信息

            @rtype: list of Message object
            @return 多条消息的属性，包含消息的基本属性、下次可消费时间和临时句柄

            @note: Exception
            :: MNSClientParameterException  参数格式异常
            :: MNSClientNetworkException    网络异常
            :: MNSServerException           mns处理异常
        """
        req = BatchReceiveMessageRequest(self.queue_name, batch_size, self.encoding, wait_seconds)
        req.set_req_info(req_info)
        resp = BatchReceiveMessageResponse()
        self.mns_client.batch_receive_message(req, resp)
        self.debuginfo(resp)
        return self.__batchrecv_resp2msg__(resp)

    def batch_delete_message(self, receipt_handle_list, req_info=None):
        """批量删除消息
            
            @type receipt_handle_list: list
            @param receipt_handle_list: batch_receive_message返回的多条消息的临时句柄

            @type req_info: RequestInfo object
            @param req_info: 透传到MNS的请求信息

            @note: Exception
            :: MNSClientParameterException  参数格式异常
            :: MNSClientNetworkException    网络异常
            :: MNSServerException           mns处理异常
        """
        req = BatchDeleteMessageRequest(self.queue_name, receipt_handle_list)
        req.set_req_info(req_info)
        resp = BatchDeleteMessageResponse()
        self.mns_client.batch_delete_message(req, resp)
        self.debuginfo(resp)

    def debuginfo(self, resp):
        if self.debug:
            print("===================DEBUG INFO===================")
            print("RequestId: %s" % resp.header["x-mns-request-id"])
            print("================================================")
    
    def __resp2meta__(self, queue_meta, resp):
        queue_meta.visibility_timeout = resp.visibility_timeout
        queue_meta.maximum_message_size = resp.maximum_message_size
        queue_meta.message_retention_period = resp.message_retention_period
        queue_meta.delay_seconds = resp.delay_seconds
        queue_meta.polling_wait_seconds = resp.polling_wait_seconds
        queue_meta.logging_enabled = resp.logging_enabled

        queue_meta.active_messages = resp.active_messages
        queue_meta.inactive_messages = resp.inactive_messages
        queue_meta.delay_messages = resp.delay_messages
        queue_meta.create_time = resp.create_time
        queue_meta.last_modify_time = resp.last_modify_time
        queue_meta.queue_name = resp.queue_name

    def __batchrecv_resp2msg__(self, resp):
        msg_list = []
        for entry in resp.message_list:
            msg = Message()
            msg.message_id = entry.message_id
            msg.message_body_md5 = entry.message_body_md5
            msg.dequeue_count = entry.dequeue_count
            msg.enqueue_time = entry.enqueue_time
            msg.first_dequeue_time = entry.first_dequeue_time
            msg.message_body = entry.message_body
            msg.priority = entry.priority
            msg.next_visible_time = entry.next_visible_time
            msg.receipt_handle = entry.receipt_handle
            msg_list.append(msg)
        return msg_list            


class Message:
    def __init__(self, message_body = None, delay_seconds = None, priority = None):
        """ 消息属性

            @note: send_message 指定属性
            :: message_body         消息体 
            :: delay_seconds        消息延迟时间
            :: priority             消息优先级

            @note: send_message 返回属性
            :: message_id           消息编号
            :: message_body_md5     消息体的MD5值

            @note: peek_message 返回属性(基本属性)
            :: message_body         消息体
            :: message_id           消息编号
            :: message_body_md5     消息体的MD5值
            :: dequeue_count        消息被消费的次数
            :: enqueue_time         消息发送到队列的时间，单位：毫秒
            :: first_dequeue_time   消息第一次被消费的时间，单位：毫秒

            @note: receive_message 返回属性，除基本属性外
            :: receipt_handle       下次删除或修改消息的临时句柄，next_visible_time之前有效
            :: next_visible_time    消息下次可消费时间

            @note: change_message_visibility 返回属性
            :: receipt_handle
            :: next_visible_time
        """
        self.message_body = "" if message_body is None else message_body
        self.delay_seconds = -1 if delay_seconds is None else delay_seconds
        self.priority = -1 if priority is None else priority

        self.message_id = ""
        self.message_body_md5 = ""

        self.dequeue_count = -1
        self.enqueue_time = -1
        self.first_dequeue_time = -1

        self.receipt_handle = ""
        self.next_visible_time = 1

    def set_delayseconds(self, delay_seconds):
        self.delay_seconds = delay_seconds

    def set_priority(self, priority):
        self.priority = priority

