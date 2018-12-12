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
class UnicomOrderConfirmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'UnicomOrderConfirm','smartag')

	def get_TmsCode(self):
		return self.get_query_params().get('TmsCode')

	def set_TmsCode(self,TmsCode):
		self.add_query_param('TmsCode',TmsCode)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OrderItems(self):
		return self.get_query_params().get('OrderItems')

	def set_OrderItems(self,OrderItems):
		for i in range(len(OrderItems)):	
			if OrderItems[i].get('ScItemName') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.ScItemName' , OrderItems[i].get('ScItemName'))
			if OrderItems[i].get('ItemAmount') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.ItemAmount' , OrderItems[i].get('ItemAmount'))
			for j in range(len(OrderItems[i].get('SnLists'))):
				if OrderItems[i].get('SnLists')[j] is not None:
					self.add_query_param('OrderItem.' + str(i + 1) + '.SnList.'+str(j + 1), OrderItems[i].get('SnLists')[j])
			if OrderItems[i].get('OrderItemId') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.OrderItemId' , OrderItems[i].get('OrderItemId'))
			if OrderItems[i].get('ScItemCode') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.ScItemCode' , OrderItems[i].get('ScItemCode'))
			if OrderItems[i].get('ItemQuantity') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.ItemQuantity' , OrderItems[i].get('ItemQuantity'))
			if OrderItems[i].get('TradeId') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.TradeId' , OrderItems[i].get('TradeId'))
			if OrderItems[i].get('TradeItemId') is not None:
				self.add_query_param('OrderItem.' + str(i + 1) + '.TradeItemId' , OrderItems[i].get('TradeItemId'))


	def get_OwnerUserId(self):
		return self.get_query_params().get('OwnerUserId')

	def set_OwnerUserId(self,OwnerUserId):
		self.add_query_param('OwnerUserId',OwnerUserId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OrderPostFee(self):
		return self.get_query_params().get('OrderPostFee')

	def set_OrderPostFee(self,OrderPostFee):
		self.add_query_param('OrderPostFee',OrderPostFee)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TmsOrderCode(self):
		return self.get_query_params().get('TmsOrderCode')

	def set_TmsOrderCode(self,TmsOrderCode):
		self.add_query_param('TmsOrderCode',TmsOrderCode)

	def get_TradeId(self):
		return self.get_query_params().get('TradeId')

	def set_TradeId(self,TradeId):
		self.add_query_param('TradeId',TradeId)