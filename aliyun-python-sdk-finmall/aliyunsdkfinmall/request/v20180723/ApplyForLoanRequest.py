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
class ApplyForLoanRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'ApplyForLoan','finmall')

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_CreditId(self):
		return self.get_query_params().get('CreditId')

	def set_CreditId(self,CreditId):
		self.add_query_param('CreditId',CreditId)

	def get_ProductId(self):
		return self.get_query_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_query_param('ProductId',ProductId)

	def get_FundpartyId(self):
		return self.get_query_params().get('FundpartyId')

	def set_FundpartyId(self,FundpartyId):
		self.add_query_param('FundpartyId',FundpartyId)

	def get_BizData(self):
		return self.get_query_params().get('BizData')

	def set_BizData(self,BizData):
		self.add_query_param('BizData',BizData)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)