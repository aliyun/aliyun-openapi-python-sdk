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

class QueryItemInventoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'QueryItemInventory','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DivisionCode(self):
		return self.get_query_params().get('DivisionCode')

	def set_DivisionCode(self,DivisionCode):
		self.add_query_param('DivisionCode',DivisionCode)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_ItemLists(self):
		return self.get_query_params().get('ItemLists')

	def set_ItemLists(self,ItemLists):
		for i in range(len(ItemLists)):	
			if ItemLists[i].get('ItemId') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.ItemId' , ItemLists[i].get('ItemId'))
			for j in range(len(ItemLists[i].get('SkuIdLists'))):
				if ItemLists[i].get('SkuIdLists')[j] is not None:
					self.add_query_param('ItemList.' + str(i + 1) + '.SkuIdList.'+str(j + 1), ItemLists[i].get('SkuIdLists')[j])
			if ItemLists[i].get('LmItemId') is not None:
				self.add_query_param('ItemList.' + str(i + 1) + '.LmItemId' , ItemLists[i].get('LmItemId'))
