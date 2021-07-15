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

class UpdateServerGroupAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateServerGroupAttribute','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ServerGroupName(self): # String
		return self.get_query_params().get('ServerGroupName')

	def set_ServerGroupName(self, ServerGroupName):  # String
		self.add_query_param('ServerGroupName', ServerGroupName)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_HealthCheckConfig(self): # Struct
		return self.get_query_params().get('HealthCheckConfig')

	def set_HealthCheckConfig(self, HealthCheckConfig):  # Struct
		for key1, value1 in HealthCheckConfig.items():
			for index2, value2 in enumerate(value1):
				self.add_query_param('HealthCheckConfig.' + key1 + '.' + str(index2 + 1) + '.String', value2)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckEnabled', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckTimeout', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckMethod', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckHost', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckProtocol', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.UnhealthyThreshold', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthyThreshold', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckPath', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckInterval', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckHttpVersion', value1)
			self.add_query_param('HealthCheckConfig.' + key1 + '.HealthCheckConnectPort', value1)
	def get_Scheduler(self): # String
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_query_param('Scheduler', Scheduler)
	def get_ServerGroupId(self): # String
		return self.get_query_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_query_param('ServerGroupId', ServerGroupId)
	def get_StickySessionConfig(self): # Struct
		return self.get_query_params().get('StickySessionConfig')

	def set_StickySessionConfig(self, StickySessionConfig):  # Struct
		for key1, value1 in StickySessionConfig.items():
			self.add_query_param('StickySessionConfig.' + key1 + '.StickySessionEnabled', value1)
			self.add_query_param('StickySessionConfig.' + key1 + '.Cookie', value1)
			self.add_query_param('StickySessionConfig.' + key1 + '.CookieTimeout', value1)
			self.add_query_param('StickySessionConfig.' + key1 + '.StickySessionType', value1)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
