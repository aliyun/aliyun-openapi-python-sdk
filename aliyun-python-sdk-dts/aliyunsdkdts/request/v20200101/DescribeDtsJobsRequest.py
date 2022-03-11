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
from aliyunsdkdts.endpoint import endpoint_data

class DescribeDtsJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribeDtsJobs','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OrderDirection(self): # String
		return self.get_query_params().get('OrderDirection')

	def set_OrderDirection(self, OrderDirection):  # String
		self.add_query_param('OrderDirection', OrderDirection)
	def get_DedicatedClusterId(self): # String
		return self.get_query_params().get('DedicatedClusterId')

	def set_DedicatedClusterId(self, DedicatedClusterId):  # String
		self.add_query_param('DedicatedClusterId', DedicatedClusterId)
	def get_DedicatedClusterNodeId(self): # Long
		return self.get_query_params().get('DedicatedClusterNodeId')

	def set_DedicatedClusterNodeId(self, DedicatedClusterNodeId):  # Long
		self.add_query_param('DedicatedClusterNodeId', DedicatedClusterNodeId)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_OrderColumn(self): # String
		return self.get_query_params().get('OrderColumn')

	def set_OrderColumn(self, OrderColumn):  # String
		self.add_query_param('OrderColumn', OrderColumn)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_DtsJobId(self): # String
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_query_param('DtsJobId', DtsJobId)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_Params(self): # String
		return self.get_query_params().get('Params')

	def set_Params(self, Params):  # String
		self.add_query_param('Params', Params)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
	def get_JobType(self): # String
		return self.get_query_params().get('JobType')

	def set_JobType(self, JobType):  # String
		self.add_query_param('JobType', JobType)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
