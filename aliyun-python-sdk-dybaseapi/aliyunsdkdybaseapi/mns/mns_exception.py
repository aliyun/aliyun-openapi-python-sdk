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


class MNSExceptionBase(Exception):
    """
    @type type: string
    @param type: 错误类型

    @type message: string
    @param message: 错误描述

    @type req_id: string
    @param req_id: 请求的request_id
    """
    def __init__(self, type, message, req_id = None):
        self.type = type
        self.message = message
        self.req_id = req_id

    def get_info(self):
        if self.req_id is not None:
            return "(\"%s\" \"%s\") RequestID:%s\n" % (self.type, self.message, self.req_id)
        else:
            return "(\"%s\" \"%s\")\n" % (self.type, self.message)

    def __str__(self):
        return "MNSExceptionBase  %s" % (self.get_info())


class MNSClientException(MNSExceptionBase):
    def __init__(self, type, message, req_id = None):
        MNSExceptionBase.__init__(self, type, message, req_id)

    def __str__(self):
        return "MNSClientException  %s" % (self.get_info())


class MNSServerException(MNSExceptionBase):
    """ mns处理异常

        @note: 根据type进行分类处理，常见错误类型：
             : InvalidArgument       参数不合法
             : AccessDenied          无权对该资源进行当前操作
             : QueueNotExist         队列不存在
             : MessageNotExist       队列中没有消息
             : 更多错误类型请移步阿里云消息和通知服务官网进行了解；
    """
    def __init__(self, type, message, request_id, host_id, sub_errors=None):
        MNSExceptionBase.__init__(self, type, message, request_id)
        self.request_id = request_id
        self.host_id = host_id
        self.sub_errors = sub_errors

    def __str__(self):
        return "MNSServerException  %s" % (self.get_info())


class MNSClientNetworkException(MNSClientException):
    """ 网络异常

        @note: 检查endpoint是否正确、本机网络是否正常等;
    """
    def __init__(self, type, message, req_id=None):
        MNSClientException.__init__(self, type, message, req_id)

    def get_info(self):
        return "(\"%s\", \"%s\")\n" % (self.type, self.message)

    def __str__(self):
        return "MNSClientNetworkException  %s" % (self.get_info())


class MNSClientParameterException(MNSClientException):
    """ 参数格式错误

        @note: 请根据提示修改对应参数;
    """
    def __init__(self, type, message, req_id=None):
        MNSClientException.__init__(self, type, message, req_id)

    def __str__(self):
        return "MNSClientParameterException  %s" % (self.get_info())
