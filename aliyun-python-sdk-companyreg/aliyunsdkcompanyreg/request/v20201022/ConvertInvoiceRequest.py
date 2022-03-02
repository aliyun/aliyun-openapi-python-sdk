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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class ConvertInvoiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2020-10-22', 'ConvertInvoice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsFee(self): # Boolean
		return self.get_query_params().get('IsFee')

	def set_IsFee(self, IsFee):  # Boolean
		self.add_query_param('IsFee', IsFee)
	def get_ShellMethod(self): # String
		return self.get_query_params().get('ShellMethod')

	def set_ShellMethod(self, ShellMethod):  # String
		self.add_query_param('ShellMethod', ShellMethod)
	def get_Kind(self): # String
		return self.get_query_params().get('Kind')

	def set_Kind(self, Kind):  # String
		self.add_query_param('Kind', Kind)
	def get_Use(self): # String
		return self.get_query_params().get('Use')

	def set_Use(self, Use):  # String
		self.add_query_param('Use', Use)
	def get_ThirdKey(self): # String
		return self.get_query_params().get('ThirdKey')

	def set_ThirdKey(self, ThirdKey):  # String
		self.add_query_param('ThirdKey', ThirdKey)
	def get_Payer(self): # String
		return self.get_query_params().get('Payer')

	def set_Payer(self, Payer):  # String
		self.add_query_param('Payer', Payer)
	def get_SecondKey(self): # String
		return self.get_query_params().get('SecondKey')

	def set_SecondKey(self, SecondKey):  # String
		self.add_query_param('SecondKey', SecondKey)
	def get_PayMethod(self): # String
		return self.get_query_params().get('PayMethod')

	def set_PayMethod(self, PayMethod):  # String
		self.add_query_param('PayMethod', PayMethod)
	def get_BuyMethod(self): # String
		return self.get_query_params().get('BuyMethod')

	def set_BuyMethod(self, BuyMethod):  # String
		self.add_query_param('BuyMethod', BuyMethod)
	def get_FixedAssetType(self): # String
		return self.get_query_params().get('FixedAssetType')

	def set_FixedAssetType(self, FixedAssetType):  # String
		self.add_query_param('FixedAssetType', FixedAssetType)
	def get_FirstKey(self): # String
		return self.get_query_params().get('FirstKey')

	def set_FirstKey(self, FirstKey):  # String
		self.add_query_param('FirstKey', FirstKey)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_BuyTarget(self): # String
		return self.get_query_params().get('BuyTarget')

	def set_BuyTarget(self, BuyTarget):  # String
		self.add_query_param('BuyTarget', BuyTarget)
