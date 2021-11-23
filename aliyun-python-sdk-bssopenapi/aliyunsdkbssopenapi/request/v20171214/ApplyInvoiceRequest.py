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

	def get_InvoicingType(self): # Integer
		return self.get_query_params().get('InvoicingType')

	def set_InvoicingType(self, InvoicingType):  # Integer
		self.add_query_param('InvoicingType', InvoicingType)
	def get_ProcessWay(self): # Integer
		return self.get_query_params().get('ProcessWay')

	def set_ProcessWay(self, ProcessWay):  # Integer
		self.add_query_param('ProcessWay', ProcessWay)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InvoiceAmount(self): # Long
		return self.get_query_params().get('InvoiceAmount')

	def set_InvoiceAmount(self, InvoiceAmount):  # Long
		self.add_query_param('InvoiceAmount', InvoiceAmount)
	def get_AddressId(self): # Long
		return self.get_query_params().get('AddressId')

	def set_AddressId(self, AddressId):  # Long
		self.add_query_param('AddressId', AddressId)
	def get_ApplyUserNick(self): # String
		return self.get_query_params().get('ApplyUserNick')

	def set_ApplyUserNick(self, ApplyUserNick):  # String
		self.add_query_param('ApplyUserNick', ApplyUserNick)
	def get_InvoiceByAmount(self): # Boolean
		return self.get_query_params().get('InvoiceByAmount')

	def set_InvoiceByAmount(self, InvoiceByAmount):  # Boolean
		self.add_query_param('InvoiceByAmount', InvoiceByAmount)
	def get_CustomerId(self): # Long
		return self.get_query_params().get('CustomerId')

	def set_CustomerId(self, CustomerId):  # Long
		self.add_query_param('CustomerId', CustomerId)
	def get_SelectedIdss(self): # RepeatList
		return self.get_query_params().get('SelectedIds')

	def set_SelectedIdss(self, SelectedIds):  # RepeatList
		for depth1 in range(len(SelectedIds)):
			self.add_query_param('SelectedIds.' + str(depth1 + 1), SelectedIds[depth1])
	def get_UserRemark(self): # String
		return self.get_query_params().get('UserRemark')

	def set_UserRemark(self, UserRemark):  # String
		self.add_query_param('UserRemark', UserRemark)
