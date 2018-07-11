# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeScalingInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingInstances','ess')

	def get_InstanceId10(self):
		return self.get_query_params().get('InstanceId.10')

	def set_InstanceId10(self,InstanceId10):
		self.add_query_param('InstanceId.10',InstanceId10)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_InstanceId12(self):
		return self.get_query_params().get('InstanceId.12')

	def set_InstanceId12(self,InstanceId12):
		self.add_query_param('InstanceId.12',InstanceId12)

	def get_InstanceId11(self):
		return self.get_query_params().get('InstanceId.11')

	def set_InstanceId11(self,InstanceId11):
		self.add_query_param('InstanceId.11',InstanceId11)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_LifecycleState(self):
		return self.get_query_params().get('LifecycleState')

	def set_LifecycleState(self,LifecycleState):
		self.add_query_param('LifecycleState',LifecycleState)

	def get_CreationType(self):
		return self.get_query_params().get('CreationType')

	def set_CreationType(self,CreationType):
		self.add_query_param('CreationType',CreationType)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_InstanceId20(self):
		return self.get_query_params().get('InstanceId.20')

	def set_InstanceId20(self,InstanceId20):
		self.add_query_param('InstanceId.20',InstanceId20)

	def get_InstanceId1(self):
		return self.get_query_params().get('InstanceId.1')

	def set_InstanceId1(self,InstanceId1):
		self.add_query_param('InstanceId.1',InstanceId1)

	def get_InstanceId3(self):
		return self.get_query_params().get('InstanceId.3')

	def set_InstanceId3(self,InstanceId3):
		self.add_query_param('InstanceId.3',InstanceId3)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_InstanceId2(self):
		return self.get_query_params().get('InstanceId.2')

	def set_InstanceId2(self,InstanceId2):
		self.add_query_param('InstanceId.2',InstanceId2)

	def get_InstanceId5(self):
		return self.get_query_params().get('InstanceId.5')

	def set_InstanceId5(self,InstanceId5):
		self.add_query_param('InstanceId.5',InstanceId5)

	def get_InstanceId4(self):
		return self.get_query_params().get('InstanceId.4')

	def set_InstanceId4(self,InstanceId4):
		self.add_query_param('InstanceId.4',InstanceId4)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceId7(self):
		return self.get_query_params().get('InstanceId.7')

	def set_InstanceId7(self,InstanceId7):
		self.add_query_param('InstanceId.7',InstanceId7)

	def get_InstanceId6(self):
		return self.get_query_params().get('InstanceId.6')

	def set_InstanceId6(self,InstanceId6):
		self.add_query_param('InstanceId.6',InstanceId6)

	def get_InstanceId9(self):
		return self.get_query_params().get('InstanceId.9')

	def set_InstanceId9(self,InstanceId9):
		self.add_query_param('InstanceId.9',InstanceId9)

	def get_InstanceId8(self):
		return self.get_query_params().get('InstanceId.8')

	def set_InstanceId8(self,InstanceId8):
		self.add_query_param('InstanceId.8',InstanceId8)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ScalingConfigurationId(self):
		return self.get_query_params().get('ScalingConfigurationId')

	def set_ScalingConfigurationId(self,ScalingConfigurationId):
		self.add_query_param('ScalingConfigurationId',ScalingConfigurationId)

	def get_HealthStatus(self):
		return self.get_query_params().get('HealthStatus')

	def set_HealthStatus(self,HealthStatus):
		self.add_query_param('HealthStatus',HealthStatus)

	def get_InstanceId18(self):
		return self.get_query_params().get('InstanceId.18')

	def set_InstanceId18(self,InstanceId18):
		self.add_query_param('InstanceId.18',InstanceId18)

	def get_InstanceId17(self):
		return self.get_query_params().get('InstanceId.17')

	def set_InstanceId17(self,InstanceId17):
		self.add_query_param('InstanceId.17',InstanceId17)

	def get_InstanceId19(self):
		return self.get_query_params().get('InstanceId.19')

	def set_InstanceId19(self,InstanceId19):
		self.add_query_param('InstanceId.19',InstanceId19)

	def get_InstanceId14(self):
		return self.get_query_params().get('InstanceId.14')

	def set_InstanceId14(self,InstanceId14):
		self.add_query_param('InstanceId.14',InstanceId14)

	def get_InstanceId13(self):
		return self.get_query_params().get('InstanceId.13')

	def set_InstanceId13(self,InstanceId13):
		self.add_query_param('InstanceId.13',InstanceId13)

	def get_InstanceId16(self):
		return self.get_query_params().get('InstanceId.16')

	def set_InstanceId16(self,InstanceId16):
		self.add_query_param('InstanceId.16',InstanceId16)

	def get_InstanceId15(self):
		return self.get_query_params().get('InstanceId.15')

	def set_InstanceId15(self,InstanceId15):
		self.add_query_param('InstanceId.15',InstanceId15)