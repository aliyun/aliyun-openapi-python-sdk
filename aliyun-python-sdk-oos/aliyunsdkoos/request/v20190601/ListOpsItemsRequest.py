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
from aliyunsdkoos.endpoint import endpoint_data

class ListOpsItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'ListOpsItems','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceTags(self): # String
		return self.get_query_params().get('ResourceTags')

	def set_ResourceTags(self, ResourceTags):  # String
		self.add_query_param('ResourceTags', ResourceTags)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_Filters(self): # RepeatList
		return self.get_query_params().get('Filter')

	def set_Filters(self, Filter):  # RepeatList
		for depth1 in range(len(Filter)):
			if Filter[depth1].get('Name') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Name', Filter[depth1].get('Name'))
			if Filter[depth1].get('Value') is not None:
				for depth2 in range(len(Filter[depth1].get('Value'))):
					self.add_query_param('Filter.' + str(depth1 + 1) + '.Value.' + str(depth2 + 1), Filter[depth1].get('Value')[depth2])
			if Filter[depth1].get('Operator') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Operator', Filter[depth1].get('Operator'))
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
