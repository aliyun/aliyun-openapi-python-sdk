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
class DescribeScalingActivitiesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingActivities','ess')

	def get_ScalingActivityId9(self):
		return self.get_query_params().get('ScalingActivityId.9')

	def set_ScalingActivityId9(self,ScalingActivityId9):
		self.add_query_param('ScalingActivityId.9',ScalingActivityId9)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ScalingActivityId5(self):
		return self.get_query_params().get('ScalingActivityId.5')

	def set_ScalingActivityId5(self,ScalingActivityId5):
		self.add_query_param('ScalingActivityId.5',ScalingActivityId5)

	def get_ScalingActivityId6(self):
		return self.get_query_params().get('ScalingActivityId.6')

	def set_ScalingActivityId6(self,ScalingActivityId6):
		self.add_query_param('ScalingActivityId.6',ScalingActivityId6)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_ScalingActivityId7(self):
		return self.get_query_params().get('ScalingActivityId.7')

	def set_ScalingActivityId7(self,ScalingActivityId7):
		self.add_query_param('ScalingActivityId.7',ScalingActivityId7)

	def get_ScalingActivityId8(self):
		return self.get_query_params().get('ScalingActivityId.8')

	def set_ScalingActivityId8(self,ScalingActivityId8):
		self.add_query_param('ScalingActivityId.8',ScalingActivityId8)

	def get_ScalingActivityId1(self):
		return self.get_query_params().get('ScalingActivityId.1')

	def set_ScalingActivityId1(self,ScalingActivityId1):
		self.add_query_param('ScalingActivityId.1',ScalingActivityId1)

	def get_ScalingActivityId2(self):
		return self.get_query_params().get('ScalingActivityId.2')

	def set_ScalingActivityId2(self,ScalingActivityId2):
		self.add_query_param('ScalingActivityId.2',ScalingActivityId2)

	def get_ScalingActivityId3(self):
		return self.get_query_params().get('ScalingActivityId.3')

	def set_ScalingActivityId3(self,ScalingActivityId3):
		self.add_query_param('ScalingActivityId.3',ScalingActivityId3)

	def get_ScalingActivityId4(self):
		return self.get_query_params().get('ScalingActivityId.4')

	def set_ScalingActivityId4(self,ScalingActivityId4):
		self.add_query_param('ScalingActivityId.4',ScalingActivityId4)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_StatusCode(self):
		return self.get_query_params().get('StatusCode')

	def set_StatusCode(self,StatusCode):
		self.add_query_param('StatusCode',StatusCode)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ScalingActivityId11(self):
		return self.get_query_params().get('ScalingActivityId.11')

	def set_ScalingActivityId11(self,ScalingActivityId11):
		self.add_query_param('ScalingActivityId.11',ScalingActivityId11)

	def get_ScalingActivityId10(self):
		return self.get_query_params().get('ScalingActivityId.10')

	def set_ScalingActivityId10(self,ScalingActivityId10):
		self.add_query_param('ScalingActivityId.10',ScalingActivityId10)

	def get_ScalingActivityId13(self):
		return self.get_query_params().get('ScalingActivityId.13')

	def set_ScalingActivityId13(self,ScalingActivityId13):
		self.add_query_param('ScalingActivityId.13',ScalingActivityId13)

	def get_ScalingActivityId12(self):
		return self.get_query_params().get('ScalingActivityId.12')

	def set_ScalingActivityId12(self,ScalingActivityId12):
		self.add_query_param('ScalingActivityId.12',ScalingActivityId12)

	def get_ScalingActivityId15(self):
		return self.get_query_params().get('ScalingActivityId.15')

	def set_ScalingActivityId15(self,ScalingActivityId15):
		self.add_query_param('ScalingActivityId.15',ScalingActivityId15)

	def get_ScalingActivityId14(self):
		return self.get_query_params().get('ScalingActivityId.14')

	def set_ScalingActivityId14(self,ScalingActivityId14):
		self.add_query_param('ScalingActivityId.14',ScalingActivityId14)

	def get_ScalingActivityId17(self):
		return self.get_query_params().get('ScalingActivityId.17')

	def set_ScalingActivityId17(self,ScalingActivityId17):
		self.add_query_param('ScalingActivityId.17',ScalingActivityId17)

	def get_ScalingActivityId16(self):
		return self.get_query_params().get('ScalingActivityId.16')

	def set_ScalingActivityId16(self,ScalingActivityId16):
		self.add_query_param('ScalingActivityId.16',ScalingActivityId16)

	def get_ScalingActivityId19(self):
		return self.get_query_params().get('ScalingActivityId.19')

	def set_ScalingActivityId19(self,ScalingActivityId19):
		self.add_query_param('ScalingActivityId.19',ScalingActivityId19)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_ScalingActivityId18(self):
		return self.get_query_params().get('ScalingActivityId.18')

	def set_ScalingActivityId18(self,ScalingActivityId18):
		self.add_query_param('ScalingActivityId.18',ScalingActivityId18)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ScalingActivityId20(self):
		return self.get_query_params().get('ScalingActivityId.20')

	def set_ScalingActivityId20(self,ScalingActivityId20):
		self.add_query_param('ScalingActivityId.20',ScalingActivityId20)