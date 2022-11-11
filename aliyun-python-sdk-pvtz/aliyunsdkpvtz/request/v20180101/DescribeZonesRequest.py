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
from aliyunsdkpvtz.endpoint import endpoint_data

class DescribeZonesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'pvtz', '2018-01-01', 'DescribeZones','pvtz')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueryVpcId(self): # String
		return self.get_query_params().get('QueryVpcId')

	def set_QueryVpcId(self, QueryVpcId):  # String
		self.add_query_param('QueryVpcId', QueryVpcId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ResourceTags(self): # RepeatList
		return self.get_query_params().get('ResourceTag')

	def set_ResourceTags(self, ResourceTag):  # RepeatList
		for depth1 in range(len(ResourceTag)):
			if ResourceTag[depth1].get('Value') is not None:
				self.add_query_param('ResourceTag.' + str(depth1 + 1) + '.Value', ResourceTag[depth1].get('Value'))
			if ResourceTag[depth1].get('Key') is not None:
				self.add_query_param('ResourceTag.' + str(depth1 + 1) + '.Key', ResourceTag[depth1].get('Key'))
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
	def get_ZoneTags(self): # RepeatList
		return self.get_query_params().get('ZoneTag')

	def set_ZoneTags(self, ZoneTag):  # RepeatList
		for depth1 in range(len(ZoneTag)):
			self.add_query_param('ZoneTag.' + str(depth1 + 1), ZoneTag[depth1])
	def get_SearchMode(self): # String
		return self.get_query_params().get('SearchMode')

	def set_SearchMode(self, SearchMode):  # String
		self.add_query_param('SearchMode', SearchMode)
	def get_ZoneType(self): # String
		return self.get_query_params().get('ZoneType')

	def set_ZoneType(self, ZoneType):  # String
		self.add_query_param('ZoneType', ZoneType)
	def get_QueryRegionId(self): # String
		return self.get_query_params().get('QueryRegionId')

	def set_QueryRegionId(self, QueryRegionId):  # String
		self.add_query_param('QueryRegionId', QueryRegionId)
