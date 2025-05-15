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
from aliyunsdkdomain.endpoint import endpoint_data

class SubmitPurchaseInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'SubmitPurchaseInfo','domain')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PurchaseProofss(self): # RepeatList
		return self.get_body_params().get('PurchaseProofs')

	def set_PurchaseProofss(self, PurchaseProofs):  # RepeatList
		for depth1 in range(len(PurchaseProofs)):
			self.add_body_params('PurchaseProofs.' + str(depth1 + 1), PurchaseProofs[depth1])
	def get_PurchasePrice(self): # Double
		return self.get_body_params().get('PurchasePrice')

	def set_PurchasePrice(self, PurchasePrice):  # Double
		self.add_body_params('PurchasePrice', PurchasePrice)
	def get_PurchaseCurrency(self): # String
		return self.get_body_params().get('PurchaseCurrency')

	def set_PurchaseCurrency(self, PurchaseCurrency):  # String
		self.add_body_params('PurchaseCurrency', PurchaseCurrency)
	def get_BizId(self): # String
		return self.get_body_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_body_params('BizId', BizId)
