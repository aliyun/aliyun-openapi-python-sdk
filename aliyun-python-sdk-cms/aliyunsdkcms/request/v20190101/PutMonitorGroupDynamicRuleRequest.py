# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
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

	def get_GroupRuless(self):
		return self.get_query_params().get('GroupRuless')

	def set_GroupRuless(self,GroupRuless):
		for i in range(len(GroupRuless)):	
			if GroupRuless[i].get('FilterRelation') is not None:
				self.add_query_param('GroupRules.' + str(i + 1) + '.FilterRelation' , GroupRuless[i].get('FilterRelation'))
			for j in range(len(GroupRuless[i].get('Filterss'))):
				if GroupRuless[i].get('Filterss')[j] is not None:
					self.add_query_param('GroupRules.' + str(i + 1) + '.Filters.'+str(j + 1), GroupRuless[i].get('Filterss')[j])
			if GroupRuless[i].get('Category') is not None:
				self.add_query_param('GroupRules.' + str(i + 1) + '.Category' , GroupRuless[i].get('Category'))


	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)