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
from aliyunsdkcloudauth_console.endpoint import endpoint_data

class UploadIdentifyRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth-console', '2019-04-03', 'UploadIdentifyRecord','cloudauth-console')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Ext(self):
		return self.get_query_params().get('Ext')

	def set_Ext(self,Ext):
		self.add_query_param('Ext',Ext)

	def get_IdentifyingImageUrl(self):
		return self.get_query_params().get('IdentifyingImageUrl')

	def set_IdentifyingImageUrl(self,IdentifyingImageUrl):
		self.add_query_param('IdentifyingImageUrl',IdentifyingImageUrl)

	def get_IdentifyingImageBase64(self):
		return self.get_body_params().get('IdentifyingImageBase64')

	def set_IdentifyingImageBase64(self,IdentifyingImageBase64):
		self.add_body_params('IdentifyingImageBase64', IdentifyingImageBase64)

	def get_DeviceSecret(self):
		return self.get_query_params().get('DeviceSecret')

	def set_DeviceSecret(self,DeviceSecret):
		self.add_query_param('DeviceSecret',DeviceSecret)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_IotId(self):
		return self.get_query_params().get('IotId')

	def set_IotId(self,IotId):
		self.add_query_param('IotId',IotId)

	def get_DeviceName(self):
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_query_param('DeviceName',DeviceName)

	def get_IdentifyingTime(self):
		return self.get_query_params().get('IdentifyingTime')

	def set_IdentifyingTime(self,IdentifyingTime):
		self.add_query_param('IdentifyingTime',IdentifyingTime)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)