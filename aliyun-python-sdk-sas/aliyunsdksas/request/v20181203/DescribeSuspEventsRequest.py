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
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeSuspEvents','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TargetType(self):
		return self.get_query_params().get('TargetType')

	def set_TargetType(self,TargetType):
		self.add_query_param('TargetType',TargetType)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_ContainerFieldName(self):
		return self.get_query_params().get('ContainerFieldName')

	def set_ContainerFieldName(self,ContainerFieldName):
		self.add_query_param('ContainerFieldName',ContainerFieldName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ContainerFieldValue(self):
		return self.get_query_params().get('ContainerFieldValue')

	def set_ContainerFieldValue(self,ContainerFieldValue):
		self.add_query_param('ContainerFieldValue',ContainerFieldValue)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_From(self):
		return self.get_query_params().get('From')

	def set_From(self,_From):
		self.add_query_param('From',_From)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_AlarmUniqueInfo(self):
		return self.get_query_params().get('AlarmUniqueInfo')

	def set_AlarmUniqueInfo(self,AlarmUniqueInfo):
		self.add_query_param('AlarmUniqueInfo',AlarmUniqueInfo)

	def get_UniqueInfo(self):
		return self.get_query_params().get('UniqueInfo')

	def set_UniqueInfo(self,UniqueInfo):
		self.add_query_param('UniqueInfo',UniqueInfo)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_OperateErrorCodeLists(self):
		return self.get_query_params().get('OperateErrorCodeList')

	def set_OperateErrorCodeLists(self, OperateErrorCodeLists):
		for depth1 in range(len(OperateErrorCodeLists)):
			if OperateErrorCodeLists[depth1] is not None:
				self.add_query_param('OperateErrorCodeList.' + str(depth1 + 1) , OperateErrorCodeLists[depth1])

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Levels(self):
		return self.get_query_params().get('Levels')

	def set_Levels(self,Levels):
		self.add_query_param('Levels',Levels)

	def get_ParentEventTypes(self):
		return self.get_query_params().get('ParentEventTypes')

	def set_ParentEventTypes(self,ParentEventTypes):
		self.add_query_param('ParentEventTypes',ParentEventTypes)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)