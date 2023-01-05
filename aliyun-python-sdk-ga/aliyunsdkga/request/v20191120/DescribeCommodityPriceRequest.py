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
from aliyunsdkga.endpoint import endpoint_data

class DescribeCommodityPriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'DescribeCommodityPrice','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PromotionOptionNo(self): # String
		return self.get_query_params().get('PromotionOptionNo')

	def set_PromotionOptionNo(self, PromotionOptionNo):  # String
		self.add_query_param('PromotionOptionNo', PromotionOptionNo)
	def get_Orders(self): # Array
		return self.get_query_params().get('Orders')

	def set_Orders(self, Orders):  # Array
		for index1, value1 in enumerate(Orders):
			if value1.get('CommodityCode') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.CommodityCode', value1.get('CommodityCode'))
			if value1.get('OrderType') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.OrderType', value1.get('OrderType'))
			if value1.get('ChargeType') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.ChargeType', value1.get('ChargeType'))
			if value1.get('PricingCycle') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.PricingCycle', value1.get('PricingCycle'))
			if value1.get('Duration') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.Duration', value1.get('Duration'))
			if value1.get('Quantity') is not None:
				self.add_query_param('Orders.' + str(index1 + 1) + '.Quantity', value1.get('Quantity'))
			if value1.get('Components') is not None:
				for index2, value2 in enumerate(value1.get('Components')):
					if value2.get('ComponentCode') is not None:
						self.add_query_param('Orders.' + str(index1 + 1) + '.Components.' + str(index2 + 1) + '.ComponentCode', value2.get('ComponentCode'))
					if value2.get('Properties') is not None:
						for index3, value3 in enumerate(value2.get('Properties')):
							if value3.get('Code') is not None:
								self.add_query_param('Orders.' + str(index1 + 1) + '.Components.' + str(index2 + 1) + '.Properties.' + str(index3 + 1) + '.Code', value3.get('Code'))
							if value3.get('Value') is not None:
								self.add_query_param('Orders.' + str(index1 + 1) + '.Components.' + str(index2 + 1) + '.Properties.' + str(index3 + 1) + '.Value', value3.get('Value'))
