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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class QueryAccountTransactionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'QueryAccountTransactions','bssopenapi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_CreateTimeEnd(self):
		return self.get_query_params().get('CreateTimeEnd')

	def set_CreateTimeEnd(self,CreateTimeEnd):
		self.add_query_param('CreateTimeEnd',CreateTimeEnd)

	def get_RecordID(self):
		return self.get_query_params().get('RecordID')

	def set_RecordID(self,RecordID):
		self.add_query_param('RecordID',RecordID)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TransactionChannelSN(self):
		return self.get_query_params().get('TransactionChannelSN')

	def set_TransactionChannelSN(self,TransactionChannelSN):
		self.add_query_param('TransactionChannelSN',TransactionChannelSN)

	def get_CreateTimeStart(self):
		return self.get_query_params().get('CreateTimeStart')

	def set_CreateTimeStart(self,CreateTimeStart):
		self.add_query_param('CreateTimeStart',CreateTimeStart)

	def get_TransactionNumber(self):
		return self.get_query_params().get('TransactionNumber')

	def set_TransactionNumber(self,TransactionNumber):
		self.add_query_param('TransactionNumber',TransactionNumber)