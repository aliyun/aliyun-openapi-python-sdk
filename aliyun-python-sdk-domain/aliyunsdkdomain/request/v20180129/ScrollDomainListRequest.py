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

class ScrollDomainListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'ScrollDomainList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductDomainType(self): # String
		return self.get_query_params().get('ProductDomainType')

	def set_ProductDomainType(self, ProductDomainType):  # String
		self.add_query_param('ProductDomainType', ProductDomainType)
	def get_Excluded(self): # String
		return self.get_query_params().get('Excluded')

	def set_Excluded(self, Excluded):  # String
		self.add_query_param('Excluded', Excluded)
	def get_StartLength(self): # Integer
		return self.get_query_params().get('StartLength')

	def set_StartLength(self, StartLength):  # Integer
		self.add_query_param('StartLength', StartLength)
	def get_ExcludedSuffix(self): # Boolean
		return self.get_query_params().get('ExcludedSuffix')

	def set_ExcludedSuffix(self, ExcludedSuffix):  # Boolean
		self.add_query_param('ExcludedSuffix', ExcludedSuffix)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ExcludedPrefix(self): # Boolean
		return self.get_query_params().get('ExcludedPrefix')

	def set_ExcludedPrefix(self, ExcludedPrefix):  # Boolean
		self.add_query_param('ExcludedPrefix', ExcludedPrefix)
	def get_KeyWord(self): # String
		return self.get_query_params().get('KeyWord')

	def set_KeyWord(self, KeyWord):  # String
		self.add_query_param('KeyWord', KeyWord)
	def get_EndExpirationDate(self): # Long
		return self.get_query_params().get('EndExpirationDate')

	def set_EndExpirationDate(self, EndExpirationDate):  # Long
		self.add_query_param('EndExpirationDate', EndExpirationDate)
	def get_Suffixs(self): # String
		return self.get_query_params().get('Suffixs')

	def set_Suffixs(self, Suffixs):  # String
		self.add_query_param('Suffixs', Suffixs)
	def get_StartExpirationDate(self): # Long
		return self.get_query_params().get('StartExpirationDate')

	def set_StartExpirationDate(self, StartExpirationDate):  # Long
		self.add_query_param('StartExpirationDate', StartExpirationDate)
	def get_DomainStatus(self): # Integer
		return self.get_query_params().get('DomainStatus')

	def set_DomainStatus(self, DomainStatus):  # Integer
		self.add_query_param('DomainStatus', DomainStatus)
	def get_DomainGroupId(self): # Long
		return self.get_query_params().get('DomainGroupId')

	def set_DomainGroupId(self, DomainGroupId):  # Long
		self.add_query_param('DomainGroupId', DomainGroupId)
	def get_KeyWordSuffix(self): # Boolean
		return self.get_query_params().get('KeyWordSuffix')

	def set_KeyWordSuffix(self, KeyWordSuffix):  # Boolean
		self.add_query_param('KeyWordSuffix', KeyWordSuffix)
	def get_ScrollId(self): # String
		return self.get_query_params().get('ScrollId')

	def set_ScrollId(self, ScrollId):  # String
		self.add_query_param('ScrollId', ScrollId)
	def get_KeyWordPrefix(self): # Boolean
		return self.get_query_params().get('KeyWordPrefix')

	def set_KeyWordPrefix(self, KeyWordPrefix):  # Boolean
		self.add_query_param('KeyWordPrefix', KeyWordPrefix)
	def get_TradeType(self): # Integer
		return self.get_query_params().get('TradeType')

	def set_TradeType(self, TradeType):  # Integer
		self.add_query_param('TradeType', TradeType)
	def get_EndRegistrationDate(self): # Long
		return self.get_query_params().get('EndRegistrationDate')

	def set_EndRegistrationDate(self, EndRegistrationDate):  # Long
		self.add_query_param('EndRegistrationDate', EndRegistrationDate)
	def get_Form(self): # Integer
		return self.get_query_params().get('Form')

	def set_Form(self, Form):  # Integer
		self.add_query_param('Form', Form)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_StartRegistrationDate(self): # Long
		return self.get_query_params().get('StartRegistrationDate')

	def set_StartRegistrationDate(self, StartRegistrationDate):  # Long
		self.add_query_param('StartRegistrationDate', StartRegistrationDate)
	def get_EndLength(self): # Integer
		return self.get_query_params().get('EndLength')

	def set_EndLength(self, EndLength):  # Integer
		self.add_query_param('EndLength', EndLength)
