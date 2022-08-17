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

class DescribeDiskReplicaPairsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ebs', '2021-07-30', 'DescribeDiskReplicaPairs','ebs')
		self.set_method('POST')

	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_PairIds(self): # String
		return self.get_query_params().get('PairIds')

	def set_PairIds(self, PairIds):  # String
		self.add_query_param('PairIds', PairIds)
	def get_ReplicaGroupId(self): # String
		return self.get_query_params().get('ReplicaGroupId')

	def set_ReplicaGroupId(self, ReplicaGroupId):  # String
		self.add_query_param('ReplicaGroupId', ReplicaGroupId)
	def get_Site(self): # String
		return self.get_query_params().get('Site')

	def set_Site(self, Site):  # String
		self.add_query_param('Site', Site)
	def get_MaxResults(self): # Long
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_query_param('MaxResults', MaxResults)
