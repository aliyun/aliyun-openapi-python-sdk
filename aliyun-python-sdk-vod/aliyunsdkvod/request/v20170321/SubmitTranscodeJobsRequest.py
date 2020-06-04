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
from aliyunsdkvod.endpoint import endpoint_data

class SubmitTranscodeJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SubmitTranscodeJobs','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_VideoId(self):
		return self.get_query_params().get('VideoId')

	def set_VideoId(self,VideoId):
		self.add_query_param('VideoId',VideoId)

	def get_OverrideParams(self):
		return self.get_query_params().get('OverrideParams')

	def set_OverrideParams(self,OverrideParams):
		self.add_query_param('OverrideParams',OverrideParams)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_PipelineId(self):
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_query_param('PipelineId',PipelineId)

	def get_TemplateGroupId(self):
		return self.get_query_params().get('TemplateGroupId')

	def set_TemplateGroupId(self,TemplateGroupId):
		self.add_query_param('TemplateGroupId',TemplateGroupId)

	def get_FileUrl(self):
		return self.get_query_params().get('FileUrl')

	def set_FileUrl(self,FileUrl):
		self.add_query_param('FileUrl',FileUrl)

	def get_EncryptConfig(self):
		return self.get_query_params().get('EncryptConfig')

	def set_EncryptConfig(self,EncryptConfig):
		self.add_query_param('EncryptConfig',EncryptConfig)