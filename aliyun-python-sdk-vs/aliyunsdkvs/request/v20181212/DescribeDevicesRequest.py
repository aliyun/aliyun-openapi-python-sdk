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
from aliyunsdkvs.endpoint import endpoint_data

class DescribeDevicesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'DescribeDevices','vs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SortDirection(self):
		return self.get_query_params().get('SortDirection')

	def set_SortDirection(self,SortDirection):
		self.add_query_param('SortDirection',SortDirection)

	def get_IncludeDirectory(self):
		return self.get_query_params().get('IncludeDirectory')

	def set_IncludeDirectory(self,IncludeDirectory):
		self.add_query_param('IncludeDirectory',IncludeDirectory)

	def get_GbId(self):
		return self.get_query_params().get('GbId')

	def set_GbId(self,GbId):
		self.add_query_param('GbId',GbId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_ParentId(self):
		return self.get_query_params().get('ParentId')

	def set_ParentId(self,ParentId):
		self.add_query_param('ParentId',ParentId)

	def get_IncludeStats(self):
		return self.get_query_params().get('IncludeStats')

	def set_IncludeStats(self,IncludeStats):
		self.add_query_param('IncludeStats',IncludeStats)

	def get_Vendor(self):
		return self.get_query_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_query_param('Vendor',Vendor)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DirectoryId(self):
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self,DirectoryId):
		self.add_query_param('DirectoryId',DirectoryId)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_SortBy(self):
		return self.get_query_params().get('SortBy')

	def set_SortBy(self,SortBy):
		self.add_query_param('SortBy',SortBy)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)