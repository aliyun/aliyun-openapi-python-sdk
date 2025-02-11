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
from aliyunsdkcloudauth.endpoint import endpoint_data

class InsertWhiteListSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'InsertWhiteListSetting','cloudauth')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ValidDay(self): # Integer
		return self.get_query_params().get('ValidDay')

	def set_ValidDay(self, ValidDay):  # Integer
		self.add_query_param('ValidDay', ValidDay)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_CertifyId(self): # String
		return self.get_query_params().get('CertifyId')

	def set_CertifyId(self, CertifyId):  # String
		self.add_query_param('CertifyId', CertifyId)
	def get_CertNo(self): # String
		return self.get_query_params().get('CertNo')

	def set_CertNo(self, CertNo):  # String
		self.add_query_param('CertNo', CertNo)
	def get_ServiceCode(self): # String
		return self.get_query_params().get('ServiceCode')

	def set_ServiceCode(self, ServiceCode):  # String
		self.add_query_param('ServiceCode', ServiceCode)
	def get_SceneId(self): # Long
		return self.get_query_params().get('SceneId')

	def set_SceneId(self, SceneId):  # Long
		self.add_query_param('SceneId', SceneId)
