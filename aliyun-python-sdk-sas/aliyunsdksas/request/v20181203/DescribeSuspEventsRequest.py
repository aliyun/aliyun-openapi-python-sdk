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

class DescribeSuspEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeSuspEvents')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_ContainerFieldName(self): # String
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self, ContainerFieldName):  # String
		self.add_query_param('ContainerFieldName', ContainerFieldName)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_EventNames(self): # String
		return self.get_query_params().get('EventNames')

	def set_EventNames(self, EventNames):  # String
		self.add_query_param('EventNames', EventNames)
	def get_From(self): # String
		return self.get_query_params().get('From')

	def set_From(self, _From):  # String
		self.add_query_param('From', _From)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_TacticId(self): # String
		return self.get_body_params().get('TacticId')

	def set_TacticId(self, TacticId):  # String
		self.add_body_params('TacticId', TacticId)
	def get_AlarmUniqueInfo(self): # String
		return self.get_query_params().get('AlarmUniqueInfo')

	def set_AlarmUniqueInfo(self, AlarmUniqueInfo):  # String
		self.add_query_param('AlarmUniqueInfo', AlarmUniqueInfo)
	def get_UniqueInfo(self): # String
		return self.get_query_params().get('UniqueInfo')

	def set_UniqueInfo(self, UniqueInfo):  # String
		self.add_query_param('UniqueInfo', UniqueInfo)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_OperateTimeEnd(self): # String
		return self.get_query_params().get('OperateTimeEnd')

	def set_OperateTimeEnd(self, OperateTimeEnd):  # String
		self.add_query_param('OperateTimeEnd', OperateTimeEnd)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_Uuids(self): # String
		return self.get_query_params().get('Uuids')

	def set_Uuids(self, Uuids):  # String
		self.add_query_param('Uuids', Uuids)
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
	def get_ContainerFieldValue(self): # String
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self, ContainerFieldValue):  # String
		self.add_query_param('ContainerFieldValue', ContainerFieldValue)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
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
	def get_OperateTimeStart(self): # String
		return self.get_query_params().get('OperateTimeStart')

	def set_OperateTimeStart(self, OperateTimeStart):  # String
		self.add_query_param('OperateTimeStart', OperateTimeStart)
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
