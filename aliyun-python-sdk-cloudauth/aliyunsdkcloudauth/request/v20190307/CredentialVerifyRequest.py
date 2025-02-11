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
from aliyunsdkcloudauth.endpoint import endpoint_data
import json

class CredentialVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'CredentialVerify','cloudauth')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_IsOCR(self): # String
		return self.get_query_params().get('IsOCR')

	def set_IsOCR(self, IsOCR):  # String
		self.add_query_param('IsOCR', IsOCR)
	def get_IsCheck(self): # String
		return self.get_query_params().get('IsCheck')

	def set_IsCheck(self, IsCheck):  # String
		self.add_query_param('IsCheck', IsCheck)
	def get_ImageContext(self): # String
		return self.get_body_params().get('ImageContext')

	def set_ImageContext(self, ImageContext):  # String
		self.add_body_params('ImageContext', ImageContext)
	def get_CredType(self): # String
		return self.get_query_params().get('CredType')

	def set_CredType(self, CredType):  # String
		self.add_query_param('CredType', CredType)
	def get_PromptModel(self): # String
		return self.get_query_params().get('PromptModel')

	def set_PromptModel(self, PromptModel):  # String
		self.add_query_param('PromptModel', PromptModel)
	def get_IdentifyNum(self): # String
		return self.get_query_params().get('IdentifyNum')

	def set_IdentifyNum(self, IdentifyNum):  # String
		self.add_query_param('IdentifyNum', IdentifyNum)
	def get_CredName(self): # String
		return self.get_query_params().get('CredName')

	def set_CredName(self, CredName):  # String
		self.add_query_param('CredName', CredName)
	def get_MerchantId(self): # String
		return self.get_query_params().get('MerchantId')

	def set_MerchantId(self, MerchantId):  # String
		self.add_query_param('MerchantId', MerchantId)
	def get_MerchantDetail(self): # Array
		return self.get_query_params().get('MerchantDetail')

	def set_MerchantDetail(self, MerchantDetail):  # Array
		self.add_query_param("MerchantDetail", json.dumps(MerchantDetail))
	def get_ImageUrl(self): # String
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_query_param('ImageUrl', ImageUrl)
	def get_CertNum(self): # String
		return self.get_query_params().get('CertNum')

	def set_CertNum(self, CertNum):  # String
		self.add_query_param('CertNum', CertNum)
	def get_Prompt(self): # String
		return self.get_query_params().get('Prompt')

	def set_Prompt(self, Prompt):  # String
		self.add_query_param('Prompt', Prompt)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
