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

class QueryDomainListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryDomainList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductDomainType(self): # String
		return self.get_query_params().get('ProductDomainType')

	def set_ProductDomainType(self, ProductDomainType):  # String
		self.add_query_param('ProductDomainType', ProductDomainType)
	def get_OrderKeyType(self): # String
		return self.get_query_params().get('OrderKeyType')

	def set_OrderKeyType(self, OrderKeyType):  # String
		self.add_query_param('OrderKeyType', OrderKeyType)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_OrderByType(self): # String
		return self.get_query_params().get('OrderByType')

	def set_OrderByType(self, OrderByType):  # String
		self.add_query_param('OrderByType', OrderByType)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_QueryType(self): # String
		return self.get_query_params().get('QueryType')

	def set_QueryType(self, QueryType):  # String
		self.add_query_param('QueryType', QueryType)
	def get_EndExpirationDate(self): # Long
		return self.get_query_params().get('EndExpirationDate')

	def set_EndExpirationDate(self, EndExpirationDate):  # Long
		self.add_query_param('EndExpirationDate', EndExpirationDate)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_StartExpirationDate(self): # Long
		return self.get_query_params().get('StartExpirationDate')

	def set_StartExpirationDate(self, StartExpirationDate):  # Long
		self.add_query_param('StartExpirationDate', StartExpirationDate)
	def get_DomainGroupId(self): # String
		return self.get_query_params().get('DomainGroupId')

	def set_DomainGroupId(self, DomainGroupId):  # String
		self.add_query_param('DomainGroupId', DomainGroupId)
	def get_EndRegistrationDate(self): # Long
		return self.get_query_params().get('EndRegistrationDate')

	def set_EndRegistrationDate(self, EndRegistrationDate):  # Long
		self.add_query_param('EndRegistrationDate', EndRegistrationDate)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
	def get_StartRegistrationDate(self): # Long
		return self.get_query_params().get('StartRegistrationDate')

	def set_StartRegistrationDate(self, StartRegistrationDate):  # Long
		self.add_query_param('StartRegistrationDate', StartRegistrationDate)
