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
from aliyunsdkmarket.endpoint import endpoint_data

class CreateOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Market', '2015-11-01', 'CreateOrder','yunmarket')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OrderSouce(self):
		return self.get_query_params().get('OrderSouce')

	def set_OrderSouce(self,OrderSouce):
		self.add_query_param('OrderSouce',OrderSouce)

	def get_Commodity(self):
		return self.get_query_params().get('Commodity')

	def set_Commodity(self,Commodity):
		self.add_query_param('Commodity',Commodity)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PaymentType(self):
		return self.get_query_params().get('PaymentType')

	def set_PaymentType(self,PaymentType):
		self.add_query_param('PaymentType',PaymentType)

	def get_OrderType(self):
		return self.get_query_params().get('OrderType')

	def set_OrderType(self,OrderType):
		self.add_query_param('OrderType',OrderType)