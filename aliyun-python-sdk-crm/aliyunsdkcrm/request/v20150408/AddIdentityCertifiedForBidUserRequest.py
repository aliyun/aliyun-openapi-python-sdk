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
class AddIdentityCertifiedForBidUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Crm', '2015-04-08', 'AddIdentityCertifiedForBidUser','crm')

	def get_BidType(self):
		return self.get_query_params().get('BidType')

	def set_BidType(self,BidType):
		self.add_query_param('BidType',BidType)

	def get_LicenseNumber(self):
		return self.get_query_params().get('LicenseNumber')

	def set_LicenseNumber(self,LicenseNumber):
		self.add_query_param('LicenseNumber',LicenseNumber)

	def get_LicenseType(self):
		return self.get_query_params().get('LicenseType')

	def set_LicenseType(self,LicenseType):
		self.add_query_param('LicenseType',LicenseType)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PK(self):
		return self.get_query_params().get('PK')

	def set_PK(self,PK):
		self.add_query_param('PK',PK)

	def get_IsEnterprise(self):
		return self.get_query_params().get('IsEnterprise')

	def set_IsEnterprise(self,IsEnterprise):
		self.add_query_param('IsEnterprise',IsEnterprise)