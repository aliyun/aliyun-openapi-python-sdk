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


import os
import types
import logging
import logging.handlers
from aliyunsdkdybaseapi.mns.mns_exception import *

METHODS = ["PUT", "POST", "GET", "DELETE"]

class MNSLogger:
    @staticmethod
    def get_logger(log_name=None, log_file=None, log_level=logging.INFO):
        if log_name is None:
            log_name = "mns_python_sdk"
        if log_file is None:
            log_file = os.path.join(os.path.split(os.path.realpath(__file__))[0], "mns_python_sdk.log")
        logger = logging.getLogger(log_name)
        if logger.handlers == []:
            fileHandler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10*1024*1024)
            formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(thread)d] %(message)s', '%Y-%m-%d %H:%M:%S')
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)
        MNSLogger.validate_loglevel(log_level)
        logger.setLevel(log_level)
        return logger

    @staticmethod
    def validate_loglevel(log_level):
        log_levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
        if log_level not in log_levels:
            raise MNSClientParameterException("LogLevelInvalid", "Bad value: '%s', expect levels: '%s'." % \
                (log_level, ','.join([str(item) for item in log_levels])))

class ValidatorBase:
    @staticmethod
    def validate(req):
        pass

    @staticmethod
    def type_validate(item, valid_type, param_name=None, req_id=None):
        if not (type(item) is valid_type):
            if param_name is None:
                raise MNSClientParameterException("TypeInvalid", "Bad type: '%s', '%s' expect type '%s'." % (type(item), item, valid_type), req_id)
            else:
                raise MNSClientParameterException("TypeInvalid", "Param '%s' in bad type: '%s', '%s' expect type '%s'." % (param_name, type(item), item, valid_type), req_id)

    @staticmethod
    def is_str(item, param_name=None, req_id=None):
        if not isinstance(item, str):
            if param_name is None:
                raise MNSClientParameterException("TypeInvalid", "Bad type: '%s', '%s' expect basestring." % (type(item), item), req_id)
            else:
                raise MNSClientParameterException("TypeInvalid", "Param '%s' in bad type: '%s', '%s' expect basestring." % (param_name, type(item), item), req_id)

    @staticmethod
    def marker_validate(req):
        ValidatorBase.is_str(req.marker, req_id=req.request_id)

    @staticmethod
    def retnumber_validate(req):
        ValidatorBase.type_validate(req.ret_number, types.IntType, req_id=req.request_id)
        if (req.ret_number != -1 and req.ret_number <= 0 ):
            raise MNSClientParameterException("HeaderInvalid", "Bad value: '%s', x-mns-number should larger than 0." % req.ret_number, req.request_id)

    @staticmethod
    def name_validate(name, nameType, req_id=None):
        #type
        ValidatorBase.is_str(name, req_id=req_id)

        #length
        if len(name) < 1:
            raise MNSClientParameterException("QueueNameInvalid", "Bad value: '%s', the length of %s should larger than 1." % (name, nameType), req_id)

    @staticmethod
    def list_condition_validate(req):
        if req.prefix != "":
            ValidatorBase.name_validate(req.prefix, "prefix")

        ValidatorBase.marker_validate(req)
        ValidatorBase.retnumber_validate(req)

class MessageValidator(ValidatorBase):
    @staticmethod
    def receiphandle_validate(receipt_handle, req_id):
        if (receipt_handle == ""):
            raise MNSClientParameterException("ReceiptHandleInvalid", "The receipt handle should not be null.", req_id)

    @staticmethod
    def waitseconds_validate(wait_seconds, req_id):
        if wait_seconds != -1 and wait_seconds < 0:
            raise MNSClientParameterException("WaitSecondsInvalid", "Bad value: '%d', wait_seconds should larger than 0." % wait_seconds, req_id)

    @staticmethod
    def batchsize_validate(batch_size, req_id):
        if batch_size != -1 and batch_size < 0:
            raise MNSClientParameterException("BatchSizeInvalid", "Bad value: '%d', batch_size should larger than 0." % batch_size, req_id)

class BatchReceiveMessageValidator(MessageValidator):
    @staticmethod
    def validate(req):
        MessageValidator.validate(req)
        ValidatorBase.name_validate(req.queue_name, "queue_name", req.request_id)
        MessageValidator.batchsize_validate(req.batch_size, req.request_id)
        MessageValidator.waitseconds_validate(req.wait_seconds, req.request_id)

class BatchDeleteMessageValidator(MessageValidator):
    @staticmethod
    def validate(req):
        MessageValidator.validate(req)
        ValidatorBase.name_validate(req.queue_name, "queue_name", req.request_id)
        for receipt_handle in req.receipt_handle_list:
            MessageValidator.receiphandle_validate(receipt_handle, req.request_id)
