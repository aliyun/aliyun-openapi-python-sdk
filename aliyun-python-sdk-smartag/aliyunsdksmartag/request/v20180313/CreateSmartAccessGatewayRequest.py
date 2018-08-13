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
class CreateSmartAccessGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'CreateSmartAccessGateway','smartag')

	def get_MaxBandWidth(self):
		return self.get_query_params().get('MaxBandWidth')

	def set_MaxBandWidth(self,MaxBandWidth):
		self.add_query_param('MaxBandWidth',MaxBandWidth)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ReceiverTown(self):
		return self.get_query_params().get('ReceiverTown')

	def set_ReceiverTown(self,ReceiverTown):
		self.add_query_param('ReceiverTown',ReceiverTown)

	def get_ReceiverDistrict(self):
		return self.get_query_params().get('ReceiverDistrict')

	def set_ReceiverDistrict(self,ReceiverDistrict):
		self.add_query_param('ReceiverDistrict',ReceiverDistrict)

	def get_ReceiverAddress(self):
		return self.get_query_params().get('ReceiverAddress')

	def set_ReceiverAddress(self,ReceiverAddress):
		self.add_query_param('ReceiverAddress',ReceiverAddress)

	def get_BuyerMessage(self):
		return self.get_query_params().get('BuyerMessage')

	def set_BuyerMessage(self,BuyerMessage):
		self.add_query_param('BuyerMessage',BuyerMessage)

	def get_HardWareSpec(self):
		return self.get_query_params().get('HardWareSpec')

	def set_HardWareSpec(self,HardWareSpec):
		self.add_query_param('HardWareSpec',HardWareSpec)

	def get_ReceiverEmail(self):
		return self.get_query_params().get('ReceiverEmail')

	def set_ReceiverEmail(self,ReceiverEmail):
		self.add_query_param('ReceiverEmail',ReceiverEmail)

	def get_ReceiverState(self):
		return self.get_query_params().get('ReceiverState')

	def set_ReceiverState(self,ReceiverState):
		self.add_query_param('ReceiverState',ReceiverState)

	def get_ReceiverCity(self):
		return self.get_query_params().get('ReceiverCity')

	def set_ReceiverCity(self,ReceiverCity):
		self.add_query_param('ReceiverCity',ReceiverCity)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_ReceiverMobile(self):
		return self.get_query_params().get('ReceiverMobile')

	def set_ReceiverMobile(self,ReceiverMobile):
		self.add_query_param('ReceiverMobile',ReceiverMobile)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ReceiverPhone(self):
		return self.get_query_params().get('ReceiverPhone')

	def set_ReceiverPhone(self,ReceiverPhone):
		self.add_query_param('ReceiverPhone',ReceiverPhone)

	def get_ReceiverName(self):
		return self.get_query_params().get('ReceiverName')

	def set_ReceiverName(self,ReceiverName):
		self.add_query_param('ReceiverName',ReceiverName)

	def get_HaType(self):
		return self.get_query_params().get('HaType')

	def set_HaType(self,HaType):
		self.add_query_param('HaType',HaType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ReceiverCountry(self):
		return self.get_query_params().get('ReceiverCountry')

	def set_ReceiverCountry(self,ReceiverCountry):
		self.add_query_param('ReceiverCountry',ReceiverCountry)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_ReceiverZip(self):
		return self.get_query_params().get('ReceiverZip')

	def set_ReceiverZip(self,ReceiverZip):
		self.add_query_param('ReceiverZip',ReceiverZip)