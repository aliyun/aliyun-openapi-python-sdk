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
from aliyunsdklinkedmall.endpoint import endpoint_data

class CreateOrderV2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'CreateOrderV2','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Quantity(self):
		return self.get_query_params().get('Quantity')

	def set_Quantity(self,Quantity):
		self.add_query_param('Quantity',Quantity)

	def get_BizUid(self):
		return self.get_query_params().get('BizUid')

	def set_BizUid(self,BizUid):
		self.add_query_param('BizUid',BizUid)

	def get_ExtJson(self):
		return self.get_query_params().get('ExtJson')

	def set_ExtJson(self,ExtJson):
		self.add_query_param('ExtJson',ExtJson)

	def get_AccountType(self):
		return self.get_query_params().get('AccountType')

	def set_AccountType(self,AccountType):
		self.add_query_param('AccountType',AccountType)

	def get_UseAnonymousTbAccount(self):
		return self.get_query_params().get('UseAnonymousTbAccount')

	def set_UseAnonymousTbAccount(self,UseAnonymousTbAccount):
		self.add_query_param('UseAnonymousTbAccount',UseAnonymousTbAccount)

	def get_OrderExpireTime(self):
		return self.get_query_params().get('OrderExpireTime')

	def set_OrderExpireTime(self,OrderExpireTime):
		self.add_query_param('OrderExpireTime',OrderExpireTime)

	def get_LmItemId(self):
		return self.get_query_params().get('LmItemId')

	def set_LmItemId(self,LmItemId):
		self.add_query_param('LmItemId',LmItemId)

	def get_ItemLists(self):
		return self.get_query_params().get('ItemLists')

	def set_ItemLists(self,ItemLists):
		for i in range(len(ItemLists)):	
			if ItemLists[i].get('ItemId') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.ItemId' , ItemLists[i].get('ItemId'))
			if ItemLists[i].get('Quantity') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.Quantity' , ItemLists[i].get('Quantity'))
			if ItemLists[i].get('LmItemId') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.LmItemId' , ItemLists[i].get('LmItemId'))
			if ItemLists[i].get('SkuId') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.SkuId' , ItemLists[i].get('SkuId'))


	def get_ItemId(self):
		return self.get_query_params().get('ItemId')

	def set_ItemId(self,ItemId):
		self.add_query_param('ItemId',ItemId)

	def get_TotalAmount(self):
		return self.get_query_params().get('TotalAmount')

	def set_TotalAmount(self,TotalAmount):
		self.add_query_param('TotalAmount',TotalAmount)

	def get_ThirdPartyUserId(self):
		return self.get_query_params().get('ThirdPartyUserId')

	def set_ThirdPartyUserId(self,ThirdPartyUserId):
		self.add_query_param('ThirdPartyUserId',ThirdPartyUserId)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_OutTradeId(self):
		return self.get_query_params().get('OutTradeId')

	def set_OutTradeId(self,OutTradeId):
		self.add_query_param('OutTradeId',OutTradeId)

	def get_DeliveryAddress(self):
		return self.get_query_params().get('DeliveryAddress')

	def set_DeliveryAddress(self,DeliveryAddress):
		self.add_query_param('DeliveryAddress',DeliveryAddress)