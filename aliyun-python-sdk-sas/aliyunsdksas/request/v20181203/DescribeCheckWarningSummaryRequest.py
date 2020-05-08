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
from aliyunsdksas.endpoint import endpoint_data

class DescribeCheckWarningSummaryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeCheckWarningSummary','sas')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RiskName(self):
		return self.get_query_params().get('RiskName')

	def set_RiskName(self,RiskName):
		self.add_query_param('RiskName',RiskName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_RiskStatus(self):
		return self.get_query_params().get('RiskStatus')

	def set_RiskStatus(self,RiskStatus):
		self.add_query_param('RiskStatus',RiskStatus)

	def get_StrategyId(self):
		return self.get_query_params().get('StrategyId')

	def set_StrategyId(self,StrategyId):
		self.add_query_param('StrategyId',StrategyId)

	def get_TypeName(self):
		return self.get_query_params().get('TypeName')

	def set_TypeName(self,TypeName):
		self.add_query_param('TypeName',TypeName)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)