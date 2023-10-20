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

class ExportSuspEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ExportSuspEvents','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeEnd(self): # String
		return self.get_query_params().get('TimeEnd')

	def set_TimeEnd(self, TimeEnd):  # String
		self.add_query_param('TimeEnd', TimeEnd)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_ContainerFieldName(self): # String
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self, ContainerFieldName):  # String
		self.add_query_param('ContainerFieldName', ContainerFieldName)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_ContainerFieldValue(self): # String
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self, ContainerFieldValue):  # String
		self.add_query_param('ContainerFieldValue', ContainerFieldValue)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_From(self): # String
		return self.get_query_params().get('From')

	def set_From(self, _From):  # String
		self.add_query_param('From', _From)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_UniqueInfo(self): # String
		return self.get_query_params().get('UniqueInfo')

	def set_UniqueInfo(self, UniqueInfo):  # String
		self.add_query_param('UniqueInfo', UniqueInfo)
	def get_Dealed(self): # String
		return self.get_query_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_query_param('Dealed', Dealed)
	def get_CurrentPage(self): # String
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # String
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_OperateErrorCodeLists(self): # RepeatList
		return self.get_query_params().get('OperateErrorCodeList')

	def set_OperateErrorCodeLists(self, OperateErrorCodeList):  # RepeatList
		for depth1 in range(len(OperateErrorCodeList)):
			self.add_query_param('OperateErrorCodeList.' + str(depth1 + 1), OperateErrorCodeList[depth1])
	def get_AssetsTypeLists(self): # RepeatList
		return self.get_query_params().get('AssetsTypeList')

	def set_AssetsTypeLists(self, AssetsTypeList):  # RepeatList
		for depth1 in range(len(AssetsTypeList)):
			self.add_query_param('AssetsTypeList.' + str(depth1 + 1), AssetsTypeList[depth1])
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_TimeStart(self): # String
		return self.get_query_params().get('TimeStart')

	def set_TimeStart(self, TimeStart):  # String
		self.add_query_param('TimeStart', TimeStart)
	def get_Levels(self): # String
		return self.get_query_params().get('Levels')

	def set_Levels(self, Levels):  # String
		self.add_query_param('Levels', Levels)
	def get_ParentEventTypes(self): # String
		return self.get_query_params().get('ParentEventTypes')

	def set_ParentEventTypes(self, ParentEventTypes):  # String
		self.add_query_param('ParentEventTypes', ParentEventTypes)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
