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
from aliyunsdksmc.endpoint import endpoint_data

class CreateCrossZoneMigrationJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'smc', '2019-06-01', 'CreateCrossZoneMigrationJob','smc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TargetInstanceType(self): # String
		return self.get_query_params().get('TargetInstanceType')

	def set_TargetInstanceType(self, TargetInstanceType):  # String
		self.add_query_param('TargetInstanceType', TargetInstanceType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_TargetZoneId(self): # String
		return self.get_query_params().get('TargetZoneId')

	def set_TargetZoneId(self, TargetZoneId):  # String
		self.add_query_param('TargetZoneId', TargetZoneId)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_TargetVSwitchId(self): # String
		return self.get_query_params().get('TargetVSwitchId')

	def set_TargetVSwitchId(self, TargetVSwitchId):  # String
		self.add_query_param('TargetVSwitchId', TargetVSwitchId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Disks(self): # RepeatList
		return self.get_query_params().get('Disk')

	def set_Disks(self, Disk):  # RepeatList
		for depth1 in range(len(Disk)):
			if Disk[depth1].get('PerformanceLevel') is not None:
				self.add_query_param('Disk.' + str(depth1 + 1) + '.PerformanceLevel', Disk[depth1].get('PerformanceLevel'))
			if Disk[depth1].get('DiskId') is not None:
				self.add_query_param('Disk.' + str(depth1 + 1) + '.DiskId', Disk[depth1].get('DiskId'))
			if Disk[depth1].get('Category') is not None:
				self.add_query_param('Disk.' + str(depth1 + 1) + '.Category', Disk[depth1].get('Category'))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
