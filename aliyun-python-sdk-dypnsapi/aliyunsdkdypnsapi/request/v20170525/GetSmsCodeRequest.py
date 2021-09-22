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
from aliyunsdkdypnsapi.endpoint import endpoint_data

class GetSmsCodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dypnsapi', '2017-05-25', 'GetSmsCode')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_BizToken(self): # String
		return self.get_query_params().get('BizToken')

	def set_BizToken(self, BizToken):  # String
		self.add_query_param('BizToken', BizToken)
	def get_SceneCode(self): # String
		return self.get_query_params().get('SceneCode')

	def set_SceneCode(self, SceneCode):  # String
		self.add_query_param('SceneCode', SceneCode)
	def get_OsType(self): # String
		return self.get_query_params().get('OsType')

	def set_OsType(self, OsType):  # String
		self.add_query_param('OsType', OsType)
