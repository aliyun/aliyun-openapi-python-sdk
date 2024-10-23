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
from aliyunsdkgwlb.endpoint import endpoint_data

class UpdateServerGroupAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'UpdateServerGroupAttribute','gwlb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ServerGroupName(self): # String
		return self.get_body_params().get('ServerGroupName')

	def set_ServerGroupName(self, ServerGroupName):  # String
		self.add_body_params('ServerGroupName', ServerGroupName)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_HealthCheckConfig(self): # Struct
		return self.get_body_params().get('HealthCheckConfig')

	def set_HealthCheckConfig(self, HealthCheckConfig):  # Struct
		if HealthCheckConfig.get('HealthCheckConnectPort') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckConnectPort', HealthCheckConfig.get('HealthCheckConnectPort'))
		if HealthCheckConfig.get('HealthCheckConnectTimeout') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckConnectTimeout', HealthCheckConfig.get('HealthCheckConnectTimeout'))
		if HealthCheckConfig.get('HealthCheckDomain') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckDomain', HealthCheckConfig.get('HealthCheckDomain'))
		if HealthCheckConfig.get('HealthCheckEnabled') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckEnabled', HealthCheckConfig.get('HealthCheckEnabled'))
		if HealthCheckConfig.get('HealthCheckHttpCode') is not None:
			for index1, value1 in enumerate(HealthCheckConfig.get('HealthCheckHttpCode')):
				self.add_body_params('HealthCheckConfig.HealthCheckHttpCode.' + str(index1 + 1), value1)
		if HealthCheckConfig.get('HealthCheckInterval') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckInterval', HealthCheckConfig.get('HealthCheckInterval'))
		if HealthCheckConfig.get('HealthCheckPath') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckPath', HealthCheckConfig.get('HealthCheckPath'))
		if HealthCheckConfig.get('HealthCheckProtocol') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckProtocol', HealthCheckConfig.get('HealthCheckProtocol'))
		if HealthCheckConfig.get('HealthyThreshold') is not None:
			self.add_body_params('HealthCheckConfig.HealthyThreshold', HealthCheckConfig.get('HealthyThreshold'))
		if HealthCheckConfig.get('UnhealthyThreshold') is not None:
			self.add_body_params('HealthCheckConfig.UnhealthyThreshold', HealthCheckConfig.get('UnhealthyThreshold'))
	def get_ServerGroupId(self): # String
		return self.get_body_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_body_params('ServerGroupId', ServerGroupId)
	def get_Scheduler(self): # String
		return self.get_body_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_body_params('Scheduler', Scheduler)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ConnectionDrainConfig(self): # Struct
		return self.get_body_params().get('ConnectionDrainConfig')

	def set_ConnectionDrainConfig(self, ConnectionDrainConfig):  # Struct
		if ConnectionDrainConfig.get('ConnectionDrainEnabled') is not None:
			self.add_body_params('ConnectionDrainConfig.ConnectionDrainEnabled', ConnectionDrainConfig.get('ConnectionDrainEnabled'))
		if ConnectionDrainConfig.get('ConnectionDrainTimeout') is not None:
			self.add_body_params('ConnectionDrainConfig.ConnectionDrainTimeout', ConnectionDrainConfig.get('ConnectionDrainTimeout'))
