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
from aliyunsdkcomputenest.endpoint import endpoint_data

class GenerateServicePolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNest', '2021-06-01', 'GenerateServicePolicy','computenest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_OperationTypess(self): # RepeatList
		return self.get_query_params().get('OperationTypes')

	def set_OperationTypess(self, OperationTypes):  # RepeatList
		for depth1 in range(len(OperationTypes)):
			self.add_query_param('OperationTypes.' + str(depth1 + 1), OperationTypes[depth1])
	def get_TrialType(self): # String
		return self.get_query_params().get('TrialType')

	def set_TrialType(self, TrialType):  # String
		self.add_query_param('TrialType', TrialType)
	def get_ServiceVersion(self): # String
		return self.get_query_params().get('ServiceVersion')

	def set_ServiceVersion(self, ServiceVersion):  # String
		self.add_query_param('ServiceVersion', ServiceVersion)
	def get_ServiceId(self): # String
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # String
		self.add_query_param('ServiceId', ServiceId)
