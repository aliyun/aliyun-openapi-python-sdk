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

class PutExporterRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutExporterRule','cms')
		self.set_method('POST')

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_DstNamess(self):
		return self.get_query_params().get('DstNamess')

	def set_DstNamess(self,DstNamess):
		for i in range(len(DstNamess)):	
			if DstNamess[i] is not None:
				self.add_query_param('DstNames.' + str(i + 1) , DstNamess[i]);

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_TargetWindows(self):
		return self.get_query_params().get('TargetWindows')

	def set_TargetWindows(self,TargetWindows):
		self.add_query_param('TargetWindows',TargetWindows)

	def get_Describe(self):
		return self.get_query_params().get('Describe')

	def set_Describe(self,Describe):
		self.add_query_param('Describe',Describe)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)