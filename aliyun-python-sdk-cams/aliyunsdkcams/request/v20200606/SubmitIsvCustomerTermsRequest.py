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
from aliyunsdkcams.endpoint import endpoint_data

class SubmitIsvCustomerTermsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'SubmitIsvCustomerTerms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeAddress(self): # String
		return self.get_query_params().get('OfficeAddress')

	def set_OfficeAddress(self, OfficeAddress):  # String
		self.add_query_param('OfficeAddress', OfficeAddress)
	def get_IsvTerms(self): # String
		return self.get_query_params().get('IsvTerms')

	def set_IsvTerms(self, IsvTerms):  # String
		self.add_query_param('IsvTerms', IsvTerms)
	def get_ContactMail(self): # String
		return self.get_query_params().get('ContactMail')

	def set_ContactMail(self, ContactMail):  # String
		self.add_query_param('ContactMail', ContactMail)
	def get_CountryId(self): # String
		return self.get_query_params().get('CountryId')

	def set_CountryId(self, CountryId):  # String
		self.add_query_param('CountryId', CountryId)
	def get_CustSpaceId(self): # String
		return self.get_query_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_query_param('CustSpaceId', CustSpaceId)
	def get_BusinessDesc(self): # String
		return self.get_query_params().get('BusinessDesc')

	def set_BusinessDesc(self, BusinessDesc):  # String
		self.add_query_param('BusinessDesc', BusinessDesc)
	def get_CustName(self): # String
		return self.get_query_params().get('CustName')

	def set_CustName(self, CustName):  # String
		self.add_query_param('CustName', CustName)
