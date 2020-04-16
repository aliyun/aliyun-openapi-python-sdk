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

class DescribeAlarmEventListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeAlarmEventList','sas')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AlarmEventType(self):
		return self.get_query_params().get('AlarmEventType')

	def set_AlarmEventType(self,AlarmEventType):
		self.add_query_param('AlarmEventType',AlarmEventType)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_AlarmEventName(self):
		return self.get_query_params().get('AlarmEventName')

	def set_AlarmEventName(self,AlarmEventName):
		self.add_query_param('AlarmEventName',AlarmEventName)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get__From(self):
		return self.get_query_params().get('From')

	def set__From(self,_From):
		self.add_query_param('From',_From)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

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

	def get_OperateErrorCodeLists(self):
		return self.get_query_params().get('OperateErrorCodeLists')

	def set_OperateErrorCodeLists(self,OperateErrorCodeLists):
		for i in range(len(OperateErrorCodeLists)):	
			if OperateErrorCodeLists[i] is not None:
				self.add_query_param('OperateErrorCodeList.' + str(i + 1) , OperateErrorCodeLists[i]);

	def get_Levels(self):
		return self.get_query_params().get('Levels')

	def set_Levels(self,Levels):
		self.add_query_param('Levels',Levels)