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

class UploadIcpBasicMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'UploadIcpBasicMaterial')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SocialCreditCode(self): # String
		return self.get_query_params().get('SocialCreditCode')

	def set_SocialCreditCode(self, SocialCreditCode):  # String
		self.add_query_param('SocialCreditCode', SocialCreditCode)
	def get_BusinessLicense(self): # String
		return self.get_query_params().get('BusinessLicense')

	def set_BusinessLicense(self, BusinessLicense):  # String
		self.add_query_param('BusinessLicense', BusinessLicense)
	def get_CorporateIdCard(self): # String
		return self.get_query_params().get('CorporateIdCard')

	def set_CorporateIdCard(self, CorporateIdCard):  # String
		self.add_query_param('CorporateIdCard', CorporateIdCard)
	def get_IdCardList(self): # String
		return self.get_query_params().get('IdCardList')

	def set_IdCardList(self, IdCardList):  # String
		self.add_query_param('IdCardList', IdCardList)
	def get_CompanyAddress(self): # String
		return self.get_query_params().get('CompanyAddress')

	def set_CompanyAddress(self, CompanyAddress):  # String
		self.add_query_param('CompanyAddress', CompanyAddress)
	def get_CompanyName(self): # String
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self, CompanyName):  # String
		self.add_query_param('CompanyName', CompanyName)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_CorporateName(self): # String
		return self.get_query_params().get('CorporateName')

	def set_CorporateName(self, CorporateName):  # String
		self.add_query_param('CorporateName', CorporateName)
