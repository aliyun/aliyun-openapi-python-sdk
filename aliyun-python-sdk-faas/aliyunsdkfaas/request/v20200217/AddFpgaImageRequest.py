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
from aliyunsdkfaas.endpoint import endpoint_data

class AddFpgaImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'faas', '2020-02-17', 'AddFpgaImage','faas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CloudType(self):
		return self.get_query_params().get('CloudType')

	def set_CloudType(self,CloudType):
		self.add_query_param('CloudType',CloudType)

	def get_KeyId(self):
		return self.get_query_params().get('KeyId')

	def set_KeyId(self,KeyId):
		self.add_query_param('KeyId',KeyId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_FpgaImageTags(self):
		return self.get_query_params().get('FpgaImageTags')

	def set_FpgaImageTags(self,FpgaImageTags):
		self.add_query_param('FpgaImageTags',FpgaImageTags)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ShellUniqueId(self):
		return self.get_query_params().get('ShellUniqueId')

	def set_ShellUniqueId(self,ShellUniqueId):
		self.add_query_param('ShellUniqueId',ShellUniqueId)

	def get_Encryption(self):
		return self.get_query_params().get('Encryption')

	def set_Encryption(self,Encryption):
		self.add_query_param('Encryption',Encryption)

	def get_FpgaImageName(self):
		return self.get_query_params().get('FpgaImageName')

	def set_FpgaImageName(self,FpgaImageName):
		self.add_query_param('FpgaImageName',FpgaImageName)

	def get_FpgaImageUniqueId(self):
		return self.get_query_params().get('FpgaImageUniqueId')

	def set_FpgaImageUniqueId(self,FpgaImageUniqueId):
		self.add_query_param('FpgaImageUniqueId',FpgaImageUniqueId)

	def get_FpgaImageObjectName(self):
		return self.get_query_params().get('FpgaImageObjectName')

	def set_FpgaImageObjectName(self,FpgaImageObjectName):
		self.add_query_param('FpgaImageObjectName',FpgaImageObjectName)

	def get_FpgaImageTime(self):
		return self.get_query_params().get('FpgaImageTime')

	def set_FpgaImageTime(self,FpgaImageTime):
		self.add_query_param('FpgaImageTime',FpgaImageTime)