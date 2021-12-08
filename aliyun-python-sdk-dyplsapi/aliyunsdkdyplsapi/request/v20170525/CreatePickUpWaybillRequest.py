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
from aliyunsdkdyplsapi.endpoint import endpoint_data

class CreatePickUpWaybillRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyplsapi', '2017-05-25', 'CreatePickUpWaybill')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConsigneeName(self):
		return self.get_query_params().get('ConsigneeName')

	def set_ConsigneeName(self,ConsigneeName):
		self.add_query_param('ConsigneeName',ConsigneeName)

	def get_OrderChannels(self):
		return self.get_query_params().get('OrderChannels')

	def set_OrderChannels(self,OrderChannels):
		self.add_query_param('OrderChannels',OrderChannels)

	def get_SendAddress(self):
		return self.get_query_params().get('SendAddress')

	def set_SendAddress(self,SendAddress):
		self.add_query_param('SendAddress',SendAddress)

	def get_OuterOrderCode(self):
		return self.get_query_params().get('OuterOrderCode')

	def set_OuterOrderCode(self,OuterOrderCode):
		self.add_query_param('OuterOrderCode',OuterOrderCode)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_CpCode(self):
		return self.get_query_params().get('CpCode')

	def set_CpCode(self,CpCode):
		self.add_query_param('CpCode',CpCode)

	def get_SendMobile(self):
		return self.get_query_params().get('SendMobile')

	def set_SendMobile(self,SendMobile):
		self.add_query_param('SendMobile',SendMobile)

	def get_ConsigneeMobile(self):
		return self.get_query_params().get('ConsigneeMobile')

	def set_ConsigneeMobile(self,ConsigneeMobile):
		self.add_query_param('ConsigneeMobile',ConsigneeMobile)

	def get_ContentType(self):
		return self.get_headers().get('Content-Type')

	def set_ContentType(self,ContentType):
		self.add_header('Content-Type',ContentType)

	def get_ConsigneeAddress(self):
		return self.get_query_params().get('ConsigneeAddress')

	def set_ConsigneeAddress(self,ConsigneeAddress):
		self.add_query_param('ConsigneeAddress',ConsigneeAddress)

	def get_SendPhone(self):
		return self.get_query_params().get('SendPhone')

	def set_SendPhone(self,SendPhone):
		self.add_query_param('SendPhone',SendPhone)

	def get_GoodsInfos(self):
		return self.get_query_params().get('GoodsInfos')

	def set_GoodsInfos(self,GoodsInfos):
		self.add_query_param('GoodsInfos',GoodsInfos)

	def get_SendName(self):
		return self.get_query_params().get('SendName')

	def set_SendName(self,SendName):
		self.add_query_param('SendName',SendName)

	def get_ConsigneePhone(self):
		return self.get_query_params().get('ConsigneePhone')

	def set_ConsigneePhone(self,ConsigneePhone):
		self.add_query_param('ConsigneePhone',ConsigneePhone)