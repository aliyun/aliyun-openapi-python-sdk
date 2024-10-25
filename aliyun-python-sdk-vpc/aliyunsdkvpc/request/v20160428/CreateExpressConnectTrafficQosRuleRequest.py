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

class CreateExpressConnectTrafficQosRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateExpressConnectTrafficQosRule','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DstCidr(self): # String
		return self.get_query_params().get('DstCidr')

	def set_DstCidr(self, DstCidr):  # String
		self.add_query_param('DstCidr', DstCidr)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
	def get_SrcCidr(self): # String
		return self.get_query_params().get('SrcCidr')

	def set_SrcCidr(self, SrcCidr):  # String
		self.add_query_param('SrcCidr', SrcCidr)
	def get_DstIPv6Cidr(self): # String
		return self.get_query_params().get('DstIPv6Cidr')

	def set_DstIPv6Cidr(self, DstIPv6Cidr):  # String
		self.add_query_param('DstIPv6Cidr', DstIPv6Cidr)
	def get_DstPortRange(self): # String
		return self.get_query_params().get('DstPortRange')

	def set_DstPortRange(self, DstPortRange):  # String
		self.add_query_param('DstPortRange', DstPortRange)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_QosId(self): # String
		return self.get_query_params().get('QosId')

	def set_QosId(self, QosId):  # String
		self.add_query_param('QosId', QosId)
	def get_QueueId(self): # String
		return self.get_query_params().get('QueueId')

	def set_QueueId(self, QueueId):  # String
		self.add_query_param('QueueId', QueueId)
	def get_MatchDscp(self): # Integer
		return self.get_query_params().get('MatchDscp')

	def set_MatchDscp(self, MatchDscp):  # Integer
		self.add_query_param('MatchDscp', MatchDscp)
	def get_RuleDescription(self): # String
		return self.get_query_params().get('RuleDescription')

	def set_RuleDescription(self, RuleDescription):  # String
		self.add_query_param('RuleDescription', RuleDescription)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_RemarkingDscp(self): # Integer
		return self.get_query_params().get('RemarkingDscp')

	def set_RemarkingDscp(self, RemarkingDscp):  # Integer
		self.add_query_param('RemarkingDscp', RemarkingDscp)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SrcPortRange(self): # String
		return self.get_query_params().get('SrcPortRange')

	def set_SrcPortRange(self, SrcPortRange):  # String
		self.add_query_param('SrcPortRange', SrcPortRange)
	def get_SrcIPv6Cidr(self): # String
		return self.get_query_params().get('SrcIPv6Cidr')

	def set_SrcIPv6Cidr(self, SrcIPv6Cidr):  # String
		self.add_query_param('SrcIPv6Cidr', SrcIPv6Cidr)
