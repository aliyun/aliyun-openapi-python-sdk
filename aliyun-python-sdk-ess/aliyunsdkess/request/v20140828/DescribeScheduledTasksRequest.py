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
class DescribeScheduledTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScheduledTasks','ess')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ScheduledAction2(self):
		return self.get_query_params().get('ScheduledAction.2')

	def set_ScheduledAction2(self,ScheduledAction2):
		self.add_query_param('ScheduledAction.2',ScheduledAction2)

	def get_ScheduledAction1(self):
		return self.get_query_params().get('ScheduledAction.1')

	def set_ScheduledAction1(self,ScheduledAction1):
		self.add_query_param('ScheduledAction.1',ScheduledAction1)

	def get_ScheduledAction6(self):
		return self.get_query_params().get('ScheduledAction.6')

	def set_ScheduledAction6(self,ScheduledAction6):
		self.add_query_param('ScheduledAction.6',ScheduledAction6)

	def get_ScheduledAction5(self):
		return self.get_query_params().get('ScheduledAction.5')

	def set_ScheduledAction5(self,ScheduledAction5):
		self.add_query_param('ScheduledAction.5',ScheduledAction5)

	def get_ScheduledAction4(self):
		return self.get_query_params().get('ScheduledAction.4')

	def set_ScheduledAction4(self,ScheduledAction4):
		self.add_query_param('ScheduledAction.4',ScheduledAction4)

	def get_ScheduledAction3(self):
		return self.get_query_params().get('ScheduledAction.3')

	def set_ScheduledAction3(self,ScheduledAction3):
		self.add_query_param('ScheduledAction.3',ScheduledAction3)

	def get_ScheduledAction9(self):
		return self.get_query_params().get('ScheduledAction.9')

	def set_ScheduledAction9(self,ScheduledAction9):
		self.add_query_param('ScheduledAction.9',ScheduledAction9)

	def get_ScheduledAction8(self):
		return self.get_query_params().get('ScheduledAction.8')

	def set_ScheduledAction8(self,ScheduledAction8):
		self.add_query_param('ScheduledAction.8',ScheduledAction8)

	def get_ScheduledAction7(self):
		return self.get_query_params().get('ScheduledAction.7')

	def set_ScheduledAction7(self,ScheduledAction7):
		self.add_query_param('ScheduledAction.7',ScheduledAction7)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ScheduledTaskName20(self):
		return self.get_query_params().get('ScheduledTaskName.20')

	def set_ScheduledTaskName20(self,ScheduledTaskName20):
		self.add_query_param('ScheduledTaskName.20',ScheduledTaskName20)

	def get_ScheduledTaskName19(self):
		return self.get_query_params().get('ScheduledTaskName.19')

	def set_ScheduledTaskName19(self,ScheduledTaskName19):
		self.add_query_param('ScheduledTaskName.19',ScheduledTaskName19)

	def get_ScheduledTaskName18(self):
		return self.get_query_params().get('ScheduledTaskName.18')

	def set_ScheduledTaskName18(self,ScheduledTaskName18):
		self.add_query_param('ScheduledTaskName.18',ScheduledTaskName18)

	def get_ScheduledTaskId20(self):
		return self.get_query_params().get('ScheduledTaskId.20')

	def set_ScheduledTaskId20(self,ScheduledTaskId20):
		self.add_query_param('ScheduledTaskId.20',ScheduledTaskId20)

	def get_ScheduledTaskName13(self):
		return self.get_query_params().get('ScheduledTaskName.13')

	def set_ScheduledTaskName13(self,ScheduledTaskName13):
		self.add_query_param('ScheduledTaskName.13',ScheduledTaskName13)

	def get_ScheduledTaskName12(self):
		return self.get_query_params().get('ScheduledTaskName.12')

	def set_ScheduledTaskName12(self,ScheduledTaskName12):
		self.add_query_param('ScheduledTaskName.12',ScheduledTaskName12)

	def get_ScheduledTaskName11(self):
		return self.get_query_params().get('ScheduledTaskName.11')

	def set_ScheduledTaskName11(self,ScheduledTaskName11):
		self.add_query_param('ScheduledTaskName.11',ScheduledTaskName11)

	def get_ScheduledTaskName10(self):
		return self.get_query_params().get('ScheduledTaskName.10')

	def set_ScheduledTaskName10(self,ScheduledTaskName10):
		self.add_query_param('ScheduledTaskName.10',ScheduledTaskName10)

	def get_ScheduledTaskName17(self):
		return self.get_query_params().get('ScheduledTaskName.17')

	def set_ScheduledTaskName17(self,ScheduledTaskName17):
		self.add_query_param('ScheduledTaskName.17',ScheduledTaskName17)

	def get_ScheduledTaskName16(self):
		return self.get_query_params().get('ScheduledTaskName.16')

	def set_ScheduledTaskName16(self,ScheduledTaskName16):
		self.add_query_param('ScheduledTaskName.16',ScheduledTaskName16)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ScheduledTaskName15(self):
		return self.get_query_params().get('ScheduledTaskName.15')

	def set_ScheduledTaskName15(self,ScheduledTaskName15):
		self.add_query_param('ScheduledTaskName.15',ScheduledTaskName15)

	def get_ScheduledTaskName14(self):
		return self.get_query_params().get('ScheduledTaskName.14')

	def set_ScheduledTaskName14(self,ScheduledTaskName14):
		self.add_query_param('ScheduledTaskName.14',ScheduledTaskName14)

	def get_ScheduledTaskId2(self):
		return self.get_query_params().get('ScheduledTaskId.2')

	def set_ScheduledTaskId2(self,ScheduledTaskId2):
		self.add_query_param('ScheduledTaskId.2',ScheduledTaskId2)

	def get_ScheduledTaskId1(self):
		return self.get_query_params().get('ScheduledTaskId.1')

	def set_ScheduledTaskId1(self,ScheduledTaskId1):
		self.add_query_param('ScheduledTaskId.1',ScheduledTaskId1)

	def get_ScheduledTaskId4(self):
		return self.get_query_params().get('ScheduledTaskId.4')

	def set_ScheduledTaskId4(self,ScheduledTaskId4):
		self.add_query_param('ScheduledTaskId.4',ScheduledTaskId4)

	def get_ScheduledTaskId18(self):
		return self.get_query_params().get('ScheduledTaskId.18')

	def set_ScheduledTaskId18(self,ScheduledTaskId18):
		self.add_query_param('ScheduledTaskId.18',ScheduledTaskId18)

	def get_ScheduledTaskId3(self):
		return self.get_query_params().get('ScheduledTaskId.3')

	def set_ScheduledTaskId3(self,ScheduledTaskId3):
		self.add_query_param('ScheduledTaskId.3',ScheduledTaskId3)

	def get_ScheduledTaskId19(self):
		return self.get_query_params().get('ScheduledTaskId.19')

	def set_ScheduledTaskId19(self,ScheduledTaskId19):
		self.add_query_param('ScheduledTaskId.19',ScheduledTaskId19)

	def get_ScheduledTaskId6(self):
		return self.get_query_params().get('ScheduledTaskId.6')

	def set_ScheduledTaskId6(self,ScheduledTaskId6):
		self.add_query_param('ScheduledTaskId.6',ScheduledTaskId6)

	def get_ScheduledTaskId5(self):
		return self.get_query_params().get('ScheduledTaskId.5')

	def set_ScheduledTaskId5(self,ScheduledTaskId5):
		self.add_query_param('ScheduledTaskId.5',ScheduledTaskId5)

	def get_ScheduledTaskId8(self):
		return self.get_query_params().get('ScheduledTaskId.8')

	def set_ScheduledTaskId8(self,ScheduledTaskId8):
		self.add_query_param('ScheduledTaskId.8',ScheduledTaskId8)

	def get_ScheduledTaskName9(self):
		return self.get_query_params().get('ScheduledTaskName.9')

	def set_ScheduledTaskName9(self,ScheduledTaskName9):
		self.add_query_param('ScheduledTaskName.9',ScheduledTaskName9)

	def get_ScheduledAction20(self):
		return self.get_query_params().get('ScheduledAction.20')

	def set_ScheduledAction20(self,ScheduledAction20):
		self.add_query_param('ScheduledAction.20',ScheduledAction20)

	def get_ScheduledTaskId7(self):
		return self.get_query_params().get('ScheduledTaskId.7')

	def set_ScheduledTaskId7(self,ScheduledTaskId7):
		self.add_query_param('ScheduledTaskId.7',ScheduledTaskId7)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ScheduledTaskId12(self):
		return self.get_query_params().get('ScheduledTaskId.12')

	def set_ScheduledTaskId12(self,ScheduledTaskId12):
		self.add_query_param('ScheduledTaskId.12',ScheduledTaskId12)

	def get_ScheduledTaskName7(self):
		return self.get_query_params().get('ScheduledTaskName.7')

	def set_ScheduledTaskName7(self,ScheduledTaskName7):
		self.add_query_param('ScheduledTaskName.7',ScheduledTaskName7)

	def get_ScheduledTaskId9(self):
		return self.get_query_params().get('ScheduledTaskId.9')

	def set_ScheduledTaskId9(self,ScheduledTaskId9):
		self.add_query_param('ScheduledTaskId.9',ScheduledTaskId9)

	def get_ScheduledTaskId13(self):
		return self.get_query_params().get('ScheduledTaskId.13')

	def set_ScheduledTaskId13(self,ScheduledTaskId13):
		self.add_query_param('ScheduledTaskId.13',ScheduledTaskId13)

	def get_ScheduledTaskName8(self):
		return self.get_query_params().get('ScheduledTaskName.8')

	def set_ScheduledTaskName8(self,ScheduledTaskName8):
		self.add_query_param('ScheduledTaskName.8',ScheduledTaskName8)

	def get_ScheduledTaskId10(self):
		return self.get_query_params().get('ScheduledTaskId.10')

	def set_ScheduledTaskId10(self,ScheduledTaskId10):
		self.add_query_param('ScheduledTaskId.10',ScheduledTaskId10)

	def get_ScheduledTaskName5(self):
		return self.get_query_params().get('ScheduledTaskName.5')

	def set_ScheduledTaskName5(self,ScheduledTaskName5):
		self.add_query_param('ScheduledTaskName.5',ScheduledTaskName5)

	def get_ScheduledTaskId11(self):
		return self.get_query_params().get('ScheduledTaskId.11')

	def set_ScheduledTaskId11(self,ScheduledTaskId11):
		self.add_query_param('ScheduledTaskId.11',ScheduledTaskId11)

	def get_ScheduledTaskName6(self):
		return self.get_query_params().get('ScheduledTaskName.6')

	def set_ScheduledTaskName6(self,ScheduledTaskName6):
		self.add_query_param('ScheduledTaskName.6',ScheduledTaskName6)

	def get_ScheduledTaskId16(self):
		return self.get_query_params().get('ScheduledTaskId.16')

	def set_ScheduledTaskId16(self,ScheduledTaskId16):
		self.add_query_param('ScheduledTaskId.16',ScheduledTaskId16)

	def get_ScheduledTaskName3(self):
		return self.get_query_params().get('ScheduledTaskName.3')

	def set_ScheduledTaskName3(self,ScheduledTaskName3):
		self.add_query_param('ScheduledTaskName.3',ScheduledTaskName3)

	def get_ScheduledTaskId17(self):
		return self.get_query_params().get('ScheduledTaskId.17')

	def set_ScheduledTaskId17(self,ScheduledTaskId17):
		self.add_query_param('ScheduledTaskId.17',ScheduledTaskId17)

	def get_ScheduledTaskName4(self):
		return self.get_query_params().get('ScheduledTaskName.4')

	def set_ScheduledTaskName4(self,ScheduledTaskName4):
		self.add_query_param('ScheduledTaskName.4',ScheduledTaskName4)

	def get_ScheduledTaskId14(self):
		return self.get_query_params().get('ScheduledTaskId.14')

	def set_ScheduledTaskId14(self,ScheduledTaskId14):
		self.add_query_param('ScheduledTaskId.14',ScheduledTaskId14)

	def get_ScheduledTaskName1(self):
		return self.get_query_params().get('ScheduledTaskName.1')

	def set_ScheduledTaskName1(self,ScheduledTaskName1):
		self.add_query_param('ScheduledTaskName.1',ScheduledTaskName1)

	def get_ScheduledTaskId15(self):
		return self.get_query_params().get('ScheduledTaskId.15')

	def set_ScheduledTaskId15(self,ScheduledTaskId15):
		self.add_query_param('ScheduledTaskId.15',ScheduledTaskId15)

	def get_ScheduledTaskName2(self):
		return self.get_query_params().get('ScheduledTaskName.2')

	def set_ScheduledTaskName2(self,ScheduledTaskName2):
		self.add_query_param('ScheduledTaskName.2',ScheduledTaskName2)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_ScheduledAction18(self):
		return self.get_query_params().get('ScheduledAction.18')

	def set_ScheduledAction18(self,ScheduledAction18):
		self.add_query_param('ScheduledAction.18',ScheduledAction18)

	def get_ScheduledAction19(self):
		return self.get_query_params().get('ScheduledAction.19')

	def set_ScheduledAction19(self,ScheduledAction19):
		self.add_query_param('ScheduledAction.19',ScheduledAction19)

	def get_ScheduledAction16(self):
		return self.get_query_params().get('ScheduledAction.16')

	def set_ScheduledAction16(self,ScheduledAction16):
		self.add_query_param('ScheduledAction.16',ScheduledAction16)

	def get_ScheduledAction17(self):
		return self.get_query_params().get('ScheduledAction.17')

	def set_ScheduledAction17(self,ScheduledAction17):
		self.add_query_param('ScheduledAction.17',ScheduledAction17)

	def get_ScheduledAction14(self):
		return self.get_query_params().get('ScheduledAction.14')

	def set_ScheduledAction14(self,ScheduledAction14):
		self.add_query_param('ScheduledAction.14',ScheduledAction14)

	def get_ScheduledAction15(self):
		return self.get_query_params().get('ScheduledAction.15')

	def set_ScheduledAction15(self,ScheduledAction15):
		self.add_query_param('ScheduledAction.15',ScheduledAction15)

	def get_ScheduledAction12(self):
		return self.get_query_params().get('ScheduledAction.12')

	def set_ScheduledAction12(self,ScheduledAction12):
		self.add_query_param('ScheduledAction.12',ScheduledAction12)

	def get_ScheduledAction13(self):
		return self.get_query_params().get('ScheduledAction.13')

	def set_ScheduledAction13(self,ScheduledAction13):
		self.add_query_param('ScheduledAction.13',ScheduledAction13)

	def get_ScheduledAction10(self):
		return self.get_query_params().get('ScheduledAction.10')

	def set_ScheduledAction10(self,ScheduledAction10):
		self.add_query_param('ScheduledAction.10',ScheduledAction10)

	def get_ScheduledAction11(self):
		return self.get_query_params().get('ScheduledAction.11')

	def set_ScheduledAction11(self,ScheduledAction11):
		self.add_query_param('ScheduledAction.11',ScheduledAction11)