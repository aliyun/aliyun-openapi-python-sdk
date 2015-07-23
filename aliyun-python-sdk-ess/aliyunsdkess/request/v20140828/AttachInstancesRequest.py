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
class AttachInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'AttachInstances')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_InstanceId1(self):
		return self.get_query_params().get('InstanceId1')

	def set_InstanceId1(self,InstanceId1):
		self.add_query_param('InstanceId1',InstanceId1)

	def get_InstanceId2(self):
		return self.get_query_params().get('InstanceId2')

	def set_InstanceId2(self,InstanceId2):
		self.add_query_param('InstanceId2',InstanceId2)

	def get_InstanceId3(self):
		return self.get_query_params().get('InstanceId3')

	def set_InstanceId3(self,InstanceId3):
		self.add_query_param('InstanceId3',InstanceId3)

	def get_InstanceId4(self):
		return self.get_query_params().get('InstanceId4')

	def set_InstanceId4(self,InstanceId4):
		self.add_query_param('InstanceId4',InstanceId4)

	def get_InstanceId5(self):
		return self.get_query_params().get('InstanceId5')

	def set_InstanceId5(self,InstanceId5):
		self.add_query_param('InstanceId5',InstanceId5)

	def get_InstanceId6(self):
		return self.get_query_params().get('InstanceId6')

	def set_InstanceId6(self,InstanceId6):
		self.add_query_param('InstanceId6',InstanceId6)

	def get_InstanceId7(self):
		return self.get_query_params().get('InstanceId7')

	def set_InstanceId7(self,InstanceId7):
		self.add_query_param('InstanceId7',InstanceId7)

	def get_InstanceId8(self):
		return self.get_query_params().get('InstanceId8')

	def set_InstanceId8(self,InstanceId8):
		self.add_query_param('InstanceId8',InstanceId8)

	def get_InstanceId9(self):
		return self.get_query_params().get('InstanceId9')

	def set_InstanceId9(self,InstanceId9):
		self.add_query_param('InstanceId9',InstanceId9)

	def get_InstanceId10(self):
		return self.get_query_params().get('InstanceId10')

	def set_InstanceId10(self,InstanceId10):
		self.add_query_param('InstanceId10',InstanceId10)

	def get_InstanceId11(self):
		return self.get_query_params().get('InstanceId11')

	def set_InstanceId11(self,InstanceId11):
		self.add_query_param('InstanceId11',InstanceId11)

	def get_InstanceId12(self):
		return self.get_query_params().get('InstanceId12')

	def set_InstanceId12(self,InstanceId12):
		self.add_query_param('InstanceId12',InstanceId12)

	def get_InstanceId13(self):
		return self.get_query_params().get('InstanceId13')

	def set_InstanceId13(self,InstanceId13):
		self.add_query_param('InstanceId13',InstanceId13)

	def get_InstanceId14(self):
		return self.get_query_params().get('InstanceId14')

	def set_InstanceId14(self,InstanceId14):
		self.add_query_param('InstanceId14',InstanceId14)

	def get_InstanceId15(self):
		return self.get_query_params().get('InstanceId15')

	def set_InstanceId15(self,InstanceId15):
		self.add_query_param('InstanceId15',InstanceId15)

	def get_InstanceId16(self):
		return self.get_query_params().get('InstanceId16')

	def set_InstanceId16(self,InstanceId16):
		self.add_query_param('InstanceId16',InstanceId16)

	def get_InstanceId17(self):
		return self.get_query_params().get('InstanceId17')

	def set_InstanceId17(self,InstanceId17):
		self.add_query_param('InstanceId17',InstanceId17)

	def get_InstanceId18(self):
		return self.get_query_params().get('InstanceId18')

	def set_InstanceId18(self,InstanceId18):
		self.add_query_param('InstanceId18',InstanceId18)

	def get_InstanceId19(self):
		return self.get_query_params().get('InstanceId19')

	def set_InstanceId19(self,InstanceId19):
		self.add_query_param('InstanceId19',InstanceId19)

	def get_InstanceId20(self):
		return self.get_query_params().get('InstanceId20')

	def set_InstanceId20(self,InstanceId20):
		self.add_query_param('InstanceId20',InstanceId20)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)