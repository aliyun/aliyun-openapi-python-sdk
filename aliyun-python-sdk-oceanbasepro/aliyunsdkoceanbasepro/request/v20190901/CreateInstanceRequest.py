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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'CreateInstance','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsolationOptimization(self): # String
		return self.get_body_params().get('IsolationOptimization')

	def set_IsolationOptimization(self, IsolationOptimization):  # String
		self.add_body_params('IsolationOptimization', IsolationOptimization)
	def get_InstanceClass(self): # String
		return self.get_body_params().get('InstanceClass')

	def set_InstanceClass(self, InstanceClass):  # String
		self.add_body_params('InstanceClass', InstanceClass)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_AutoRenewPeriod(self): # Long
		return self.get_body_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Long
		self.add_body_params('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # Long
		return self.get_body_params().get('Period')

	def set_Period(self, Period):  # Long
		self.add_body_params('Period', Period)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_DiskSize(self): # Long
		return self.get_body_params().get('DiskSize')

	def set_DiskSize(self, DiskSize):  # Long
		self.add_body_params('DiskSize', DiskSize)
	def get_Zones(self): # String
		return self.get_body_params().get('Zones')

	def set_Zones(self, Zones):  # String
		self.add_body_params('Zones', Zones)
	def get_DiskType(self): # String
		return self.get_body_params().get('DiskType')

	def set_DiskType(self, DiskType):  # String
		self.add_body_params('DiskType', DiskType)
	def get_ObVersion(self): # String
		return self.get_body_params().get('ObVersion')

	def set_ObVersion(self, ObVersion):  # String
		self.add_body_params('ObVersion', ObVersion)
	def get_PeriodUnit(self): # String
		return self.get_body_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_body_params('PeriodUnit', PeriodUnit)
	def get_InstanceName(self): # String
		return self.get_body_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_body_params('InstanceName', InstanceName)
	def get_ReplicaMode(self): # String
		return self.get_body_params().get('ReplicaMode')

	def set_ReplicaMode(self, ReplicaMode):  # String
		self.add_body_params('ReplicaMode', ReplicaMode)
	def get_AutoRenew(self): # Boolean
		return self.get_body_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_body_params('AutoRenew', AutoRenew)
	def get_Series(self): # String
		return self.get_body_params().get('Series')

	def set_Series(self, Series):  # String
		self.add_body_params('Series', Series)
	def get_CpuArch(self): # String
		return self.get_body_params().get('CpuArch')

	def set_CpuArch(self, CpuArch):  # String
		self.add_body_params('CpuArch', CpuArch)
	def get_PrimaryInstance(self): # String
		return self.get_body_params().get('PrimaryInstance')

	def set_PrimaryInstance(self, PrimaryInstance):  # String
		self.add_body_params('PrimaryInstance', PrimaryInstance)
	def get_PrimaryRegion(self): # String
		return self.get_body_params().get('PrimaryRegion')

	def set_PrimaryRegion(self, PrimaryRegion):  # String
		self.add_body_params('PrimaryRegion', PrimaryRegion)
	def get_ChargeType(self): # String
		return self.get_body_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_body_params('ChargeType', ChargeType)
