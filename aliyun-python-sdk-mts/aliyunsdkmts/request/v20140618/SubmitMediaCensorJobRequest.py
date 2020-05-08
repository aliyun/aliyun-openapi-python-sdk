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
from aliyunsdkmts.endpoint import endpoint_data

class SubmitMediaCensorJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'SubmitMediaCensorJob')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_VideoCensorConfig(self):
		return self.get_query_params().get('VideoCensorConfig')

	def set_VideoCensorConfig(self,VideoCensorConfig):
		self.add_query_param('VideoCensorConfig',VideoCensorConfig)

	def get_UserData(self):
		return self.get_query_params().get('UserData')

	def set_UserData(self,UserData):
		self.add_query_param('UserData',UserData)

	def get_CoverImages(self):
		return self.get_query_params().get('CoverImages')

	def set_CoverImages(self,CoverImages):
		self.add_query_param('CoverImages',CoverImages)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PipelineId(self):
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self,PipelineId):
		self.add_query_param('PipelineId',PipelineId)

	def get_Input(self):
		return self.get_query_params().get('Input')

	def set_Input(self,Input):
		self.add_query_param('Input',Input)

	def get_Barrages(self):
		return self.get_query_params().get('Barrages')

	def set_Barrages(self,Barrages):
		self.add_query_param('Barrages',Barrages)