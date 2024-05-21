# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryDomainListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain-intl', '2017-12-18', 'QueryDomainList','domain')

	def get_EndExpirationDate(self):
		return self.get_query_params().get('EndExpirationDate')

	def set_EndExpirationDate(self,EndExpirationDate):
		self.add_query_param('EndExpirationDate',EndExpirationDate)

	def get_ProductDomainType(self):
		return self.get_query_params().get('ProductDomainType')

	def set_ProductDomainType(self,ProductDomainType):
		self.add_query_param('ProductDomainType',ProductDomainType)

	def get_OrderKeyType(self):
		return self.get_query_params().get('OrderKeyType')

	def set_OrderKeyType(self,OrderKeyType):
		self.add_query_param('OrderKeyType',OrderKeyType)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_StartExpirationDate(self):
		return self.get_query_params().get('StartExpirationDate')

	def set_StartExpirationDate(self,StartExpirationDate):
		self.add_query_param('StartExpirationDate',StartExpirationDate)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_OrderByType(self):
		return self.get_query_params().get('OrderByType')

	def set_OrderByType(self,OrderByType):
		self.add_query_param('OrderByType',OrderByType)

	def get_EndRegistrationDate(self):
		return self.get_query_params().get('EndRegistrationDate')

	def set_EndRegistrationDate(self,EndRegistrationDate):
		self.add_query_param('EndRegistrationDate',EndRegistrationDate)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_QueryType(self):
		return self.get_query_params().get('QueryType')

	def set_QueryType(self,QueryType):
		self.add_query_param('QueryType',QueryType)

	def get_StartRegistrationDate(self):
		return self.get_query_params().get('StartRegistrationDate')

	def set_StartRegistrationDate(self,StartRegistrationDate):
		self.add_query_param('StartRegistrationDate',StartRegistrationDate)