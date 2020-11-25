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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeLaunchTemplatesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeLaunchTemplates','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LaunchTemplateNames(self):
		return self.get_query_params().get('LaunchTemplateName')

	def set_LaunchTemplateNames(self, LaunchTemplateNames):
		for depth1 in range(len(LaunchTemplateNames)):
			if LaunchTemplateNames[depth1] is not None:
				self.add_query_param('LaunchTemplateName.' + str(depth1 + 1) , LaunchTemplateNames[depth1])

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TemplateTags(self):
		return self.get_query_params().get('TemplateTag')

	def set_TemplateTags(self, TemplateTags):
		for depth1 in range(len(TemplateTags)):
			if TemplateTags[depth1].get('Key') is not None:
				self.add_query_param('TemplateTag.' + str(depth1 + 1) + '.Key', TemplateTags[depth1].get('Key'))
			if TemplateTags[depth1].get('Value') is not None:
				self.add_query_param('TemplateTag.' + str(depth1 + 1) + '.Value', TemplateTags[depth1].get('Value'))

	def get_LaunchTemplateIds(self):
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateIds(self, LaunchTemplateIds):
		for depth1 in range(len(LaunchTemplateIds)):
			if LaunchTemplateIds[depth1] is not None:
				self.add_query_param('LaunchTemplateId.' + str(depth1 + 1) , LaunchTemplateIds[depth1])

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_TemplateResourceGroupId(self):
		return self.get_query_params().get('TemplateResourceGroupId')

	def set_TemplateResourceGroupId(self,TemplateResourceGroupId):
		self.add_query_param('TemplateResourceGroupId',TemplateResourceGroupId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)