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

class GetServiceTemplateParameterConstraintsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNest', '2021-06-01', 'GetServiceTemplateParameterConstraints','computenest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_EnablePrivateVpcConnection(self): # Boolean
		return self.get_query_params().get('EnablePrivateVpcConnection')

	def set_EnablePrivateVpcConnection(self, EnablePrivateVpcConnection):  # Boolean
		self.add_query_param('EnablePrivateVpcConnection', EnablePrivateVpcConnection)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_ServiceInstanceId(self): # String
		return self.get_query_params().get('ServiceInstanceId')

	def set_ServiceInstanceId(self, ServiceInstanceId):  # String
		self.add_query_param('ServiceInstanceId', ServiceInstanceId)
	def get_DeployRegionId(self): # String
		return self.get_query_params().get('DeployRegionId')

	def set_DeployRegionId(self, DeployRegionId):  # String
		self.add_query_param('DeployRegionId', DeployRegionId)
	def get_SpecificationName(self): # String
		return self.get_query_params().get('SpecificationName')

	def set_SpecificationName(self, SpecificationName):  # String
		self.add_query_param('SpecificationName', SpecificationName)
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
	def get_Parameterss(self): # RepeatList
		return self.get_query_params().get('Parameters')

	def set_Parameterss(self, Parameters):  # RepeatList
		for depth1 in range(len(Parameters)):
			if Parameters[depth1].get('ParameterValue') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterValue', Parameters[depth1].get('ParameterValue'))
			if Parameters[depth1].get('ParameterKey') is not None:
				self.add_query_param('Parameters.' + str(depth1 + 1) + '.ParameterKey', Parameters[depth1].get('ParameterKey'))
