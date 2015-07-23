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
class DescribeScalingRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScalingRules')

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

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_ScalingRuleId1(self):
		return self.get_query_params().get('ScalingRuleId1')

	def set_ScalingRuleId1(self,ScalingRuleId1):
		self.add_query_param('ScalingRuleId1',ScalingRuleId1)

	def get_ScalingRuleId2(self):
		return self.get_query_params().get('ScalingRuleId2')

	def set_ScalingRuleId2(self,ScalingRuleId2):
		self.add_query_param('ScalingRuleId2',ScalingRuleId2)

	def get_ScalingRuleId3(self):
		return self.get_query_params().get('ScalingRuleId3')

	def set_ScalingRuleId3(self,ScalingRuleId3):
		self.add_query_param('ScalingRuleId3',ScalingRuleId3)

	def get_ScalingRuleId4(self):
		return self.get_query_params().get('ScalingRuleId4')

	def set_ScalingRuleId4(self,ScalingRuleId4):
		self.add_query_param('ScalingRuleId4',ScalingRuleId4)

	def get_ScalingRuleId5(self):
		return self.get_query_params().get('ScalingRuleId5')

	def set_ScalingRuleId5(self,ScalingRuleId5):
		self.add_query_param('ScalingRuleId5',ScalingRuleId5)

	def get_ScalingRuleId6(self):
		return self.get_query_params().get('ScalingRuleId6')

	def set_ScalingRuleId6(self,ScalingRuleId6):
		self.add_query_param('ScalingRuleId6',ScalingRuleId6)

	def get_ScalingRuleId7(self):
		return self.get_query_params().get('ScalingRuleId7')

	def set_ScalingRuleId7(self,ScalingRuleId7):
		self.add_query_param('ScalingRuleId7',ScalingRuleId7)

	def get_ScalingRuleId8(self):
		return self.get_query_params().get('ScalingRuleId8')

	def set_ScalingRuleId8(self,ScalingRuleId8):
		self.add_query_param('ScalingRuleId8',ScalingRuleId8)

	def get_ScalingRuleId9(self):
		return self.get_query_params().get('ScalingRuleId9')

	def set_ScalingRuleId9(self,ScalingRuleId9):
		self.add_query_param('ScalingRuleId9',ScalingRuleId9)

	def get_ScalingRuleId10(self):
		return self.get_query_params().get('ScalingRuleId10')

	def set_ScalingRuleId10(self,ScalingRuleId10):
		self.add_query_param('ScalingRuleId10',ScalingRuleId10)

	def get_ScalingRuleName1(self):
		return self.get_query_params().get('ScalingRuleName1')

	def set_ScalingRuleName1(self,ScalingRuleName1):
		self.add_query_param('ScalingRuleName1',ScalingRuleName1)

	def get_ScalingRuleName2(self):
		return self.get_query_params().get('ScalingRuleName2')

	def set_ScalingRuleName2(self,ScalingRuleName2):
		self.add_query_param('ScalingRuleName2',ScalingRuleName2)

	def get_ScalingRuleName3(self):
		return self.get_query_params().get('ScalingRuleName3')

	def set_ScalingRuleName3(self,ScalingRuleName3):
		self.add_query_param('ScalingRuleName3',ScalingRuleName3)

	def get_ScalingRuleName4(self):
		return self.get_query_params().get('ScalingRuleName4')

	def set_ScalingRuleName4(self,ScalingRuleName4):
		self.add_query_param('ScalingRuleName4',ScalingRuleName4)

	def get_ScalingRuleName5(self):
		return self.get_query_params().get('ScalingRuleName5')

	def set_ScalingRuleName5(self,ScalingRuleName5):
		self.add_query_param('ScalingRuleName5',ScalingRuleName5)

	def get_ScalingRuleName6(self):
		return self.get_query_params().get('ScalingRuleName6')

	def set_ScalingRuleName6(self,ScalingRuleName6):
		self.add_query_param('ScalingRuleName6',ScalingRuleName6)

	def get_ScalingRuleName7(self):
		return self.get_query_params().get('ScalingRuleName7')

	def set_ScalingRuleName7(self,ScalingRuleName7):
		self.add_query_param('ScalingRuleName7',ScalingRuleName7)

	def get_ScalingRuleName8(self):
		return self.get_query_params().get('ScalingRuleName8')

	def set_ScalingRuleName8(self,ScalingRuleName8):
		self.add_query_param('ScalingRuleName8',ScalingRuleName8)

	def get_ScalingRuleName9(self):
		return self.get_query_params().get('ScalingRuleName9')

	def set_ScalingRuleName9(self,ScalingRuleName9):
		self.add_query_param('ScalingRuleName9',ScalingRuleName9)

	def get_ScalingRuleName10(self):
		return self.get_query_params().get('ScalingRuleName10')

	def set_ScalingRuleName10(self,ScalingRuleName10):
		self.add_query_param('ScalingRuleName10',ScalingRuleName10)

	def get_ScalingRuleAri1(self):
		return self.get_query_params().get('ScalingRuleAri1')

	def set_ScalingRuleAri1(self,ScalingRuleAri1):
		self.add_query_param('ScalingRuleAri1',ScalingRuleAri1)

	def get_ScalingRuleAri2(self):
		return self.get_query_params().get('ScalingRuleAri2')

	def set_ScalingRuleAri2(self,ScalingRuleAri2):
		self.add_query_param('ScalingRuleAri2',ScalingRuleAri2)

	def get_ScalingRuleAri3(self):
		return self.get_query_params().get('ScalingRuleAri3')

	def set_ScalingRuleAri3(self,ScalingRuleAri3):
		self.add_query_param('ScalingRuleAri3',ScalingRuleAri3)

	def get_ScalingRuleAri4(self):
		return self.get_query_params().get('ScalingRuleAri4')

	def set_ScalingRuleAri4(self,ScalingRuleAri4):
		self.add_query_param('ScalingRuleAri4',ScalingRuleAri4)

	def get_ScalingRuleAri5(self):
		return self.get_query_params().get('ScalingRuleAri5')

	def set_ScalingRuleAri5(self,ScalingRuleAri5):
		self.add_query_param('ScalingRuleAri5',ScalingRuleAri5)

	def get_ScalingRuleAri6(self):
		return self.get_query_params().get('ScalingRuleAri6')

	def set_ScalingRuleAri6(self,ScalingRuleAri6):
		self.add_query_param('ScalingRuleAri6',ScalingRuleAri6)

	def get_ScalingRuleAri7(self):
		return self.get_query_params().get('ScalingRuleAri7')

	def set_ScalingRuleAri7(self,ScalingRuleAri7):
		self.add_query_param('ScalingRuleAri7',ScalingRuleAri7)

	def get_ScalingRuleAri8(self):
		return self.get_query_params().get('ScalingRuleAri8')

	def set_ScalingRuleAri8(self,ScalingRuleAri8):
		self.add_query_param('ScalingRuleAri8',ScalingRuleAri8)

	def get_ScalingRuleAri9(self):
		return self.get_query_params().get('ScalingRuleAri9')

	def set_ScalingRuleAri9(self,ScalingRuleAri9):
		self.add_query_param('ScalingRuleAri9',ScalingRuleAri9)

	def get_ScalingRuleAri10(self):
		return self.get_query_params().get('ScalingRuleAri10')

	def set_ScalingRuleAri10(self,ScalingRuleAri10):
		self.add_query_param('ScalingRuleAri10',ScalingRuleAri10)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)