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
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageVulList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Tag(self): # String
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_query_param('Tag', Tag)
	def get_AliasName(self): # String
		return self.get_query_params().get('AliasName')

	def set_AliasName(self, AliasName):  # String
		self.add_query_param('AliasName', AliasName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Necessity(self): # String
		return self.get_query_params().get('Necessity')

	def set_Necessity(self, Necessity):  # String
		self.add_query_param('Necessity', Necessity)
	def get_Uuids(self): # String
		return self.get_query_params().get('Uuids')

	def set_Uuids(self, Uuids):  # String
		self.add_query_param('Uuids', Uuids)
	def get_RepoId(self): # String
		return self.get_query_params().get('RepoId')

	def set_RepoId(self, RepoId):  # String
		self.add_query_param('RepoId', RepoId)
	def get_StatusList(self): # String
		return self.get_query_params().get('StatusList')

	def set_StatusList(self, StatusList):  # String
		self.add_query_param('StatusList', StatusList)
	def get_RepoNamespace(self): # String
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self, RepoNamespace):  # String
		self.add_query_param('RepoNamespace', RepoNamespace)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Digest(self): # String
		return self.get_query_params().get('Digest')

	def set_Digest(self, Digest):  # String
		self.add_query_param('Digest', Digest)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Dealed(self): # String
		return self.get_query_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_query_param('Dealed', Dealed)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_RepoName(self): # String
		return self.get_query_params().get('RepoName')

	def set_RepoName(self, RepoName):  # String
		self.add_query_param('RepoName', RepoName)
	def get_RepoInstanceId(self): # String
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self, RepoInstanceId):  # String
		self.add_query_param('RepoInstanceId', RepoInstanceId)
	def get_RepoRegionId(self): # String
		return self.get_query_params().get('RepoRegionId')

	def set_RepoRegionId(self, RepoRegionId):  # String
		self.add_query_param('RepoRegionId', RepoRegionId)
