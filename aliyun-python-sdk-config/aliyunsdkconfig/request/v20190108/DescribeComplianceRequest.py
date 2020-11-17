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

class DescribeComplianceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Config', '2019-01-08', 'DescribeCompliance','Config')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfigRuleId(self):
		return self.get_query_params().get('ConfigRuleId')

	def set_ConfigRuleId(self,ConfigRuleId):
		self.add_query_param('ConfigRuleId',ConfigRuleId)

	def get_ResourceId(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self,ResourceId):
		self.add_query_param('ResourceId',ResourceId)

	def get_MultiAccount(self):
		return self.get_query_params().get('MultiAccount')

	def set_MultiAccount(self,MultiAccount):
		self.add_query_param('MultiAccount',MultiAccount)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_ComplianceType(self):
		return self.get_query_params().get('ComplianceType')

	def set_ComplianceType(self,ComplianceType):
		self.add_query_param('ComplianceType',ComplianceType)

	def get_MemberId(self):
		return self.get_query_params().get('MemberId')

	def set_MemberId(self,MemberId):
		self.add_query_param('MemberId',MemberId)