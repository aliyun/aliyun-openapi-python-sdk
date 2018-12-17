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
class DescribeItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2018-08-01', 'DescribeItems')

	def get_ItemId(self):
		return self.get_query_params().get('ItemId')

	def set_ItemId(self,ItemId):
		self.add_query_param('ItemId',ItemId)

	def get_BePromotion(self):
		return self.get_query_params().get('BePromotion')

	def set_BePromotion(self,BePromotion):
		self.add_query_param('BePromotion',BePromotion)

	def get_ShelfCode(self):
		return self.get_query_params().get('ShelfCode')

	def set_ShelfCode(self,ShelfCode):
		self.add_query_param('ShelfCode',ShelfCode)

	def get_ItemTitle(self):
		return self.get_query_params().get('ItemTitle')

	def set_ItemTitle(self,ItemTitle):
		self.add_query_param('ItemTitle',ItemTitle)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_StoreId(self):
		return self.get_query_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_query_param('StoreId',StoreId)

	def get_SkuId(self):
		return self.get_query_params().get('SkuId')

	def set_SkuId(self,SkuId):
		self.add_query_param('SkuId',SkuId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ItemBarCode(self):
		return self.get_query_params().get('ItemBarCode')

	def set_ItemBarCode(self,ItemBarCode):
		self.add_query_param('ItemBarCode',ItemBarCode)