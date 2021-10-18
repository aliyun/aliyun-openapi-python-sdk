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

class DescribeLaunchTemplateVersionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeLaunchTemplateVersions','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_LaunchTemplateName(self): # String
		return self.get_query_params().get('LaunchTemplateName')

	def set_LaunchTemplateName(self, LaunchTemplateName):  # String
		self.add_query_param('LaunchTemplateName', LaunchTemplateName)
	def get_MaxVersion(self): # Long
		return self.get_query_params().get('MaxVersion')

	def set_MaxVersion(self, MaxVersion):  # Long
		self.add_query_param('MaxVersion', MaxVersion)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DefaultVersion(self): # Boolean
		return self.get_query_params().get('DefaultVersion')

	def set_DefaultVersion(self, DefaultVersion):  # Boolean
		self.add_query_param('DefaultVersion', DefaultVersion)
	def get_MinVersion(self): # Long
		return self.get_query_params().get('MinVersion')

	def set_MinVersion(self, MinVersion):  # Long
		self.add_query_param('MinVersion', MinVersion)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_LaunchTemplateId(self): # String
		return self.get_query_params().get('LaunchTemplateId')

	def set_LaunchTemplateId(self, LaunchTemplateId):  # String
		self.add_query_param('LaunchTemplateId', LaunchTemplateId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LaunchTemplateVersions(self): # RepeatList
		return self.get_query_params().get('LaunchTemplateVersion')

	def set_LaunchTemplateVersions(self, LaunchTemplateVersion):  # RepeatList
		for depth1 in range(len(LaunchTemplateVersion)):
			self.add_query_param('LaunchTemplateVersion.' + str(depth1 + 1), LaunchTemplateVersion[depth1])
	def get_DetailFlag(self): # Boolean
		return self.get_query_params().get('DetailFlag')

	def set_DetailFlag(self, DetailFlag):  # Boolean
		self.add_query_param('DetailFlag', DetailFlag)
