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
from aliyunsdkcloudesl.endpoint import endpoint_data

class BatchInsertItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2020-02-01', 'BatchInsertItems','cloudesl')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_ItemInfos(self):
		return self.get_body_params().get('ItemInfos')

	def set_ItemInfos(self, ItemInfos):
		for depth1 in range(len(ItemInfos)):
			if ItemInfos[depth1].get('MemberPrice') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.MemberPrice', ItemInfos[depth1].get('MemberPrice'))
			if ItemInfos[depth1].get('ActionPrice') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ActionPrice', ItemInfos[depth1].get('ActionPrice'))
			if ItemInfos[depth1].get('BeSourceCode') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.BeSourceCode', ItemInfos[depth1].get('BeSourceCode'))
			if ItemInfos[depth1].get('BrandName') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.BrandName', ItemInfos[depth1].get('BrandName'))
			if ItemInfos[depth1].get('PromotionStart') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.PromotionStart', ItemInfos[depth1].get('PromotionStart'))
			if ItemInfos[depth1].get('PriceUnit') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.PriceUnit', ItemInfos[depth1].get('PriceUnit'))
			if ItemInfos[depth1].get('Rank') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.Rank', ItemInfos[depth1].get('Rank'))
			if ItemInfos[depth1].get('ItemInfoIndex') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemInfoIndex', ItemInfos[depth1].get('ItemInfoIndex'))
			if ItemInfos[depth1].get('ItemBarCode') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemBarCode', ItemInfos[depth1].get('ItemBarCode'))
			if ItemInfos[depth1].get('CustomizeFeatureK') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureK', ItemInfos[depth1].get('CustomizeFeatureK'))
			if ItemInfos[depth1].get('CustomizeFeatureL') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureL', ItemInfos[depth1].get('CustomizeFeatureL'))
			if ItemInfos[depth1].get('CustomizeFeatureM') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureM', ItemInfos[depth1].get('CustomizeFeatureM'))
			if ItemInfos[depth1].get('BePromotion') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.BePromotion', ItemInfos[depth1].get('BePromotion'))
			if ItemInfos[depth1].get('CustomizeFeatureN') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureN', ItemInfos[depth1].get('CustomizeFeatureN'))
			if ItemInfos[depth1].get('CustomizeFeatureO') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureO', ItemInfos[depth1].get('CustomizeFeatureO'))
			if ItemInfos[depth1].get('PromotionEnd') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.PromotionEnd', ItemInfos[depth1].get('PromotionEnd'))
			if ItemInfos[depth1].get('ItemTitle') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemTitle', ItemInfos[depth1].get('ItemTitle'))
			if ItemInfos[depth1].get('CustomizeFeatureC') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureC', ItemInfos[depth1].get('CustomizeFeatureC'))
			if ItemInfos[depth1].get('CustomizeFeatureD') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureD', ItemInfos[depth1].get('CustomizeFeatureD'))
			if ItemInfos[depth1].get('ItemQrCode') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemQrCode', ItemInfos[depth1].get('ItemQrCode'))
			if ItemInfos[depth1].get('CustomizeFeatureE') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureE', ItemInfos[depth1].get('CustomizeFeatureE'))
			if ItemInfos[depth1].get('InventoryStatus') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.InventoryStatus', ItemInfos[depth1].get('InventoryStatus'))
			if ItemInfos[depth1].get('PromotionReason') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.PromotionReason', ItemInfos[depth1].get('PromotionReason'))
			if ItemInfos[depth1].get('CustomizeFeatureF') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureF', ItemInfos[depth1].get('CustomizeFeatureF'))
			if ItemInfos[depth1].get('CustomizeFeatureG') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureG', ItemInfos[depth1].get('CustomizeFeatureG'))
			if ItemInfos[depth1].get('CustomizeFeatureH') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureH', ItemInfos[depth1].get('CustomizeFeatureH'))
			if ItemInfos[depth1].get('CustomizeFeatureI') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureI', ItemInfos[depth1].get('CustomizeFeatureI'))
			if ItemInfos[depth1].get('CustomizeFeatureJ') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureJ', ItemInfos[depth1].get('CustomizeFeatureJ'))
			if ItemInfos[depth1].get('CustomizeFeatureA') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureA', ItemInfos[depth1].get('CustomizeFeatureA'))
			if ItemInfos[depth1].get('CustomizeFeatureB') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CustomizeFeatureB', ItemInfos[depth1].get('CustomizeFeatureB'))
			if ItemInfos[depth1].get('SuggestPrice') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SuggestPrice', ItemInfos[depth1].get('SuggestPrice'))
			if ItemInfos[depth1].get('ForestFirstId') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ForestFirstId', ItemInfos[depth1].get('ForestFirstId'))
			if ItemInfos[depth1].get('ProductionPlace') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ProductionPlace', ItemInfos[depth1].get('ProductionPlace'))
			if ItemInfos[depth1].get('Manufacturer') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.Manufacturer', ItemInfos[depth1].get('Manufacturer'))
			if ItemInfos[depth1].get('SourceCode') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SourceCode', ItemInfos[depth1].get('SourceCode'))
			if ItemInfos[depth1].get('ItemId') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemId', ItemInfos[depth1].get('ItemId'))
			if ItemInfos[depth1].get('SalesPrice') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SalesPrice', ItemInfos[depth1].get('SalesPrice'))
			if ItemInfos[depth1].get('OriginalPrice') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.OriginalPrice', ItemInfos[depth1].get('OriginalPrice'))
			if ItemInfos[depth1].get('ItemShortTitle') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemShortTitle', ItemInfos[depth1].get('ItemShortTitle'))
			if ItemInfos[depth1].get('ForestSecondId') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ForestSecondId', ItemInfos[depth1].get('ForestSecondId'))
			if ItemInfos[depth1].get('ItemPicUrl') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ItemPicUrl', ItemInfos[depth1].get('ItemPicUrl'))
			if ItemInfos[depth1].get('SupplierName') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SupplierName', ItemInfos[depth1].get('SupplierName'))
			if ItemInfos[depth1].get('Material') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.Material', ItemInfos[depth1].get('Material'))
			if ItemInfos[depth1].get('ModelNumber') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.ModelNumber', ItemInfos[depth1].get('ModelNumber'))
			if ItemInfos[depth1].get('SaleSpec') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SaleSpec', ItemInfos[depth1].get('SaleSpec'))
			if ItemInfos[depth1].get('CategoryName') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.CategoryName', ItemInfos[depth1].get('CategoryName'))
			if ItemInfos[depth1].get('TaxFee') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.TaxFee', ItemInfos[depth1].get('TaxFee'))
			if ItemInfos[depth1].get('EnergyEfficiency') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.EnergyEfficiency', ItemInfos[depth1].get('EnergyEfficiency'))
			if ItemInfos[depth1].get('PromotionText') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.PromotionText', ItemInfos[depth1].get('PromotionText'))
			if ItemInfos[depth1].get('SkuId') is not None:
				self.add_body_params('ItemInfo.' + str(depth1 + 1) + '.SkuId', ItemInfos[depth1].get('SkuId'))