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

class GetResourceCountsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceCenter', '2022-12-01', 'GetResourceCounts')
		self.set_method('POST')

	def get_Filters(self): # RepeatList
		return self.get_query_params().get('Filter')

	def set_Filters(self, Filter):  # RepeatList
		for depth1 in range(len(Filter)):
			if Filter[depth1].get('MatchType') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.MatchType', Filter[depth1].get('MatchType'))
			if Filter[depth1].get('Value') is not None:
				for depth2 in range(len(Filter[depth1].get('Value'))):
					self.add_query_param('Filter.' + str(depth1 + 1) + '.Value.' + str(depth2 + 1), Filter[depth1].get('Value')[depth2])
			if Filter[depth1].get('Key') is not None:
				self.add_query_param('Filter.' + str(depth1 + 1) + '.Key', Filter[depth1].get('Key'))
	def get_GroupByKey(self): # String
		return self.get_query_params().get('GroupByKey')

	def set_GroupByKey(self, GroupByKey):  # String
		self.add_query_param('GroupByKey', GroupByKey)
