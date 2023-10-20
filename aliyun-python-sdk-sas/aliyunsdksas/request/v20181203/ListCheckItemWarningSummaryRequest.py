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

class ListCheckItemWarningSummaryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListCheckItemWarningSummary','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RiskType(self): # String
		return self.get_query_params().get('RiskType')

	def set_RiskType(self, RiskType):  # String
		self.add_query_param('RiskType', RiskType)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_ContainerFieldName(self): # String
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self, ContainerFieldName):  # String
		self.add_query_param('ContainerFieldName', ContainerFieldName)
	def get_CheckType(self): # String
		return self.get_query_params().get('CheckType')

	def set_CheckType(self, CheckType):  # String
		self.add_query_param('CheckType', CheckType)
	def get_ContainerFieldValue(self): # String
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self, ContainerFieldValue):  # String
		self.add_query_param('ContainerFieldValue', ContainerFieldValue)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_CheckWarningStatus(self): # Integer
		return self.get_query_params().get('CheckWarningStatus')

	def set_CheckWarningStatus(self, CheckWarningStatus):  # Integer
		self.add_query_param('CheckWarningStatus', CheckWarningStatus)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_CheckItemFuzzy(self): # String
		return self.get_query_params().get('CheckItemFuzzy')

	def set_CheckItemFuzzy(self, CheckItemFuzzy):  # String
		self.add_query_param('CheckItemFuzzy', CheckItemFuzzy)
	def get_CheckLevel(self): # String
		return self.get_query_params().get('CheckLevel')

	def set_CheckLevel(self, CheckLevel):  # String
		self.add_query_param('CheckLevel', CheckLevel)
