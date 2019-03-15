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
class AddTrialRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'AddTrialRecord','finmall')

	def get_Note(self):
		return self.get_query_params().get('Note')

	def set_Note(self,Note):
		self.add_query_param('Note',Note)

	def get_EnterpriseEmail(self):
		return self.get_query_params().get('EnterpriseEmail')

	def set_EnterpriseEmail(self,EnterpriseEmail):
		self.add_query_param('EnterpriseEmail',EnterpriseEmail)

	def get_ContractPhoneNumber(self):
		return self.get_query_params().get('ContractPhoneNumber')

	def set_ContractPhoneNumber(self,ContractPhoneNumber):
		self.add_query_param('ContractPhoneNumber',ContractPhoneNumber)

	def get_ContractName(self):
		return self.get_query_params().get('ContractName')

	def set_ContractName(self,ContractName):
		self.add_query_param('ContractName',ContractName)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_EnterpriseName(self):
		return self.get_query_params().get('EnterpriseName')

	def set_EnterpriseName(self,EnterpriseName):
		self.add_query_param('EnterpriseName',EnterpriseName)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_Products(self):
		return self.get_query_params().get('Products')

	def set_Products(self,Products):
		self.add_query_param('Products',Products)

	def get_Budget(self):
		return self.get_query_params().get('Budget')

	def set_Budget(self,Budget):
		self.add_query_param('Budget',Budget)