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
class DescribeSecurityGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeSecurityGroups')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_SecurityGroupIds(self):
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIds(self,SecurityGroupIds):
		self.add_query_param('SecurityGroupIds',SecurityGroupIds)

	def get_Tag1Key(self):
		return self.get_query_params().get('Tag.1.Key')

	def set_Tag1Key(self,Tag1Key):
		self.add_query_param('Tag.1.Key',Tag1Key)

	def get_Tag2Key(self):
		return self.get_query_params().get('Tag.2.Key')

	def set_Tag2Key(self,Tag2Key):
		self.add_query_param('Tag.2.Key',Tag2Key)

	def get_Tag3Key(self):
		return self.get_query_params().get('Tag.3.Key')

	def set_Tag3Key(self,Tag3Key):
		self.add_query_param('Tag.3.Key',Tag3Key)

	def get_Tag4Key(self):
		return self.get_query_params().get('Tag.4.Key')

	def set_Tag4Key(self,Tag4Key):
		self.add_query_param('Tag.4.Key',Tag4Key)

	def get_Tag5Key(self):
		return self.get_query_params().get('Tag.5.Key')

	def set_Tag5Key(self,Tag5Key):
		self.add_query_param('Tag.5.Key',Tag5Key)

	def get_Tag1Value(self):
		return self.get_query_params().get('Tag.1.Value')

	def set_Tag1Value(self,Tag1Value):
		self.add_query_param('Tag.1.Value',Tag1Value)

	def get_Tag2Value(self):
		return self.get_query_params().get('Tag.2.Value')

	def set_Tag2Value(self,Tag2Value):
		self.add_query_param('Tag.2.Value',Tag2Value)

	def get_Tag3Value(self):
		return self.get_query_params().get('Tag.3.Value')

	def set_Tag3Value(self,Tag3Value):
		self.add_query_param('Tag.3.Value',Tag3Value)

	def get_Tag4Value(self):
		return self.get_query_params().get('Tag.4.Value')

	def set_Tag4Value(self,Tag4Value):
		self.add_query_param('Tag.4.Value',Tag4Value)

	def get_Tag5Value(self):
		return self.get_query_params().get('Tag.5.Value')

	def set_Tag5Value(self,Tag5Value):
		self.add_query_param('Tag.5.Value',Tag5Value)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_SecurityGroupName(self):
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self,SecurityGroupName):
		self.add_query_param('SecurityGroupName',SecurityGroupName)

	def get_IsQueryEcsCount(self):
		return self.get_query_params().get('IsQueryEcsCount')

	def set_IsQueryEcsCount(self,IsQueryEcsCount):
		self.add_query_param('IsQueryEcsCount',IsQueryEcsCount)

	def get_FuzzyQuery(self):
		return self.get_query_params().get('FuzzyQuery')

	def set_FuzzyQuery(self,FuzzyQuery):
		self.add_query_param('FuzzyQuery',FuzzyQuery)