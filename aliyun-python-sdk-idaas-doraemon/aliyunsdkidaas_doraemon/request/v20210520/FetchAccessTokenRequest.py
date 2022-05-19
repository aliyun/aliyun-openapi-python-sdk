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
from aliyunsdkidaas_doraemon.endpoint import endpoint_data

class FetchAccessTokenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idaas-doraemon', '2021-05-20', 'FetchAccessToken')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_XClientIp(self): # String
		return self.get_query_params().get('XClientIp')

	def set_XClientIp(self, XClientIp):  # String
		self.add_query_param('XClientIp', XClientIp)
	def get_MobileExtendParamsJsonSign(self): # String
		return self.get_query_params().get('MobileExtendParamsJsonSign')

	def set_MobileExtendParamsJsonSign(self, MobileExtendParamsJsonSign):  # String
		self.add_query_param('MobileExtendParamsJsonSign', MobileExtendParamsJsonSign)
	def get_ServerExtendParamsJson(self): # String
		return self.get_query_params().get('ServerExtendParamsJson')

	def set_ServerExtendParamsJson(self, ServerExtendParamsJson):  # String
		self.add_query_param('ServerExtendParamsJson', ServerExtendParamsJson)
	def get_MobileExtendParamsJson(self): # String
		return self.get_query_params().get('MobileExtendParamsJson')

	def set_MobileExtendParamsJson(self, MobileExtendParamsJson):  # String
		self.add_query_param('MobileExtendParamsJson', MobileExtendParamsJson)
	def get_ApplicationExternalId(self): # String
		return self.get_query_params().get('ApplicationExternalId')

	def set_ApplicationExternalId(self, ApplicationExternalId):  # String
		self.add_query_param('ApplicationExternalId', ApplicationExternalId)
