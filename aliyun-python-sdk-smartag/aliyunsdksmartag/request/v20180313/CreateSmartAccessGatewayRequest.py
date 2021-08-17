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
from aliyunsdksmartag.endpoint import endpoint_data

class CreateSmartAccessGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'CreateSmartAccessGateway','smartag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ReceiverTown(self): # String
		return self.get_query_params().get('ReceiverTown')

	def set_ReceiverTown(self, ReceiverTown):  # String
		self.add_query_param('ReceiverTown', ReceiverTown)
	def get_ReceiverDistrict(self): # String
		return self.get_query_params().get('ReceiverDistrict')

	def set_ReceiverDistrict(self, ReceiverDistrict):  # String
		self.add_query_param('ReceiverDistrict', ReceiverDistrict)
	def get_BuyerMessage(self): # String
		return self.get_query_params().get('BuyerMessage')

	def set_BuyerMessage(self, BuyerMessage):  # String
		self.add_query_param('BuyerMessage', BuyerMessage)
	def get_ReceiverState(self): # String
		return self.get_query_params().get('ReceiverState')

	def set_ReceiverState(self, ReceiverState):  # String
		self.add_query_param('ReceiverState', ReceiverState)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ReceiverPhone(self): # String
		return self.get_query_params().get('ReceiverPhone')

	def set_ReceiverPhone(self, ReceiverPhone):  # String
		self.add_query_param('ReceiverPhone', ReceiverPhone)
	def get_HaType(self): # String
		return self.get_query_params().get('HaType')

	def set_HaType(self, HaType):  # String
		self.add_query_param('HaType', HaType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ReceiverCountry(self): # String
		return self.get_query_params().get('ReceiverCountry')

	def set_ReceiverCountry(self, ReceiverCountry):  # String
		self.add_query_param('ReceiverCountry', ReceiverCountry)
	def get_MaxBandWidth(self): # Integer
		return self.get_query_params().get('MaxBandWidth')

	def set_MaxBandWidth(self, MaxBandWidth):  # Integer
		self.add_query_param('MaxBandWidth', MaxBandWidth)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_ReceiverAddress(self): # String
		return self.get_query_params().get('ReceiverAddress')

	def set_ReceiverAddress(self, ReceiverAddress):  # String
		self.add_query_param('ReceiverAddress', ReceiverAddress)
	def get_HardWareSpec(self): # String
		return self.get_query_params().get('HardWareSpec')

	def set_HardWareSpec(self, HardWareSpec):  # String
		self.add_query_param('HardWareSpec', HardWareSpec)
	def get_ReceiverEmail(self): # String
		return self.get_query_params().get('ReceiverEmail')

	def set_ReceiverEmail(self, ReceiverEmail):  # String
		self.add_query_param('ReceiverEmail', ReceiverEmail)
	def get_ReceiverCity(self): # String
		return self.get_query_params().get('ReceiverCity')

	def set_ReceiverCity(self, ReceiverCity):  # String
		self.add_query_param('ReceiverCity', ReceiverCity)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_CPEVersion(self): # String
		return self.get_query_params().get('CPEVersion')

	def set_CPEVersion(self, CPEVersion):  # String
		self.add_query_param('CPEVersion', CPEVersion)
	def get_ReceiverMobile(self): # String
		return self.get_query_params().get('ReceiverMobile')

	def set_ReceiverMobile(self, ReceiverMobile):  # String
		self.add_query_param('ReceiverMobile', ReceiverMobile)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_ReceiverName(self): # String
		return self.get_query_params().get('ReceiverName')

	def set_ReceiverName(self, ReceiverName):  # String
		self.add_query_param('ReceiverName', ReceiverName)
	def get_AlreadyHaveSag(self): # Boolean
		return self.get_query_params().get('AlreadyHaveSag')

	def set_AlreadyHaveSag(self, AlreadyHaveSag):  # Boolean
		self.add_query_param('AlreadyHaveSag', AlreadyHaveSag)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_ReceiverZip(self): # String
		return self.get_query_params().get('ReceiverZip')

	def set_ReceiverZip(self, ReceiverZip):  # String
		self.add_query_param('ReceiverZip', ReceiverZip)
