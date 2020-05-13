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

class DetectFaceAttributesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2018-09-16', 'DetectFaceAttributes','cloudauth')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxNumPhotosPerCategory(self):
		return self.get_body_params().get('MaxNumPhotosPerCategory')

	def set_MaxNumPhotosPerCategory(self,MaxNumPhotosPerCategory):
		self.add_body_params('MaxNumPhotosPerCategory', MaxNumPhotosPerCategory)

	def get_MaxFaceNum(self):
		return self.get_body_params().get('MaxFaceNum')

	def set_MaxFaceNum(self,MaxFaceNum):
		self.add_body_params('MaxFaceNum', MaxFaceNum)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RetAttributes(self):
		return self.get_body_params().get('RetAttributes')

	def set_RetAttributes(self,RetAttributes):
		self.add_body_params('RetAttributes', RetAttributes)

	def get_ClientTag(self):
		return self.get_body_params().get('ClientTag')

	def set_ClientTag(self,ClientTag):
		self.add_body_params('ClientTag', ClientTag)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_MaterialValue(self):
		return self.get_body_params().get('MaterialValue')

	def set_MaterialValue(self,MaterialValue):
		self.add_body_params('MaterialValue', MaterialValue)

	def get_DontSaveDB(self):
		return self.get_body_params().get('DontSaveDB')

	def set_DontSaveDB(self,DontSaveDB):
		self.add_body_params('DontSaveDB', DontSaveDB)