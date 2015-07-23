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
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'DescribeScheduledTasks')

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

	def get_ScheduledAction1(self):
		return self.get_query_params().get('ScheduledAction1')

	def set_ScheduledAction1(self,ScheduledAction1):
		self.add_query_param('ScheduledAction1',ScheduledAction1)

	def get_ScheduledAction2(self):
		return self.get_query_params().get('ScheduledAction2')

	def set_ScheduledAction2(self,ScheduledAction2):
		self.add_query_param('ScheduledAction2',ScheduledAction2)

	def get_ScheduledAction3(self):
		return self.get_query_params().get('ScheduledAction3')

	def set_ScheduledAction3(self,ScheduledAction3):
		self.add_query_param('ScheduledAction3',ScheduledAction3)

	def get_ScheduledAction4(self):
		return self.get_query_params().get('ScheduledAction4')

	def set_ScheduledAction4(self,ScheduledAction4):
		self.add_query_param('ScheduledAction4',ScheduledAction4)

	def get_ScheduledAction5(self):
		return self.get_query_params().get('ScheduledAction5')

	def set_ScheduledAction5(self,ScheduledAction5):
		self.add_query_param('ScheduledAction5',ScheduledAction5)

	def get_ScheduledAction6(self):
		return self.get_query_params().get('ScheduledAction6')

	def set_ScheduledAction6(self,ScheduledAction6):
		self.add_query_param('ScheduledAction6',ScheduledAction6)

	def get_ScheduledAction7(self):
		return self.get_query_params().get('ScheduledAction7')

	def set_ScheduledAction7(self,ScheduledAction7):
		self.add_query_param('ScheduledAction7',ScheduledAction7)

	def get_ScheduledAction8(self):
		return self.get_query_params().get('ScheduledAction8')

	def set_ScheduledAction8(self,ScheduledAction8):
		self.add_query_param('ScheduledAction8',ScheduledAction8)

	def get_ScheduledAction9(self):
		return self.get_query_params().get('ScheduledAction9')

	def set_ScheduledAction9(self,ScheduledAction9):
		self.add_query_param('ScheduledAction9',ScheduledAction9)

	def get_ScheduledAction10(self):
		return self.get_query_params().get('ScheduledAction10')

	def set_ScheduledAction10(self,ScheduledAction10):
		self.add_query_param('ScheduledAction10',ScheduledAction10)

	def get_ScheduledAction11(self):
		return self.get_query_params().get('ScheduledAction11')

	def set_ScheduledAction11(self,ScheduledAction11):
		self.add_query_param('ScheduledAction11',ScheduledAction11)

	def get_ScheduledAction12(self):
		return self.get_query_params().get('ScheduledAction12')

	def set_ScheduledAction12(self,ScheduledAction12):
		self.add_query_param('ScheduledAction12',ScheduledAction12)

	def get_ScheduledAction13(self):
		return self.get_query_params().get('ScheduledAction13')

	def set_ScheduledAction13(self,ScheduledAction13):
		self.add_query_param('ScheduledAction13',ScheduledAction13)

	def get_ScheduledAction14(self):
		return self.get_query_params().get('ScheduledAction14')

	def set_ScheduledAction14(self,ScheduledAction14):
		self.add_query_param('ScheduledAction14',ScheduledAction14)

	def get_ScheduledAction15(self):
		return self.get_query_params().get('ScheduledAction15')

	def set_ScheduledAction15(self,ScheduledAction15):
		self.add_query_param('ScheduledAction15',ScheduledAction15)

	def get_ScheduledAction16(self):
		return self.get_query_params().get('ScheduledAction16')

	def set_ScheduledAction16(self,ScheduledAction16):
		self.add_query_param('ScheduledAction16',ScheduledAction16)

	def get_ScheduledAction17(self):
		return self.get_query_params().get('ScheduledAction17')

	def set_ScheduledAction17(self,ScheduledAction17):
		self.add_query_param('ScheduledAction17',ScheduledAction17)

	def get_ScheduledAction18(self):
		return self.get_query_params().get('ScheduledAction18')

	def set_ScheduledAction18(self,ScheduledAction18):
		self.add_query_param('ScheduledAction18',ScheduledAction18)

	def get_ScheduledAction19(self):
		return self.get_query_params().get('ScheduledAction19')

	def set_ScheduledAction19(self,ScheduledAction19):
		self.add_query_param('ScheduledAction19',ScheduledAction19)

	def get_ScheduledAction20(self):
		return self.get_query_params().get('ScheduledAction20')

	def set_ScheduledAction20(self,ScheduledAction20):
		self.add_query_param('ScheduledAction20',ScheduledAction20)

	def get_ScheduledTaskId1(self):
		return self.get_query_params().get('ScheduledTaskId1')

	def set_ScheduledTaskId1(self,ScheduledTaskId1):
		self.add_query_param('ScheduledTaskId1',ScheduledTaskId1)

	def get_ScheduledTaskId2(self):
		return self.get_query_params().get('ScheduledTaskId2')

	def set_ScheduledTaskId2(self,ScheduledTaskId2):
		self.add_query_param('ScheduledTaskId2',ScheduledTaskId2)

	def get_ScheduledTaskId3(self):
		return self.get_query_params().get('ScheduledTaskId3')

	def set_ScheduledTaskId3(self,ScheduledTaskId3):
		self.add_query_param('ScheduledTaskId3',ScheduledTaskId3)

	def get_ScheduledTaskId4(self):
		return self.get_query_params().get('ScheduledTaskId4')

	def set_ScheduledTaskId4(self,ScheduledTaskId4):
		self.add_query_param('ScheduledTaskId4',ScheduledTaskId4)

	def get_ScheduledTaskId5(self):
		return self.get_query_params().get('ScheduledTaskId5')

	def set_ScheduledTaskId5(self,ScheduledTaskId5):
		self.add_query_param('ScheduledTaskId5',ScheduledTaskId5)

	def get_ScheduledTaskId6(self):
		return self.get_query_params().get('ScheduledTaskId6')

	def set_ScheduledTaskId6(self,ScheduledTaskId6):
		self.add_query_param('ScheduledTaskId6',ScheduledTaskId6)

	def get_ScheduledTaskId7(self):
		return self.get_query_params().get('ScheduledTaskId7')

	def set_ScheduledTaskId7(self,ScheduledTaskId7):
		self.add_query_param('ScheduledTaskId7',ScheduledTaskId7)

	def get_ScheduledTaskId8(self):
		return self.get_query_params().get('ScheduledTaskId8')

	def set_ScheduledTaskId8(self,ScheduledTaskId8):
		self.add_query_param('ScheduledTaskId8',ScheduledTaskId8)

	def get_ScheduledTaskId9(self):
		return self.get_query_params().get('ScheduledTaskId9')

	def set_ScheduledTaskId9(self,ScheduledTaskId9):
		self.add_query_param('ScheduledTaskId9',ScheduledTaskId9)

	def get_ScheduledTaskId10(self):
		return self.get_query_params().get('ScheduledTaskId10')

	def set_ScheduledTaskId10(self,ScheduledTaskId10):
		self.add_query_param('ScheduledTaskId10',ScheduledTaskId10)

	def get_ScheduledTaskId11(self):
		return self.get_query_params().get('ScheduledTaskId11')

	def set_ScheduledTaskId11(self,ScheduledTaskId11):
		self.add_query_param('ScheduledTaskId11',ScheduledTaskId11)

	def get_ScheduledTaskId12(self):
		return self.get_query_params().get('ScheduledTaskId12')

	def set_ScheduledTaskId12(self,ScheduledTaskId12):
		self.add_query_param('ScheduledTaskId12',ScheduledTaskId12)

	def get_ScheduledTaskId13(self):
		return self.get_query_params().get('ScheduledTaskId13')

	def set_ScheduledTaskId13(self,ScheduledTaskId13):
		self.add_query_param('ScheduledTaskId13',ScheduledTaskId13)

	def get_ScheduledTaskId14(self):
		return self.get_query_params().get('ScheduledTaskId14')

	def set_ScheduledTaskId14(self,ScheduledTaskId14):
		self.add_query_param('ScheduledTaskId14',ScheduledTaskId14)

	def get_ScheduledTaskId15(self):
		return self.get_query_params().get('ScheduledTaskId15')

	def set_ScheduledTaskId15(self,ScheduledTaskId15):
		self.add_query_param('ScheduledTaskId15',ScheduledTaskId15)

	def get_ScheduledTaskId16(self):
		return self.get_query_params().get('ScheduledTaskId16')

	def set_ScheduledTaskId16(self,ScheduledTaskId16):
		self.add_query_param('ScheduledTaskId16',ScheduledTaskId16)

	def get_ScheduledTaskId17(self):
		return self.get_query_params().get('ScheduledTaskId17')

	def set_ScheduledTaskId17(self,ScheduledTaskId17):
		self.add_query_param('ScheduledTaskId17',ScheduledTaskId17)

	def get_ScheduledTaskId18(self):
		return self.get_query_params().get('ScheduledTaskId18')

	def set_ScheduledTaskId18(self,ScheduledTaskId18):
		self.add_query_param('ScheduledTaskId18',ScheduledTaskId18)

	def get_ScheduledTaskId19(self):
		return self.get_query_params().get('ScheduledTaskId19')

	def set_ScheduledTaskId19(self,ScheduledTaskId19):
		self.add_query_param('ScheduledTaskId19',ScheduledTaskId19)

	def get_ScheduledTaskId20(self):
		return self.get_query_params().get('ScheduledTaskId20')

	def set_ScheduledTaskId20(self,ScheduledTaskId20):
		self.add_query_param('ScheduledTaskId20',ScheduledTaskId20)

	def get_ScheduledTaskName1(self):
		return self.get_query_params().get('ScheduledTaskName1')

	def set_ScheduledTaskName1(self,ScheduledTaskName1):
		self.add_query_param('ScheduledTaskName1',ScheduledTaskName1)

	def get_ScheduledTaskName2(self):
		return self.get_query_params().get('ScheduledTaskName2')

	def set_ScheduledTaskName2(self,ScheduledTaskName2):
		self.add_query_param('ScheduledTaskName2',ScheduledTaskName2)

	def get_ScheduledTaskName3(self):
		return self.get_query_params().get('ScheduledTaskName3')

	def set_ScheduledTaskName3(self,ScheduledTaskName3):
		self.add_query_param('ScheduledTaskName3',ScheduledTaskName3)

	def get_ScheduledTaskName4(self):
		return self.get_query_params().get('ScheduledTaskName4')

	def set_ScheduledTaskName4(self,ScheduledTaskName4):
		self.add_query_param('ScheduledTaskName4',ScheduledTaskName4)

	def get_ScheduledTaskName5(self):
		return self.get_query_params().get('ScheduledTaskName5')

	def set_ScheduledTaskName5(self,ScheduledTaskName5):
		self.add_query_param('ScheduledTaskName5',ScheduledTaskName5)

	def get_ScheduledTaskName6(self):
		return self.get_query_params().get('ScheduledTaskName6')

	def set_ScheduledTaskName6(self,ScheduledTaskName6):
		self.add_query_param('ScheduledTaskName6',ScheduledTaskName6)

	def get_ScheduledTaskName7(self):
		return self.get_query_params().get('ScheduledTaskName7')

	def set_ScheduledTaskName7(self,ScheduledTaskName7):
		self.add_query_param('ScheduledTaskName7',ScheduledTaskName7)

	def get_ScheduledTaskName8(self):
		return self.get_query_params().get('ScheduledTaskName8')

	def set_ScheduledTaskName8(self,ScheduledTaskName8):
		self.add_query_param('ScheduledTaskName8',ScheduledTaskName8)

	def get_ScheduledTaskName9(self):
		return self.get_query_params().get('ScheduledTaskName9')

	def set_ScheduledTaskName9(self,ScheduledTaskName9):
		self.add_query_param('ScheduledTaskName9',ScheduledTaskName9)

	def get_ScheduledTaskName10(self):
		return self.get_query_params().get('ScheduledTaskName10')

	def set_ScheduledTaskName10(self,ScheduledTaskName10):
		self.add_query_param('ScheduledTaskName10',ScheduledTaskName10)

	def get_ScheduledTaskName11(self):
		return self.get_query_params().get('ScheduledTaskName11')

	def set_ScheduledTaskName11(self,ScheduledTaskName11):
		self.add_query_param('ScheduledTaskName11',ScheduledTaskName11)

	def get_ScheduledTaskName12(self):
		return self.get_query_params().get('ScheduledTaskName12')

	def set_ScheduledTaskName12(self,ScheduledTaskName12):
		self.add_query_param('ScheduledTaskName12',ScheduledTaskName12)

	def get_ScheduledTaskName13(self):
		return self.get_query_params().get('ScheduledTaskName13')

	def set_ScheduledTaskName13(self,ScheduledTaskName13):
		self.add_query_param('ScheduledTaskName13',ScheduledTaskName13)

	def get_ScheduledTaskName14(self):
		return self.get_query_params().get('ScheduledTaskName14')

	def set_ScheduledTaskName14(self,ScheduledTaskName14):
		self.add_query_param('ScheduledTaskName14',ScheduledTaskName14)

	def get_ScheduledTaskName15(self):
		return self.get_query_params().get('ScheduledTaskName15')

	def set_ScheduledTaskName15(self,ScheduledTaskName15):
		self.add_query_param('ScheduledTaskName15',ScheduledTaskName15)

	def get_ScheduledTaskName16(self):
		return self.get_query_params().get('ScheduledTaskName16')

	def set_ScheduledTaskName16(self,ScheduledTaskName16):
		self.add_query_param('ScheduledTaskName16',ScheduledTaskName16)

	def get_ScheduledTaskName17(self):
		return self.get_query_params().get('ScheduledTaskName17')

	def set_ScheduledTaskName17(self,ScheduledTaskName17):
		self.add_query_param('ScheduledTaskName17',ScheduledTaskName17)

	def get_ScheduledTaskName18(self):
		return self.get_query_params().get('ScheduledTaskName18')

	def set_ScheduledTaskName18(self,ScheduledTaskName18):
		self.add_query_param('ScheduledTaskName18',ScheduledTaskName18)

	def get_ScheduledTaskName19(self):
		return self.get_query_params().get('ScheduledTaskName19')

	def set_ScheduledTaskName19(self,ScheduledTaskName19):
		self.add_query_param('ScheduledTaskName19',ScheduledTaskName19)

	def get_ScheduledTaskName20(self):
		return self.get_query_params().get('ScheduledTaskName20')

	def set_ScheduledTaskName20(self,ScheduledTaskName20):
		self.add_query_param('ScheduledTaskName20',ScheduledTaskName20)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)