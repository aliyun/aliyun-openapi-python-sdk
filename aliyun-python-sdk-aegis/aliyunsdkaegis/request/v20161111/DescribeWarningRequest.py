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
class DescribeWarningRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'DescribeWarning','vipaegis')

	def get_TypeNames(self):
		return self.get_query_params().get('TypeNames')

	def set_TypeNames(self,TypeNames):
		self.add_query_param('TypeNames',TypeNames)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RiskName(self):
		return self.get_query_params().get('RiskName')

	def set_RiskName(self,RiskName):
		self.add_query_param('RiskName',RiskName)

	def get_StatusList(self):
		return self.get_query_params().get('StatusList')

	def set_StatusList(self,StatusList):
		self.add_query_param('StatusList',StatusList)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_RiskLevels(self):
		return self.get_query_params().get('RiskLevels')

	def set_RiskLevels(self,RiskLevels):
		self.add_query_param('RiskLevels',RiskLevels)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_SubTypeNames(self):
		return self.get_query_params().get('SubTypeNames')

	def set_SubTypeNames(self,SubTypeNames):
		self.add_query_param('SubTypeNames',SubTypeNames)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)