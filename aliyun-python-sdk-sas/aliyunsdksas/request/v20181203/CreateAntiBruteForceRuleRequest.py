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

class CreateAntiBruteForceRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateAntiBruteForceRule','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ForbiddenTime(self):
		return self.get_query_params().get('ForbiddenTime')

	def set_ForbiddenTime(self,ForbiddenTime):
		self.add_query_param('ForbiddenTime',ForbiddenTime)

	def get_FailCount(self):
		return self.get_query_params().get('FailCount')

	def set_FailCount(self,FailCount):
		self.add_query_param('FailCount',FailCount)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_UuidLists(self):
		return self.get_query_params().get('UuidLists')

	def set_UuidLists(self, UuidLists):
		for depth1 in range(len(UuidLists)):
			if UuidLists[depth1] is not None:
				self.add_query_param('UuidList.' + str(depth1 + 1) , UuidLists[depth1])

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Span(self):
		return self.get_query_params().get('Span')

	def set_Span(self,Span):
		self.add_query_param('Span',Span)

	def get_DefaultRule(self):
		return self.get_query_params().get('DefaultRule')

	def set_DefaultRule(self,DefaultRule):
		self.add_query_param('DefaultRule',DefaultRule)