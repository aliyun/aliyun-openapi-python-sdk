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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class ApplyInvoiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'ApplyInvoice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InvoicingType(self):
		return self.get_query_params().get('InvoicingType')

	def set_InvoicingType(self,InvoicingType):
		self.add_query_param('InvoicingType',InvoicingType)

	def get_ProcessWay(self):
		return self.get_query_params().get('ProcessWay')

	def set_ProcessWay(self,ProcessWay):
		self.add_query_param('ProcessWay',ProcessWay)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_InvoiceAmount(self):
		return self.get_query_params().get('InvoiceAmount')

	def set_InvoiceAmount(self,InvoiceAmount):
		self.add_query_param('InvoiceAmount',InvoiceAmount)

	def get_AddressId(self):
		return self.get_query_params().get('AddressId')

	def set_AddressId(self,AddressId):
		self.add_query_param('AddressId',AddressId)

	def get_ApplyUserNick(self):
		return self.get_query_params().get('ApplyUserNick')

	def set_ApplyUserNick(self,ApplyUserNick):
		self.add_query_param('ApplyUserNick',ApplyUserNick)

	def get_InvoiceByAmount(self):
		return self.get_query_params().get('InvoiceByAmount')

	def set_InvoiceByAmount(self,InvoiceByAmount):
		self.add_query_param('InvoiceByAmount',InvoiceByAmount)

	def get_CustomerId(self):
		return self.get_query_params().get('CustomerId')

	def set_CustomerId(self,CustomerId):
		self.add_query_param('CustomerId',CustomerId)

	def get_SelectedIdss(self):
		return self.get_query_params().get('SelectedIdss')

	def set_SelectedIdss(self, SelectedIdss):
		for depth1 in range(len(SelectedIdss)):
			if SelectedIdss[depth1] is not None:
				self.add_query_param('SelectedIds.' + str(depth1 + 1) , SelectedIdss[depth1])