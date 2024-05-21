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
class DescribeWhiteListProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'DescribeWhiteListProcess','vipaegis')

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ProcessName(self):
		return self.get_query_params().get('ProcessName')

	def set_ProcessName(self,ProcessName):
		self.add_query_param('ProcessName',ProcessName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ProcessType(self):
		return self.get_query_params().get('ProcessType')

	def set_ProcessType(self,ProcessType):
		self.add_query_param('ProcessType',ProcessType)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_StrategyId(self):
		return self.get_query_params().get('StrategyId')

	def set_StrategyId(self,StrategyId):
		self.add_query_param('StrategyId',StrategyId)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Desc(self):
		return self.get_query_params().get('Desc')

	def set_Desc(self,Desc):
		self.add_query_param('Desc',Desc)