# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
import json

class BusinessResultServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'BusinessResultService')
		self.set_method('GET')

	def get_ErrCode(self): # String
		return self.get_query_params().get('ErrCode')

	def set_ErrCode(self, ErrCode):  # String
		self.add_query_param('ErrCode', ErrCode)
	def get_Result(self): # Map
		return self.get_query_params().get('Result')

	def set_Result(self, Result):  # Map
		self.add_query_param("Result", json.dumps(Result))
	def get_BussinessCode(self): # String
		return self.get_query_params().get('BussinessCode')

	def set_BussinessCode(self, BussinessCode):  # String
		self.add_query_param('BussinessCode', BussinessCode)
	def get_RequestId(self): # String
		return self.get_query_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_query_param('RequestId', RequestId)
	def get_Success(self): # Boolean
		return self.get_query_params().get('Success')

	def set_Success(self, Success):  # Boolean
		self.add_query_param('Success', Success)
	def get_ErrMessage(self): # String
		return self.get_query_params().get('ErrMessage')

	def set_ErrMessage(self, ErrMessage):  # String
		self.add_query_param('ErrMessage', ErrMessage)
	def get_ActionCode(self): # String
		return self.get_query_params().get('ActionCode')

	def set_ActionCode(self, ActionCode):  # String
		self.add_query_param('ActionCode', ActionCode)
