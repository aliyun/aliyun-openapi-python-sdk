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
from aliyunsdkconfig.endpoint import endpoint_data

class ListAggregateConfigRuleEvaluationResultsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2020-09-07', 'ListAggregateConfigRuleEvaluationResults')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ConfigRuleId(self): # String
		return self.get_query_params().get('ConfigRuleId')

	def set_ConfigRuleId(self, ConfigRuleId):  # String
		self.add_query_param('ConfigRuleId', ConfigRuleId)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AggregatorId(self): # String
		return self.get_query_params().get('AggregatorId')

	def set_AggregatorId(self, AggregatorId):  # String
		self.add_query_param('AggregatorId', AggregatorId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_CompliancePackId(self): # String
		return self.get_query_params().get('CompliancePackId')

	def set_CompliancePackId(self, CompliancePackId):  # String
		self.add_query_param('CompliancePackId', CompliancePackId)
	def get_ComplianceType(self): # String
		return self.get_query_params().get('ComplianceType')

	def set_ComplianceType(self, ComplianceType):  # String
		self.add_query_param('ComplianceType', ComplianceType)
