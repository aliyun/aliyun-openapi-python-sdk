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
class ListNotaryOrdersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'ListNotaryOrders','trademark')

	def get_SortKeyType(self):
		return self.get_query_params().get('SortKeyType')

	def set_SortKeyType(self,SortKeyType):
		self.add_query_param('SortKeyType',SortKeyType)

	def get_SortByType(self):
		return self.get_query_params().get('SortByType')

	def set_SortByType(self,SortByType):
		self.add_query_param('SortByType',SortByType)

	def get_StartOrderDate(self):
		return self.get_query_params().get('StartOrderDate')

	def set_StartOrderDate(self,StartOrderDate):
		self.add_query_param('StartOrderDate',StartOrderDate)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_NotaryType(self):
		return self.get_query_params().get('NotaryType')

	def set_NotaryType(self,NotaryType):
		self.add_query_param('NotaryType',NotaryType)

	def get_EndOrderDate(self):
		return self.get_query_params().get('EndOrderDate')

	def set_EndOrderDate(self,EndOrderDate):
		self.add_query_param('EndOrderDate',EndOrderDate)

	def get_AliyunOrderId(self):
		return self.get_query_params().get('AliyunOrderId')

	def set_AliyunOrderId(self,AliyunOrderId):
		self.add_query_param('AliyunOrderId',AliyunOrderId)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_NotaryStatus(self):
		return self.get_query_params().get('NotaryStatus')

	def set_NotaryStatus(self,NotaryStatus):
		self.add_query_param('NotaryStatus',NotaryStatus)