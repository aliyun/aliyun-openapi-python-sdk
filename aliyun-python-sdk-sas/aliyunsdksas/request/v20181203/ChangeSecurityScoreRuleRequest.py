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
from aliyunsdksas.endpoint import endpoint_data

class ChangeSecurityScoreRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ChangeSecurityScoreRule','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResetSecurityScoreRule(self): # Boolean
		return self.get_query_params().get('ResetSecurityScoreRule')

	def set_ResetSecurityScoreRule(self, ResetSecurityScoreRule):  # Boolean
		self.add_query_param('ResetSecurityScoreRule', ResetSecurityScoreRule)
	def get_SecurityScoreRuleLists(self): # RepeatList
		return self.get_query_params().get('SecurityScoreRuleList')

	def set_SecurityScoreRuleLists(self, SecurityScoreRuleList):  # RepeatList
		for depth1 in range(len(SecurityScoreRuleList)):
			if SecurityScoreRuleList[depth1].get('Score') is not None:
				self.add_query_param('SecurityScoreRuleList.' + str(depth1 + 1) + '.Score', SecurityScoreRuleList[depth1].get('Score'))
			if SecurityScoreRuleList[depth1].get('SecurityScoreItemList') is not None:
				for depth2 in range(len(SecurityScoreRuleList[depth1].get('SecurityScoreItemList'))):
					if SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('Score') is not None:
						self.add_query_param('SecurityScoreRuleList.' + str(depth1 + 1) + '.SecurityScoreItemList.'  + str(depth2 + 1) + '.Score', SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('Score'))
					if SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('SubRuleType') is not None:
						self.add_query_param('SecurityScoreRuleList.' + str(depth1 + 1) + '.SecurityScoreItemList.'  + str(depth2 + 1) + '.SubRuleType', SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('SubRuleType'))
					if SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('ScoreThreshold') is not None:
						self.add_query_param('SecurityScoreRuleList.' + str(depth1 + 1) + '.SecurityScoreItemList.'  + str(depth2 + 1) + '.ScoreThreshold', SecurityScoreRuleList[depth1].get('SecurityScoreItemList')[depth2].get('ScoreThreshold'))
			if SecurityScoreRuleList[depth1].get('RuleType') is not None:
				self.add_query_param('SecurityScoreRuleList.' + str(depth1 + 1) + '.RuleType', SecurityScoreRuleList[depth1].get('RuleType'))
