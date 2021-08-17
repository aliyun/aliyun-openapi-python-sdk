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

class CreateOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateOrder')
		self.set_method('POST')

	def get_SrcType(self):
		return self.get_query_params().get('SrcType')

	def set_SrcType(self,SrcType):
		self.add_query_param('SrcType',SrcType)

	def get_AvailableSwitchPortNum(self):
		return self.get_query_params().get('AvailableSwitchPortNum')

	def set_AvailableSwitchPortNum(self,AvailableSwitchPortNum):
		self.add_query_param('AvailableSwitchPortNum',AvailableSwitchPortNum)

	def get_PhoneNumber(self):
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self,PhoneNumber):
		self.add_query_param('PhoneNumber',PhoneNumber)

	def get_ToRegion(self):
		return self.get_query_params().get('ToRegion')

	def set_ToRegion(self,ToRegion):
		self.add_query_param('ToRegion',ToRegion)

	def get_AverageFileSize(self):
		return self.get_query_params().get('AverageFileSize')

	def set_AverageFileSize(self,AverageFileSize):
		self.add_query_param('AverageFileSize',AverageFileSize)

	def get_ContactName(self):
		return self.get_query_params().get('ContactName')

	def set_ContactName(self,ContactName):
		self.add_query_param('ContactName',ContactName)

	def get_HasComputingNode(self):
		return self.get_query_params().get('HasComputingNode')

	def set_HasComputingNode(self,HasComputingNode):
		self.add_query_param('HasComputingNode',HasComputingNode)

	def get_MigSize(self):
		return self.get_query_params().get('MigSize')

	def set_MigSize(self,MigSize):
		self.add_query_param('MigSize',MigSize)

	def get_HasElectricalPort(self):
		return self.get_query_params().get('HasElectricalPort')

	def set_HasElectricalPort(self,HasElectricalPort):
		self.add_query_param('HasElectricalPort',HasElectricalPort)

	def get_Has3U(self):
		return self.get_query_params().get('Has3U')

	def set_Has3U(self,Has3U):
		self.add_query_param('Has3U',Has3U)

	def get_HasGigabitSwitch(self):
		return self.get_query_params().get('HasGigabitSwitch')

	def set_HasGigabitSwitch(self,HasGigabitSwitch):
		self.add_query_param('HasGigabitSwitch',HasGigabitSwitch)

	def get_HasBrowser(self):
		return self.get_query_params().get('HasBrowser')

	def set_HasBrowser(self,HasBrowser):
		self.add_query_param('HasBrowser',HasBrowser)

	def get_HasTenGigabitSwitch(self):
		return self.get_query_params().get('HasTenGigabitSwitch')

	def set_HasTenGigabitSwitch(self,HasTenGigabitSwitch):
		self.add_query_param('HasTenGigabitSwitch',HasTenGigabitSwitch)

	def get_destType(self):
		return self.get_query_params().get('destType')

	def set_destType(self,destType):
		self.add_query_param('destType',destType)

	def get_TotalFileCount(self):
		return self.get_query_params().get('TotalFileCount')

	def set_TotalFileCount(self,TotalFileCount):
		self.add_query_param('TotalFileCount',TotalFileCount)

	def get_HasFibreOpticalPort(self):
		return self.get_query_params().get('HasFibreOpticalPort')

	def set_HasFibreOpticalPort(self,HasFibreOpticalPort):
		self.add_query_param('HasFibreOpticalPort',HasFibreOpticalPort)