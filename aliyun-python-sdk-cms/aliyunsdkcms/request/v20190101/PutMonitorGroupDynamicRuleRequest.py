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

class PutMonitorGroupDynamicRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutMonitorGroupDynamicRule','cms')
		self.set_method('POST')

	def get_GroupRuless(self):
		return self.get_query_params().get('GroupRules')

	def set_GroupRuless(self, GroupRuless):
		for depth1 in range(len(GroupRuless)):
			if GroupRuless[depth1].get('FilterRelation') is not None:
				self.add_query_param('GroupRules.' + str(depth1 + 1) + '.FilterRelation', GroupRuless[depth1].get('FilterRelation'))
			if GroupRuless[depth1].get('Filters') is not None:
				for depth2 in range(len(GroupRuless[depth1].get('Filters'))):
					if GroupRuless[depth1].get('Filters')[depth2].get('Function') is not None:
						self.add_query_param('GroupRules.' + str(depth1 + 1) + '.Filters.' + str(depth2 + 1) + '.Function', GroupRuless[depth1].get('Filters')[depth2].get('Function'))
					if GroupRuless[depth1].get('Filters')[depth2].get('Name') is not None:
						self.add_query_param('GroupRules.' + str(depth1 + 1) + '.Filters.' + str(depth2 + 1) + '.Name', GroupRuless[depth1].get('Filters')[depth2].get('Name'))
					if GroupRuless[depth1].get('Filters')[depth2].get('Value') is not None:
						self.add_query_param('GroupRules.' + str(depth1 + 1) + '.Filters.' + str(depth2 + 1) + '.Value', GroupRuless[depth1].get('Filters')[depth2].get('Value'))
			if GroupRuless[depth1].get('Category') is not None:
				self.add_query_param('GroupRules.' + str(depth1 + 1) + '.Category', GroupRuless[depth1].get('Category'))

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)