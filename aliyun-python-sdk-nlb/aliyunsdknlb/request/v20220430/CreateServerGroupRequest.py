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
from aliyunsdknlb.endpoint import endpoint_data

class CreateServerGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'CreateServerGroup','nlb')
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
	def get_PreserveClientIpEnabled(self): # Boolean
		return self.get_body_params().get('PreserveClientIpEnabled')

	def set_PreserveClientIpEnabled(self, PreserveClientIpEnabled):  # Boolean
		self.add_body_params('PreserveClientIpEnabled', PreserveClientIpEnabled)
	def get_HealthCheckConfig(self): # Struct
		return self.get_body_params().get('HealthCheckConfig')

	def set_HealthCheckConfig(self, HealthCheckConfig):  # Struct
		if HealthCheckConfig.get('HealthCheckEnabled') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckEnabled', HealthCheckConfig.get('HealthCheckEnabled'))
		if HealthCheckConfig.get('HealthCheckType') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckType', HealthCheckConfig.get('HealthCheckType'))
		if HealthCheckConfig.get('HealthCheckConnectPort') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckConnectPort', HealthCheckConfig.get('HealthCheckConnectPort'))
		if HealthCheckConfig.get('HealthyThreshold') is not None:
			self.add_body_params('HealthCheckConfig.HealthyThreshold', HealthCheckConfig.get('HealthyThreshold'))
		if HealthCheckConfig.get('UnhealthyThreshold') is not None:
			self.add_body_params('HealthCheckConfig.UnhealthyThreshold', HealthCheckConfig.get('UnhealthyThreshold'))
		if HealthCheckConfig.get('HealthCheckConnectTimeout') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckConnectTimeout', HealthCheckConfig.get('HealthCheckConnectTimeout'))
		if HealthCheckConfig.get('HealthCheckInterval') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckInterval', HealthCheckConfig.get('HealthCheckInterval'))
		if HealthCheckConfig.get('HealthCheckDomain') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckDomain', HealthCheckConfig.get('HealthCheckDomain'))
		if HealthCheckConfig.get('HealthCheckUrl') is not None:
			self.add_body_params('HealthCheckConfig.HealthCheckUrl', HealthCheckConfig.get('HealthCheckUrl'))
		if HealthCheckConfig.get('HealthCheckHttpCode') is not None:
			for index1, value1 in enumerate(HealthCheckConfig.get('HealthCheckHttpCode')):
				self.add_body_params('HealthCheckConfig.HealthCheckHttpCode.' + str(index1 + 1), value1)
		if HealthCheckConfig.get('HttpCheckMethod') is not None:
			self.add_body_params('HealthCheckConfig.HttpCheckMethod', HealthCheckConfig.get('HttpCheckMethod'))
	def get_AddressIPVersion(self): # String
		return self.get_body_params().get('AddressIPVersion')

	def set_AddressIPVersion(self, AddressIPVersion):  # String
		self.add_body_params('AddressIPVersion', AddressIPVersion)
	def get_Scheduler(self): # String
		return self.get_body_params().get('Scheduler')

	def set_Scheduler(self, Scheduler):  # String
		self.add_body_params('Scheduler', Scheduler)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_Protocol(self): # String
		return self.get_body_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_body_params('Protocol', Protocol)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ConnectionDrainEnabled(self): # Boolean
		return self.get_body_params().get('ConnectionDrainEnabled')

	def set_ConnectionDrainEnabled(self, ConnectionDrainEnabled):  # Boolean
		self.add_body_params('ConnectionDrainEnabled', ConnectionDrainEnabled)
	def get_ConnectionDrainTimeout(self): # Integer
		return self.get_body_params().get('ConnectionDrainTimeout')

	def set_ConnectionDrainTimeout(self, ConnectionDrainTimeout):  # Integer
		self.add_body_params('ConnectionDrainTimeout', ConnectionDrainTimeout)
	def get_AnyPortEnabled(self): # Boolean
		return self.get_body_params().get('AnyPortEnabled')

	def set_AnyPortEnabled(self, AnyPortEnabled):  # Boolean
		self.add_body_params('AnyPortEnabled', AnyPortEnabled)
	def get_ServerGroupType(self): # String
		return self.get_body_params().get('ServerGroupType')

	def set_ServerGroupType(self, ServerGroupType):  # String
		self.add_body_params('ServerGroupType', ServerGroupType)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
