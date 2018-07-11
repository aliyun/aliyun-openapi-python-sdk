# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeLaunchTemplatesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeLaunchTemplates','ecs')

	def get_TemplateTag1Value(self):
		return self.get_query_params().get('TemplateTag.1.Value')

	def set_TemplateTag1Value(self,TemplateTag1Value):
		self.add_query_param('TemplateTag.1.Value',TemplateTag1Value)

	def get_LaunchTemplateNames(self):
		return self.get_query_params().get('LaunchTemplateNames')

	def set_LaunchTemplateNames(self,LaunchTemplateNames):
		for i in range(len(LaunchTemplateNames)):	
			if LaunchTemplateNames[i] is not None:
				self.add_query_param('LaunchTemplateName.' + str(i + 1) , LaunchTemplateNames[i]);

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TemplateTag4Key(self):
		return self.get_query_params().get('TemplateTag.4.Key')

	def set_TemplateTag4Key(self,TemplateTag4Key):
		self.add_query_param('TemplateTag.4.Key',TemplateTag4Key)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_TemplateTag3Key(self):
		return self.get_query_params().get('TemplateTag.3.Key')

	def set_TemplateTag3Key(self,TemplateTag3Key):
		self.add_query_param('TemplateTag.3.Key',TemplateTag3Key)

	def get_TemplateTag5Value(self):
		return self.get_query_params().get('TemplateTag.5.Value')

	def set_TemplateTag5Value(self,TemplateTag5Value):
		self.add_query_param('TemplateTag.5.Value',TemplateTag5Value)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TemplateTag3Value(self):
		return self.get_query_params().get('TemplateTag.3.Value')

	def set_TemplateTag3Value(self,TemplateTag3Value):
		self.add_query_param('TemplateTag.3.Value',TemplateTag3Value)

	def get_TemplateTag2Key(self):
		return self.get_query_params().get('TemplateTag.2.Key')

	def set_TemplateTag2Key(self,TemplateTag2Key):
		self.add_query_param('TemplateTag.2.Key',TemplateTag2Key)

	def get_LaunchTemplateIds(self):
		return self.get_query_params().get('LaunchTemplateIds')

	def set_LaunchTemplateIds(self,LaunchTemplateIds):
		for i in range(len(LaunchTemplateIds)):	
			if LaunchTemplateIds[i] is not None:
				self.add_query_param('LaunchTemplateId.' + str(i + 1) , LaunchTemplateIds[i]);

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

	def get_TemplateTag2Value(self):
		return self.get_query_params().get('TemplateTag.2.Value')

	def set_TemplateTag2Value(self,TemplateTag2Value):
		self.add_query_param('TemplateTag.2.Value',TemplateTag2Value)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TemplateTag4Value(self):
		return self.get_query_params().get('TemplateTag.4.Value')

	def set_TemplateTag4Value(self,TemplateTag4Value):
		self.add_query_param('TemplateTag.4.Value',TemplateTag4Value)

	def get_TemplateTag5Key(self):
		return self.get_query_params().get('TemplateTag.5.Key')

	def set_TemplateTag5Key(self,TemplateTag5Key):
		self.add_query_param('TemplateTag.5.Key',TemplateTag5Key)

	def get_TemplateTag1Key(self):
		return self.get_query_params().get('TemplateTag.1.Key')

	def set_TemplateTag1Key(self,TemplateTag1Key):
		self.add_query_param('TemplateTag.1.Key',TemplateTag1Key)