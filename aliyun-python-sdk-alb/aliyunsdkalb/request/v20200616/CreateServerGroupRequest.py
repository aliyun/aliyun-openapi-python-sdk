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

class CreateServerGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'CreateServerGroup','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CrossZoneEnabled(self): # Boolean
		return self.get_query_params().get('CrossZoneEnabled')

	def set_CrossZoneEnabled(self, CrossZoneEnabled):  # Boolean
		self.add_query_param('CrossZoneEnabled', CrossZoneEnabled)
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
				self.add_query_param('HealthCheckConfig.HealthCheckCodes.' + str(index1 + 1), value1)
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
				self.add_query_param('HealthCheckConfig.HealthCheckHttpCodes.' + str(index1 + 1), value1)
		if HealthCheckConfig.get('HealthCheckHttpVersion') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckHttpVersion', HealthCheckConfig.get('HealthCheckHttpVersion'))
		if HealthCheckConfig.get('HealthCheckConnectPort') is not None:
			self.add_query_param('HealthCheckConfig.HealthCheckConnectPort', HealthCheckConfig.get('HealthCheckConnectPort'))
	def get_SlowStartConfig(self): # Struct
		return self.get_query_params().get('SlowStartConfig')

	def set_SlowStartConfig(self, SlowStartConfig):  # Struct
		if SlowStartConfig.get('SlowStartDuration') is not None:
			self.add_query_param('SlowStartConfig.SlowStartDuration', SlowStartConfig.get('SlowStartDuration'))
		if SlowStartConfig.get('SlowStartEnabled') is not None:
			self.add_query_param('SlowStartConfig.SlowStartEnabled', SlowStartConfig.get('SlowStartEnabled'))
	def get_Scheduler(self): # String
		return self.get_query_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_query_param('Scheduler', Scheduler)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_UpstreamKeepaliveEnabled(self): # Boolean
		return self.get_query_params().get('UpstreamKeepaliveEnabled')

	def set_UpstreamKeepaliveEnabled(self, UpstreamKeepaliveEnabled):  # Boolean
		self.add_query_param('UpstreamKeepaliveEnabled', UpstreamKeepaliveEnabled)
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Value') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if value1.get('Key') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
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
	def get_ConnectionDrainConfig(self): # Struct
		return self.get_query_params().get('ConnectionDrainConfig')

	def set_ConnectionDrainConfig(self, ConnectionDrainConfig):  # Struct
		if ConnectionDrainConfig.get('ConnectionDrainEnabled') is not None:
			self.add_query_param('ConnectionDrainConfig.ConnectionDrainEnabled', ConnectionDrainConfig.get('ConnectionDrainEnabled'))
		if ConnectionDrainConfig.get('ConnectionDrainTimeout') is not None:
			self.add_query_param('ConnectionDrainConfig.ConnectionDrainTimeout', ConnectionDrainConfig.get('ConnectionDrainTimeout'))
	def get_ServerGroupType(self): # String
		return self.get_query_params().get('ServerGroupType')

	def set_ServerGroupType(self, ServerGroupType):  # String
		self.add_query_param('ServerGroupType', ServerGroupType)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_UchConfig(self): # Struct
		return self.get_query_params().get('UchConfig')

	def set_UchConfig(self, UchConfig):  # Struct
		if UchConfig.get('Type') is not None:
			self.add_query_param('UchConfig.Type', UchConfig.get('Type'))
		if UchConfig.get('Value') is not None:
			self.add_query_param('UchConfig.Value', UchConfig.get('Value'))
