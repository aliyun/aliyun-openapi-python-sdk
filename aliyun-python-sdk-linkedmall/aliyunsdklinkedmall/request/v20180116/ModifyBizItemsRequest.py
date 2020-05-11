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

class ModifyBizItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'ModifyBizItems','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_ItemLists(self):
		return self.get_body_params().get('ItemLists')

	def set_ItemLists(self,ItemLists):
		for i in range(len(ItemLists)):	
			if ItemLists[i].get('ItemId') is not None:
				self.add_body_params('ItemList.' + str(i + 1) + '.ItemId' , ItemLists[i].get('ItemId'))
			if ItemLists[i].get('LmItemId') is not None:
				self.add_body_params('ItemList.' + str(i + 1) + '.LmItemId' , ItemLists[i].get('LmItemId'))
			for j in range(len(ItemLists[i].get('SkuLists'))):
				if ItemLists[i].get('SkuLists')[j] is not None:
					if ItemLists[i].get('SkuLists')[j].get('StatusAction') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.StatusAction', ItemLists[i].get('SkuLists')[j].get('StatusAction'))
					if ItemLists[i].get('SkuLists')[j].get('PriceCent') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.PriceCent', ItemLists[i].get('SkuLists')[j].get('PriceCent'))
					if ItemLists[i].get('SkuLists')[j].get('PointsAmount') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.PointsAmount', ItemLists[i].get('SkuLists')[j].get('PointsAmount'))
					if ItemLists[i].get('SkuLists')[j].get('Quantity') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.Quantity', ItemLists[i].get('SkuLists')[j].get('Quantity'))
					if ItemLists[i].get('SkuLists')[j].get('BenefitId') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.BenefitId', ItemLists[i].get('SkuLists')[j].get('BenefitId'))
					if ItemLists[i].get('SkuLists')[j].get('SkuId') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.SkuId', ItemLists[i].get('SkuLists')[j].get('SkuId'))
					if ItemLists[i].get('SkuLists')[j].get('Points') is not None:
						self.add_body_params('ItemList.' + str(i + 1) + '.SkuList.'+str(j + 1)+ '.Points', ItemLists[i].get('SkuLists')[j].get('Points'))


	def get_SubBizId(self):
		return self.get_query_params().get('SubBizId')

	def set_SubBizId(self,SubBizId):
		self.add_query_param('SubBizId',SubBizId)