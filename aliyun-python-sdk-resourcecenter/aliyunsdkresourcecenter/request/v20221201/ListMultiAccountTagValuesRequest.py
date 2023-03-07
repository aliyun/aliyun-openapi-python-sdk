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

class ListMultiAccountTagValuesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'ListMultiAccountTagValues')
		self.set_method('POST')

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Scope(self): # String
		return self.get_query_params().get('Scope')

	def set_Scope(self, Scope):  # String
		self.add_query_param('Scope', Scope)
	def get_MatchType(self): # String
		return self.get_query_params().get('MatchType')

	def set_MatchType(self, MatchType):  # String
		self.add_query_param('MatchType', MatchType)
	def get_TagValue(self): # String
		return self.get_query_params().get('TagValue')

	def set_TagValue(self, TagValue):  # String
		self.add_query_param('TagValue', TagValue)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_TagKey(self): # String
		return self.get_query_params().get('TagKey')

	def set_TagKey(self, TagKey):  # String
		self.add_query_param('TagKey', TagKey)
