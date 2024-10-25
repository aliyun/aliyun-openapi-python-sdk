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
from aliyunsdkvpc.endpoint import endpoint_data

class DescribeExpressConnectTrafficQosRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'DescribeExpressConnectTrafficQosRule','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RuleIdLists(self): # RepeatList
		return self.get_query_params().get('RuleIdList')

	def set_RuleIdLists(self, RuleIdList):  # RepeatList
		for depth1 in range(len(RuleIdList)):
			self.add_query_param('RuleIdList.' + str(depth1 + 1), RuleIdList[depth1])
	def get_QosId(self): # String
		return self.get_query_params().get('QosId')

	def set_QosId(self, QosId):  # String
		self.add_query_param('QosId', QosId)
	def get_QueueId(self): # String
		return self.get_query_params().get('QueueId')

	def set_QueueId(self, QueueId):  # String
		self.add_query_param('QueueId', QueueId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RuleNameLists(self): # RepeatList
		return self.get_query_params().get('RuleNameList')

	def set_RuleNameLists(self, RuleNameList):  # RepeatList
		for depth1 in range(len(RuleNameList)):
			self.add_query_param('RuleNameList.' + str(depth1 + 1), RuleNameList[depth1])
