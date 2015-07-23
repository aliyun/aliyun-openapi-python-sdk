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
class DescribeScalingGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingGroups')

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

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ScalingGroupId1(self):
		return self.get_query_params().get('ScalingGroupId1')

	def set_ScalingGroupId1(self,ScalingGroupId1):
		self.add_query_param('ScalingGroupId1',ScalingGroupId1)

	def get_ScalingGroupId2(self):
		return self.get_query_params().get('ScalingGroupId2')

	def set_ScalingGroupId2(self,ScalingGroupId2):
		self.add_query_param('ScalingGroupId2',ScalingGroupId2)

	def get_ScalingGroupId3(self):
		return self.get_query_params().get('ScalingGroupId3')

	def set_ScalingGroupId3(self,ScalingGroupId3):
		self.add_query_param('ScalingGroupId3',ScalingGroupId3)

	def get_ScalingGroupId4(self):
		return self.get_query_params().get('ScalingGroupId4')

	def set_ScalingGroupId4(self,ScalingGroupId4):
		self.add_query_param('ScalingGroupId4',ScalingGroupId4)

	def get_ScalingGroupId5(self):
		return self.get_query_params().get('ScalingGroupId5')

	def set_ScalingGroupId5(self,ScalingGroupId5):
		self.add_query_param('ScalingGroupId5',ScalingGroupId5)

	def get_ScalingGroupId6(self):
		return self.get_query_params().get('ScalingGroupId6')

	def set_ScalingGroupId6(self,ScalingGroupId6):
		self.add_query_param('ScalingGroupId6',ScalingGroupId6)

	def get_ScalingGroupId7(self):
		return self.get_query_params().get('ScalingGroupId7')

	def set_ScalingGroupId7(self,ScalingGroupId7):
		self.add_query_param('ScalingGroupId7',ScalingGroupId7)

	def get_ScalingGroupId8(self):
		return self.get_query_params().get('ScalingGroupId8')

	def set_ScalingGroupId8(self,ScalingGroupId8):
		self.add_query_param('ScalingGroupId8',ScalingGroupId8)

	def get_ScalingGroupId9(self):
		return self.get_query_params().get('ScalingGroupId9')

	def set_ScalingGroupId9(self,ScalingGroupId9):
		self.add_query_param('ScalingGroupId9',ScalingGroupId9)

	def get_ScalingGroupId10(self):
		return self.get_query_params().get('ScalingGroupId10')

	def set_ScalingGroupId10(self,ScalingGroupId10):
		self.add_query_param('ScalingGroupId10',ScalingGroupId10)

	def get_ScalingGroupId12(self):
		return self.get_query_params().get('ScalingGroupId12')

	def set_ScalingGroupId12(self,ScalingGroupId12):
		self.add_query_param('ScalingGroupId12',ScalingGroupId12)

	def get_ScalingGroupId13(self):
		return self.get_query_params().get('ScalingGroupId13')

	def set_ScalingGroupId13(self,ScalingGroupId13):
		self.add_query_param('ScalingGroupId13',ScalingGroupId13)

	def get_ScalingGroupId14(self):
		return self.get_query_params().get('ScalingGroupId14')

	def set_ScalingGroupId14(self,ScalingGroupId14):
		self.add_query_param('ScalingGroupId14',ScalingGroupId14)

	def get_ScalingGroupId15(self):
		return self.get_query_params().get('ScalingGroupId15')

	def set_ScalingGroupId15(self,ScalingGroupId15):
		self.add_query_param('ScalingGroupId15',ScalingGroupId15)

	def get_ScalingGroupId16(self):
		return self.get_query_params().get('ScalingGroupId16')

	def set_ScalingGroupId16(self,ScalingGroupId16):
		self.add_query_param('ScalingGroupId16',ScalingGroupId16)

	def get_ScalingGroupId17(self):
		return self.get_query_params().get('ScalingGroupId17')

	def set_ScalingGroupId17(self,ScalingGroupId17):
		self.add_query_param('ScalingGroupId17',ScalingGroupId17)

	def get_ScalingGroupId18(self):
		return self.get_query_params().get('ScalingGroupId18')

	def set_ScalingGroupId18(self,ScalingGroupId18):
		self.add_query_param('ScalingGroupId18',ScalingGroupId18)

	def get_ScalingGroupId19(self):
		return self.get_query_params().get('ScalingGroupId19')

	def set_ScalingGroupId19(self,ScalingGroupId19):
		self.add_query_param('ScalingGroupId19',ScalingGroupId19)

	def get_ScalingGroupId20(self):
		return self.get_query_params().get('ScalingGroupId20')

	def set_ScalingGroupId20(self,ScalingGroupId20):
		self.add_query_param('ScalingGroupId20',ScalingGroupId20)

	def get_ScalingGroupName1(self):
		return self.get_query_params().get('ScalingGroupName1')

	def set_ScalingGroupName1(self,ScalingGroupName1):
		self.add_query_param('ScalingGroupName1',ScalingGroupName1)

	def get_ScalingGroupName2(self):
		return self.get_query_params().get('ScalingGroupName2')

	def set_ScalingGroupName2(self,ScalingGroupName2):
		self.add_query_param('ScalingGroupName2',ScalingGroupName2)

	def get_ScalingGroupName3(self):
		return self.get_query_params().get('ScalingGroupName3')

	def set_ScalingGroupName3(self,ScalingGroupName3):
		self.add_query_param('ScalingGroupName3',ScalingGroupName3)

	def get_ScalingGroupName4(self):
		return self.get_query_params().get('ScalingGroupName4')

	def set_ScalingGroupName4(self,ScalingGroupName4):
		self.add_query_param('ScalingGroupName4',ScalingGroupName4)

	def get_ScalingGroupName5(self):
		return self.get_query_params().get('ScalingGroupName5')

	def set_ScalingGroupName5(self,ScalingGroupName5):
		self.add_query_param('ScalingGroupName5',ScalingGroupName5)

	def get_ScalingGroupName6(self):
		return self.get_query_params().get('ScalingGroupName6')

	def set_ScalingGroupName6(self,ScalingGroupName6):
		self.add_query_param('ScalingGroupName6',ScalingGroupName6)

	def get_ScalingGroupName7(self):
		return self.get_query_params().get('ScalingGroupName7')

	def set_ScalingGroupName7(self,ScalingGroupName7):
		self.add_query_param('ScalingGroupName7',ScalingGroupName7)

	def get_ScalingGroupName8(self):
		return self.get_query_params().get('ScalingGroupName8')

	def set_ScalingGroupName8(self,ScalingGroupName8):
		self.add_query_param('ScalingGroupName8',ScalingGroupName8)

	def get_ScalingGroupName9(self):
		return self.get_query_params().get('ScalingGroupName9')

	def set_ScalingGroupName9(self,ScalingGroupName9):
		self.add_query_param('ScalingGroupName9',ScalingGroupName9)

	def get_ScalingGroupName10(self):
		return self.get_query_params().get('ScalingGroupName10')

	def set_ScalingGroupName10(self,ScalingGroupName10):
		self.add_query_param('ScalingGroupName10',ScalingGroupName10)

	def get_ScalingGroupName11(self):
		return self.get_query_params().get('ScalingGroupName11')

	def set_ScalingGroupName11(self,ScalingGroupName11):
		self.add_query_param('ScalingGroupName11',ScalingGroupName11)

	def get_ScalingGroupName12(self):
		return self.get_query_params().get('ScalingGroupName12')

	def set_ScalingGroupName12(self,ScalingGroupName12):
		self.add_query_param('ScalingGroupName12',ScalingGroupName12)

	def get_ScalingGroupName13(self):
		return self.get_query_params().get('ScalingGroupName13')

	def set_ScalingGroupName13(self,ScalingGroupName13):
		self.add_query_param('ScalingGroupName13',ScalingGroupName13)

	def get_ScalingGroupName14(self):
		return self.get_query_params().get('ScalingGroupName14')

	def set_ScalingGroupName14(self,ScalingGroupName14):
		self.add_query_param('ScalingGroupName14',ScalingGroupName14)

	def get_ScalingGroupName15(self):
		return self.get_query_params().get('ScalingGroupName15')

	def set_ScalingGroupName15(self,ScalingGroupName15):
		self.add_query_param('ScalingGroupName15',ScalingGroupName15)

	def get_ScalingGroupName16(self):
		return self.get_query_params().get('ScalingGroupName16')

	def set_ScalingGroupName16(self,ScalingGroupName16):
		self.add_query_param('ScalingGroupName16',ScalingGroupName16)

	def get_ScalingGroupName17(self):
		return self.get_query_params().get('ScalingGroupName17')

	def set_ScalingGroupName17(self,ScalingGroupName17):
		self.add_query_param('ScalingGroupName17',ScalingGroupName17)

	def get_ScalingGroupName18(self):
		return self.get_query_params().get('ScalingGroupName18')

	def set_ScalingGroupName18(self,ScalingGroupName18):
		self.add_query_param('ScalingGroupName18',ScalingGroupName18)

	def get_ScalingGroupName19(self):
		return self.get_query_params().get('ScalingGroupName19')

	def set_ScalingGroupName19(self,ScalingGroupName19):
		self.add_query_param('ScalingGroupName19',ScalingGroupName19)

	def get_ScalingGroupName20(self):
		return self.get_query_params().get('ScalingGroupName20')

	def set_ScalingGroupName20(self,ScalingGroupName20):
		self.add_query_param('ScalingGroupName20',ScalingGroupName20)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)