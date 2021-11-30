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
from aliyunsdkalb.endpoint import endpoint_data

class UpdateHealthCheckTemplateAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateHealthCheckTemplateAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_HealthCheckTimeout(self): # Integer
		return self.get_query_params().get('HealthCheckTimeout')

	def set_HealthCheckTimeout(self, HealthCheckTimeout):  # Integer
		self.add_query_param('HealthCheckTimeout', HealthCheckTimeout)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_HealthCheckProtocol(self): # String
		return self.get_query_params().get('HealthCheckProtocol')

	def set_HealthCheckProtocol(self, HealthCheckProtocol):  # String
		self.add_query_param('HealthCheckProtocol', HealthCheckProtocol)
	def get_UnhealthyThreshold(self): # Integer
		return self.get_query_params().get('UnhealthyThreshold')

	def set_UnhealthyThreshold(self, UnhealthyThreshold):  # Integer
		self.add_query_param('UnhealthyThreshold', UnhealthyThreshold)
	def get_HealthyThreshold(self): # Integer
		return self.get_query_params().get('HealthyThreshold')

	def set_HealthyThreshold(self, HealthyThreshold):  # Integer
		self.add_query_param('HealthyThreshold', HealthyThreshold)
	def get_HealthCheckPath(self): # String
		return self.get_query_params().get('HealthCheckPath')

	def set_HealthCheckPath(self, HealthCheckPath):  # String
		self.add_query_param('HealthCheckPath', HealthCheckPath)
	def get_HealthCheckCodes(self): # Array
		return self.get_query_params().get('HealthCheckCodes')

	def set_HealthCheckCodes(self, HealthCheckCodes):  # Array
		for index1, value1 in enumerate(HealthCheckCodes):
			self.add_query_param('HealthCheckCodes.' + str(index1 + 1), value1)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_HealthCheckMethod(self): # String
		return self.get_query_params().get('HealthCheckMethod')

	def set_HealthCheckMethod(self, HealthCheckMethod):  # String
		self.add_query_param('HealthCheckMethod', HealthCheckMethod)
	def get_HealthCheckHost(self): # String
		return self.get_query_params().get('HealthCheckHost')

	def set_HealthCheckHost(self, HealthCheckHost):  # String
		self.add_query_param('HealthCheckHost', HealthCheckHost)
	def get_HealthCheckInterval(self): # Integer
		return self.get_query_params().get('HealthCheckInterval')

	def set_HealthCheckInterval(self, HealthCheckInterval):  # Integer
		self.add_query_param('HealthCheckInterval', HealthCheckInterval)
	def get_HealthCheckTemplateName(self): # String
		return self.get_query_params().get('HealthCheckTemplateName')

	def set_HealthCheckTemplateName(self, HealthCheckTemplateName):  # String
		self.add_query_param('HealthCheckTemplateName', HealthCheckTemplateName)
	def get_HealthCheckTemplateId(self): # String
		return self.get_query_params().get('HealthCheckTemplateId')

	def set_HealthCheckTemplateId(self, HealthCheckTemplateId):  # String
		self.add_query_param('HealthCheckTemplateId', HealthCheckTemplateId)
	def get_HealthCheckHttpVersion(self): # String
		return self.get_query_params().get('HealthCheckHttpVersion')

	def set_HealthCheckHttpVersion(self, HealthCheckHttpVersion):  # String
		self.add_query_param('HealthCheckHttpVersion', HealthCheckHttpVersion)
	def get_HealthCheckConnectPort(self): # Integer
		return self.get_query_params().get('HealthCheckConnectPort')

	def set_HealthCheckConnectPort(self, HealthCheckConnectPort):  # Integer
		self.add_query_param('HealthCheckConnectPort', HealthCheckConnectPort)
