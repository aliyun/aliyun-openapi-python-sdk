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
		if HealthCheckConfig.get('HealthCheckCodes') is not None:
			for index1, value1 in enumerate(HealthCheckConfig.get('HealthCheckCodes')):
				self.add_query_param('HealthCheckConfig.HealthCheckCodes' + str(index1 + 1), value1)
		if HealthCheckConfig.get('HealthCheckEnabled') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckEnabled', HealthCheckConfig.get('HealthCheckEnabled'))
		if HealthCheckConfig.get('HealthCheckTimeout') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckTimeout', HealthCheckConfig.get('HealthCheckTimeout'))
		if HealthCheckConfig.get('HealthCheckMethod') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckMethod', HealthCheckConfig.get('HealthCheckMethod'))
		if HealthCheckConfig.get('HealthCheckHost') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckHost', HealthCheckConfig.get('HealthCheckHost'))
		if HealthCheckConfig.get('HealthCheckProtocol') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckProtocol', HealthCheckConfig.get('HealthCheckProtocol'))
		if HealthCheckConfig.get('UnhealthyThreshold') is not None:
			self.add_query_param('HealthCheckConfig.UnhealthyThreshold', HealthCheckConfig.get('UnhealthyThreshold'))
		if HealthCheckConfig.get('HealthyThreshold') is not None:
			self.add_query_param('HealthCheckConfig.HealthyThreshold', HealthCheckConfig.get('HealthyThreshold'))
		if HealthCheckConfig.get('HealthCheckTcpFastCloseEnabled') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckTcpFastCloseEnabled', HealthCheckConfig.get('HealthCheckTcpFastCloseEnabled'))
		if HealthCheckConfig.get('HealthCheckPath') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckPath', HealthCheckConfig.get('HealthCheckPath'))
		if HealthCheckConfig.get('HealthCheckInterval') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckInterval', HealthCheckConfig.get('HealthCheckInterval'))
		if HealthCheckConfig.get('HealthCheckHttpCodes') is not None:
			for index1, value1 in enumerate(HealthCheckConfig.get('HealthCheckHttpCodes')):
				self.add_query_param('HealthCheckConfig.HealthCheckHttpCodes' + str(index1 + 1), value1)
		if HealthCheckConfig.get('HealthCheckHttpVersion') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckHttpVersion', HealthCheckConfig.get('HealthCheckHttpVersion'))
		if HealthCheckConfig.get('HealthCheckConnectPort') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckConnectPort', HealthCheckConfig.get('HealthCheckConnectPort'))
	def get_Scheduler(self): # String
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_query_param('Scheduler', Scheduler)
	def get_ServerGroupId(self): # String
		return self.get_query_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_query_param('ServerGroupId', ServerGroupId)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_StickySessionConfig(self): # Struct
		return self.get_query_params().get('StickySessionConfig')

	def set_StickySessionConfig(self, StickySessionConfig):  # Struct
		if StickySessionConfig.get('StickySessionEnabled') is not None:
			self.add_query_param('StickySessionConfig.StickySessionEnabled', StickySessionConfig.get('StickySessionEnabled'))
		if StickySessionConfig.get('Cookie') is not None:
			self.add_query_param('StickySessionConfig.Cookie', StickySessionConfig.get('Cookie'))
		if StickySessionConfig.get('CookieTimeout') is not None:
			self.add_query_param('StickySessionConfig.CookieTimeout', StickySessionConfig.get('CookieTimeout'))
		if StickySessionConfig.get('StickySessionType') is not None:
			self.add_query_param('StickySessionConfig.StickySessionType', StickySessionConfig.get('StickySessionType'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
