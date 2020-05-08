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

	def set_ItemInfos(self,ItemInfos):
		for i in range(len(ItemInfos)):	
			if ItemInfos[i].get('MemberPrice') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.MemberPrice' , ItemInfos[i].get('MemberPrice'))
			if ItemInfos[i].get('ActionPrice') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ActionPrice' , ItemInfos[i].get('ActionPrice'))
			if ItemInfos[i].get('BeSourceCode') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.BeSourceCode' , ItemInfos[i].get('BeSourceCode'))
			if ItemInfos[i].get('BrandName') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.BrandName' , ItemInfos[i].get('BrandName'))
			if ItemInfos[i].get('PromotionStart') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.PromotionStart' , ItemInfos[i].get('PromotionStart'))
			if ItemInfos[i].get('PriceUnit') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.PriceUnit' , ItemInfos[i].get('PriceUnit'))
			if ItemInfos[i].get('Rank') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.Rank' , ItemInfos[i].get('Rank'))
			if ItemInfos[i].get('ItemInfoIndex') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemInfoIndex' , ItemInfos[i].get('ItemInfoIndex'))
			if ItemInfos[i].get('ItemBarCode') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemBarCode' , ItemInfos[i].get('ItemBarCode'))
			if ItemInfos[i].get('CustomizeFeatureK') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureK' , ItemInfos[i].get('CustomizeFeatureK'))
			if ItemInfos[i].get('CustomizeFeatureL') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureL' , ItemInfos[i].get('CustomizeFeatureL'))
			if ItemInfos[i].get('CustomizeFeatureM') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureM' , ItemInfos[i].get('CustomizeFeatureM'))
			if ItemInfos[i].get('BePromotion') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.BePromotion' , ItemInfos[i].get('BePromotion'))
			if ItemInfos[i].get('CustomizeFeatureN') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureN' , ItemInfos[i].get('CustomizeFeatureN'))
			if ItemInfos[i].get('CustomizeFeatureO') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureO' , ItemInfos[i].get('CustomizeFeatureO'))
			if ItemInfos[i].get('PromotionEnd') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.PromotionEnd' , ItemInfos[i].get('PromotionEnd'))
			if ItemInfos[i].get('ItemTitle') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemTitle' , ItemInfos[i].get('ItemTitle'))
			if ItemInfos[i].get('CustomizeFeatureC') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureC' , ItemInfos[i].get('CustomizeFeatureC'))
			if ItemInfos[i].get('CustomizeFeatureD') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureD' , ItemInfos[i].get('CustomizeFeatureD'))
			if ItemInfos[i].get('ItemQrCode') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemQrCode' , ItemInfos[i].get('ItemQrCode'))
			if ItemInfos[i].get('CustomizeFeatureE') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureE' , ItemInfos[i].get('CustomizeFeatureE'))
			if ItemInfos[i].get('InventoryStatus') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.InventoryStatus' , ItemInfos[i].get('InventoryStatus'))
			if ItemInfos[i].get('PromotionReason') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.PromotionReason' , ItemInfos[i].get('PromotionReason'))
			if ItemInfos[i].get('CustomizeFeatureF') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureF' , ItemInfos[i].get('CustomizeFeatureF'))
			if ItemInfos[i].get('CustomizeFeatureG') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureG' , ItemInfos[i].get('CustomizeFeatureG'))
			if ItemInfos[i].get('CustomizeFeatureH') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureH' , ItemInfos[i].get('CustomizeFeatureH'))
			if ItemInfos[i].get('CustomizeFeatureI') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureI' , ItemInfos[i].get('CustomizeFeatureI'))
			if ItemInfos[i].get('CustomizeFeatureJ') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureJ' , ItemInfos[i].get('CustomizeFeatureJ'))
			if ItemInfos[i].get('CustomizeFeatureA') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureA' , ItemInfos[i].get('CustomizeFeatureA'))
			if ItemInfos[i].get('CustomizeFeatureB') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CustomizeFeatureB' , ItemInfos[i].get('CustomizeFeatureB'))
			if ItemInfos[i].get('SuggestPrice') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SuggestPrice' , ItemInfos[i].get('SuggestPrice'))
			if ItemInfos[i].get('ForestFirstId') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ForestFirstId' , ItemInfos[i].get('ForestFirstId'))
			if ItemInfos[i].get('ProductionPlace') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ProductionPlace' , ItemInfos[i].get('ProductionPlace'))
			if ItemInfos[i].get('Manufacturer') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.Manufacturer' , ItemInfos[i].get('Manufacturer'))
			if ItemInfos[i].get('SourceCode') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SourceCode' , ItemInfos[i].get('SourceCode'))
			if ItemInfos[i].get('ItemId') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemId' , ItemInfos[i].get('ItemId'))
			if ItemInfos[i].get('SalesPrice') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SalesPrice' , ItemInfos[i].get('SalesPrice'))
			if ItemInfos[i].get('OriginalPrice') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.OriginalPrice' , ItemInfos[i].get('OriginalPrice'))
			if ItemInfos[i].get('ItemShortTitle') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemShortTitle' , ItemInfos[i].get('ItemShortTitle'))
			if ItemInfos[i].get('ForestSecondId') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ForestSecondId' , ItemInfos[i].get('ForestSecondId'))
			if ItemInfos[i].get('ItemPicUrl') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ItemPicUrl' , ItemInfos[i].get('ItemPicUrl'))
			if ItemInfos[i].get('SupplierName') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SupplierName' , ItemInfos[i].get('SupplierName'))
			if ItemInfos[i].get('Material') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.Material' , ItemInfos[i].get('Material'))
			if ItemInfos[i].get('ModelNumber') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.ModelNumber' , ItemInfos[i].get('ModelNumber'))
			if ItemInfos[i].get('SaleSpec') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SaleSpec' , ItemInfos[i].get('SaleSpec'))
			if ItemInfos[i].get('CategoryName') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.CategoryName' , ItemInfos[i].get('CategoryName'))
			if ItemInfos[i].get('TaxFee') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.TaxFee' , ItemInfos[i].get('TaxFee'))
			if ItemInfos[i].get('EnergyEfficiency') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.EnergyEfficiency' , ItemInfos[i].get('EnergyEfficiency'))
			if ItemInfos[i].get('PromotionText') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.PromotionText' , ItemInfos[i].get('PromotionText'))
			if ItemInfos[i].get('SkuId') is not None:
				self.add_body_params('ItemInfo.' + str(i + 1) + '.SkuId' , ItemInfos[i].get('SkuId'))
