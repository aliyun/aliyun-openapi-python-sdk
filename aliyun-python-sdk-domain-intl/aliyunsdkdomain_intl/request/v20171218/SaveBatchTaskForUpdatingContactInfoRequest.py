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
class SaveBatchTaskForUpdatingContactInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain-intl', '2017-12-18', 'SaveBatchTaskForUpdatingContactInfo','domain')

	def get_ContactType(self):
		return self.get_query_params().get('ContactType')

	def set_ContactType(self,ContactType):
		self.add_query_param('ContactType',ContactType)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_RegistrantProfileId(self):
		return self.get_query_params().get('RegistrantProfileId')

	def set_RegistrantProfileId(self,RegistrantProfileId):
		self.add_query_param('RegistrantProfileId',RegistrantProfileId)

	def get_DomainNames(self):
		return self.get_query_params().get('DomainNames')

	def set_DomainNames(self,DomainNames):
		for i in range(len(DomainNames)):	
			if DomainNames[i] is not None:
				self.add_query_param('DomainName.' + str(i + 1) , DomainNames[i]);

	def get_AddTransferLock(self):
		return self.get_query_params().get('AddTransferLock')

	def set_AddTransferLock(self,AddTransferLock):
		self.add_query_param('AddTransferLock',AddTransferLock)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)