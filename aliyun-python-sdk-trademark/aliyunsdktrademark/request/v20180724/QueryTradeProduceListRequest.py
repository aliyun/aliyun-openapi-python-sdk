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
class QueryTradeProduceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'QueryTradeProduceList','trademark')

	def get_BuyerStatus(self):
		return self.get_query_params().get('BuyerStatus')

	def set_BuyerStatus(self,BuyerStatus):
		self.add_query_param('BuyerStatus',BuyerStatus)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PreOrderId(self):
		return self.get_query_params().get('PreOrderId')

	def set_PreOrderId(self,PreOrderId):
		self.add_query_param('PreOrderId',PreOrderId)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_SortOrder(self):
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self,SortOrder):
		self.add_query_param('SortOrder',SortOrder)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_SortFiled(self):
		return self.get_query_params().get('SortFiled')

	def set_SortFiled(self,SortFiled):
		self.add_query_param('SortFiled',SortFiled)

	def get_RegisterNumber(self):
		return self.get_query_params().get('RegisterNumber')

	def set_RegisterNumber(self,RegisterNumber):
		self.add_query_param('RegisterNumber',RegisterNumber)