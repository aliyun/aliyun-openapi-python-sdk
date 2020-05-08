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
class QueryHotlineRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ccs', '2017-10-01', 'QueryHotlineRecord','ccs')

	def get_AgentId(self):
		return self.get_query_params().get('AgentId')

	def set_AgentId(self,AgentId):
		self.add_query_param('AgentId',AgentId)

	def get_MaxTalkDuration(self):
		return self.get_query_params().get('MaxTalkDuration')

	def set_MaxTalkDuration(self,MaxTalkDuration):
		self.add_query_param('MaxTalkDuration',MaxTalkDuration)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_Satisfaction(self):
		return self.get_query_params().get('Satisfaction')

	def set_Satisfaction(self,Satisfaction):
		self.add_query_param('Satisfaction',Satisfaction)

	def get_MinTalkDuratoin(self):
		return self.get_query_params().get('MinTalkDuratoin')

	def set_MinTalkDuratoin(self,MinTalkDuratoin):
		self.add_query_param('MinTalkDuratoin',MinTalkDuratoin)

	def get_CategoryIds(self):
		return self.get_query_params().get('CategoryIds')

	def set_CategoryIds(self,CategoryIds):
		self.add_query_param('CategoryIds',CategoryIds)

	def get_VisitorProvince(self):
		return self.get_query_params().get('VisitorProvince')

	def set_VisitorProvince(self,VisitorProvince):
		self.add_query_param('VisitorProvince',VisitorProvince)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CallType(self):
		return self.get_query_params().get('CallType')

	def set_CallType(self,CallType):
		self.add_query_param('CallType',CallType)

	def get_CcsInstanceId(self):
		return self.get_query_params().get('CcsInstanceId')

	def set_CcsInstanceId(self,CcsInstanceId):
		self.add_query_param('CcsInstanceId',CcsInstanceId)

	def get_VisitorPhone(self):
		return self.get_query_params().get('VisitorPhone')

	def set_VisitorPhone(self,VisitorPhone):
		self.add_query_param('VisitorPhone',VisitorPhone)

	def get_VisitorId(self):
		return self.get_query_params().get('VisitorId')

	def set_VisitorId(self,VisitorId):
		self.add_query_param('VisitorId',VisitorId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)