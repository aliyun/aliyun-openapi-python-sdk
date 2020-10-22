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

class UnicomOrderConfirmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'UnicomOrderConfirm','smartag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TmsCode(self):
		return self.get_query_params().get('TmsCode')

	def set_TmsCode(self,TmsCode):
		self.add_query_param('TmsCode',TmsCode)

	def get_OrderItems(self):
		return self.get_query_params().get('OrderItem')

	def set_OrderItems(self, OrderItems):
		for depth1 in range(len(OrderItems)):
			if OrderItems[depth1].get('ScItemName') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.ScItemName', OrderItems[depth1].get('ScItemName'))
			if OrderItems[depth1].get('ItemAmount') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.ItemAmount', OrderItems[depth1].get('ItemAmount'))
			if OrderItems[depth1].get('SnList') is not None:
				for depth2 in range(len(OrderItems[depth1].get('SnList'))):
					if OrderItems[depth1].get('SnList')[depth2] is not None:
						self.add_query_param('OrderItem.' + str(depth1 + 1) + '.SnList.' + str(depth2 + 1) , OrderItems[depth1].get('SnList')[depth2])
			if OrderItems[depth1].get('OrderItemId') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.OrderItemId', OrderItems[depth1].get('OrderItemId'))
			if OrderItems[depth1].get('ScItemCode') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.ScItemCode', OrderItems[depth1].get('ScItemCode'))
			if OrderItems[depth1].get('ItemQuantity') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.ItemQuantity', OrderItems[depth1].get('ItemQuantity'))
			if OrderItems[depth1].get('TradeId') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.TradeId', OrderItems[depth1].get('TradeId'))
			if OrderItems[depth1].get('TradeItemId') is not None:
				self.add_query_param('OrderItem.' + str(depth1 + 1) + '.TradeItemId', OrderItems[depth1].get('TradeItemId'))

	def get_OrderPostFee(self):
		return self.get_query_params().get('OrderPostFee')

	def set_OrderPostFee(self,OrderPostFee):
		self.add_query_param('OrderPostFee',OrderPostFee)

	def get_TradeId(self):
		return self.get_query_params().get('TradeId')

	def set_TradeId(self,TradeId):
		self.add_query_param('TradeId',TradeId)

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

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TmsOrderCode(self):
		return self.get_query_params().get('TmsOrderCode')

	def set_TmsOrderCode(self,TmsOrderCode):
		self.add_query_param('TmsOrderCode',TmsOrderCode)