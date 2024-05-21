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
class QueryTradeMarkApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'QueryTradeMarkApplications','trademark')

	def get_TmName(self):
		return self.get_query_params().get('TmName')

	def set_TmName(self,TmName):
		self.add_query_param('TmName',TmName)

	def get_MaterialName(self):
		return self.get_query_params().get('MaterialName')

	def set_MaterialName(self,MaterialName):
		self.add_query_param('MaterialName',MaterialName)

	def get_OrderId(self):
		return self.get_query_params().get('OrderId')

	def set_OrderId(self,OrderId):
		self.add_query_param('OrderId',OrderId)

	def get_SupplementStatus(self):
		return self.get_query_params().get('SupplementStatus')

	def set_SupplementStatus(self,SupplementStatus):
		self.add_query_param('SupplementStatus',SupplementStatus)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_TmNumber(self):
		return self.get_query_params().get('TmNumber')

	def set_TmNumber(self,TmNumber):
		self.add_query_param('TmNumber',TmNumber)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)