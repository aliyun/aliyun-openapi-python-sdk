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

class ListResourceRelationshipsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'ListResourceRelationships')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_RelatedResourceFilters(self): # RepeatList
		return self.get_query_params().get('RelatedResourceFilter')

	def set_RelatedResourceFilters(self, RelatedResourceFilter):  # RepeatList
		for depth1 in range(len(RelatedResourceFilter)):
			if RelatedResourceFilter[depth1].get('MatchType') is not None:
				self.add_query_param('RelatedResourceFilter.' + str(depth1 + 1) + '.MatchType', RelatedResourceFilter[depth1].get('MatchType'))
			if RelatedResourceFilter[depth1].get('Value') is not None:
				for depth2 in range(len(RelatedResourceFilter[depth1].get('Value'))):
					self.add_query_param('RelatedResourceFilter.' + str(depth1 + 1) + '.Value.' + str(depth2 + 1), RelatedResourceFilter[depth1].get('Value')[depth2])
			if RelatedResourceFilter[depth1].get('Key') is not None:
				self.add_query_param('RelatedResourceFilter.' + str(depth1 + 1) + '.Key', RelatedResourceFilter[depth1].get('Key'))
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
