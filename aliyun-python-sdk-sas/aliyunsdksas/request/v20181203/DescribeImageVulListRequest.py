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
from aliyunsdksas.endpoint import endpoint_data

class DescribeImageVulListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageVulList','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_ContainerFieldName(self):
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self,ContainerFieldName):
		self.add_query_param('ContainerFieldName',ContainerFieldName)

	def get_Tag(self):
		return self.get_query_params().get('Tag')

	def set_Tag(self,Tag):
		self.add_query_param('Tag',Tag)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Necessity(self):
		return self.get_query_params().get('Necessity')

	def set_Necessity(self,Necessity):
		self.add_query_param('Necessity',Necessity)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_StatusList(self):
		return self.get_query_params().get('StatusList')

	def set_StatusList(self,StatusList):
		self.add_query_param('StatusList',StatusList)

	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_RepoNamespace(self):
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self,RepoNamespace):
		self.add_query_param('RepoNamespace',RepoNamespace)

	def get_ContainerFieldValue(self):
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self,ContainerFieldValue):
		self.add_query_param('ContainerFieldValue',ContainerFieldValue)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Digest(self):
		return self.get_query_params().get('Digest')

	def set_Digest(self,Digest):
		self.add_query_param('Digest',Digest)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_RepoName(self):
		return self.get_query_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_query_param('RepoName',RepoName)

	def get_RepoInstanceId(self):
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self,RepoInstanceId):
		self.add_query_param('RepoInstanceId',RepoInstanceId)

	def get_RepoRegionId(self):
		return self.get_query_params().get('RepoRegionId')

	def set_RepoRegionId(self,RepoRegionId):
		self.add_query_param('RepoRegionId',RepoRegionId)