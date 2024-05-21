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
class ExportWarningRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'ExportWarning','vipaegis')

	def get_StatusList(self):
		return self.get_query_params().get('StatusList')

	def set_StatusList(self,StatusList):
		self.add_query_param('StatusList',StatusList)

	def get_RiskLevels(self):
		return self.get_query_params().get('RiskLevels')

	def set_RiskLevels(self,RiskLevels):
		self.add_query_param('RiskLevels',RiskLevels)

	def get_ExportType(self):
		return self.get_query_params().get('ExportType')

	def set_ExportType(self,ExportType):
		self.add_query_param('ExportType',ExportType)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_TypeNames(self):
		return self.get_query_params().get('TypeNames')

	def set_TypeNames(self,TypeNames):
		self.add_query_param('TypeNames',TypeNames)

	def get_IsSummaryExport(self):
		return self.get_query_params().get('IsSummaryExport')

	def set_IsSummaryExport(self,IsSummaryExport):
		self.add_query_param('IsSummaryExport',IsSummaryExport)

	def get_RiskName(self):
		return self.get_query_params().get('RiskName')

	def set_RiskName(self,RiskName):
		self.add_query_param('RiskName',RiskName)

	def get_RiskIds(self):
		return self.get_query_params().get('RiskIds')

	def set_RiskIds(self,RiskIds):
		self.add_query_param('RiskIds',RiskIds)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_StrategyId(self):
		return self.get_query_params().get('StrategyId')

	def set_StrategyId(self,StrategyId):
		self.add_query_param('StrategyId',StrategyId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_TypeName(self):
		return self.get_query_params().get('TypeName')

	def set_TypeName(self,TypeName):
		self.add_query_param('TypeName',TypeName)

	def get_SubTypeNames(self):
		return self.get_query_params().get('SubTypeNames')

	def set_SubTypeNames(self,SubTypeNames):
		self.add_query_param('SubTypeNames',SubTypeNames)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)