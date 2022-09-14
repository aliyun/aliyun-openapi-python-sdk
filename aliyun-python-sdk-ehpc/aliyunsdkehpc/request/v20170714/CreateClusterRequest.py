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
from aliyunsdkehpc.endpoint import endpoint_data

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2017-07-14', 'CreateCluster')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SccClusterId(self): # String
		return self.get_query_params().get('SccClusterId')

	def set_SccClusterId(self, SccClusterId):  # String
		self.add_query_param('SccClusterId', SccClusterId)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_EcsOrderManagerInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Manager.InstanceType')

	def set_EcsOrderManagerInstanceType(self, EcsOrderManagerInstanceType):  # String
		self.add_query_param('EcsOrder.Manager.InstanceType', EcsOrderManagerInstanceType)
	def get_EhpcVersion(self): # String
		return self.get_query_params().get('EhpcVersion')

	def set_EhpcVersion(self, EhpcVersion):  # String
		self.add_query_param('EhpcVersion', EhpcVersion)
	def get_AccountType(self): # String
		return self.get_query_params().get('AccountType')

	def set_AccountType(self, AccountType):  # String
		self.add_query_param('AccountType', AccountType)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_SecurityGroupName(self): # String
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self, SecurityGroupName):  # String
		self.add_query_param('SecurityGroupName', SecurityGroupName)
	def get_EcsOrderComputeInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Compute.InstanceType')

	def set_EcsOrderComputeInstanceType(self, EcsOrderComputeInstanceType):  # String
		self.add_query_param('EcsOrder.Compute.InstanceType', EcsOrderComputeInstanceType)
	def get_ImageOwnerAlias(self): # String
		return self.get_query_params().get('ImageOwnerAlias')

	def set_ImageOwnerAlias(self, ImageOwnerAlias):  # String
		self.add_query_param('ImageOwnerAlias', ImageOwnerAlias)
	def get_VolumeType(self): # String
		return self.get_query_params().get('VolumeType')

	def set_VolumeType(self, VolumeType):  # String
		self.add_query_param('VolumeType', VolumeType)
	def get_EcsOrderManagerCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Manager.Count')

	def set_EcsOrderManagerCount(self, EcsOrderManagerCount):  # Integer
		self.add_query_param('EcsOrder.Manager.Count', EcsOrderManagerCount)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_EcsOrderLoginCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Login.Count')

	def set_EcsOrderLoginCount(self, EcsOrderLoginCount):  # Integer
		self.add_query_param('EcsOrder.Login.Count', EcsOrderLoginCount)
	def get_ComputeSpotPriceLimit(self): # String
		return self.get_query_params().get('ComputeSpotPriceLimit')

	def set_ComputeSpotPriceLimit(self, ComputeSpotPriceLimit):  # String
		self.add_query_param('ComputeSpotPriceLimit', ComputeSpotPriceLimit)
	def get_VolumeProtocol(self): # String
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self, VolumeProtocol):  # String
		self.add_query_param('VolumeProtocol', VolumeProtocol)
	def get_OsTag(self): # String
		return self.get_query_params().get('OsTag')

	def set_OsTag(self, OsTag):  # String
		self.add_query_param('OsTag', OsTag)
	def get_RemoteDirectory(self): # String
		return self.get_query_params().get('RemoteDirectory')

	def set_RemoteDirectory(self, RemoteDirectory):  # String
		self.add_query_param('RemoteDirectory', RemoteDirectory)
	def get_EcsOrderComputeCount(self): # Integer
		return self.get_query_params().get('EcsOrder.Compute.Count')

	def set_EcsOrderComputeCount(self, EcsOrderComputeCount):  # Integer
		self.add_query_param('EcsOrder.Compute.Count', EcsOrderComputeCount)
	def get_ComputeSpotStrategy(self): # String
		return self.get_query_params().get('ComputeSpotStrategy')

	def set_ComputeSpotStrategy(self, ComputeSpotStrategy):  # String
		self.add_query_param('ComputeSpotStrategy', ComputeSpotStrategy)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_Applications(self): # RepeatList
		return self.get_query_params().get('Application')

	def set_Applications(self, Application):  # RepeatList
		for depth1 in range(len(Application)):
			if Application[depth1].get('Tag') is not None:
				self.add_query_param('Application.' + str(depth1 + 1) + '.Tag', Application[depth1].get('Tag'))
	def get_EcsChargeType(self): # String
		return self.get_query_params().get('EcsChargeType')

	def set_EcsChargeType(self, EcsChargeType):  # String
		self.add_query_param('EcsChargeType', EcsChargeType)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_HaEnable(self): # Boolean
		return self.get_query_params().get('HaEnable')

	def set_HaEnable(self, HaEnable):  # Boolean
		self.add_query_param('HaEnable', HaEnable)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_SchedulerType(self): # String
		return self.get_query_params().get('SchedulerType')

	def set_SchedulerType(self, SchedulerType):  # String
		self.add_query_param('SchedulerType', SchedulerType)
	def get_VolumeId(self): # String
		return self.get_query_params().get('VolumeId')

	def set_VolumeId(self, VolumeId):  # String
		self.add_query_param('VolumeId', VolumeId)
	def get_VolumeMountpoint(self): # String
		return self.get_query_params().get('VolumeMountpoint')

	def set_VolumeMountpoint(self, VolumeMountpoint):  # String
		self.add_query_param('VolumeMountpoint', VolumeMountpoint)
	def get_EcsOrderLoginInstanceType(self): # String
		return self.get_query_params().get('EcsOrder.Login.InstanceType')

	def set_EcsOrderLoginInstanceType(self, EcsOrderLoginInstanceType):  # String
		self.add_query_param('EcsOrder.Login.InstanceType', EcsOrderLoginInstanceType)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
