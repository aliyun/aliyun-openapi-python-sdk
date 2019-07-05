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
class DescribeAuditContentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'DescribeAuditContent','green')

	def get_TotalCount(self):
		return self.get_query_params().get('TotalCount')

	def set_TotalCount(self,TotalCount):
		self.add_query_param('TotalCount',TotalCount)

	def get_KeywordId(self):
		return self.get_query_params().get('KeywordId')

	def set_KeywordId(self,KeywordId):
		self.add_query_param('KeywordId',KeywordId)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_Suggestion(self):
		return self.get_query_params().get('Suggestion')

	def set_Suggestion(self,Suggestion):
		self.add_query_param('Suggestion',Suggestion)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Label(self):
		return self.get_query_params().get('Label')

	def set_Label(self,Label):
		self.add_query_param('Label',Label)

	def get_StartDate(self):
		return self.get_query_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_query_param('StartDate',StartDate)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_EndDate(self):
		return self.get_query_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_query_param('EndDate',EndDate)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_DataId(self):
		return self.get_query_params().get('DataId')

	def set_DataId(self,DataId):
		self.add_query_param('DataId',DataId)

	def get_LibType(self):
		return self.get_query_params().get('LibType')

	def set_LibType(self,LibType):
		self.add_query_param('LibType',LibType)

	def get_AuditResult(self):
		return self.get_query_params().get('AuditResult')

	def set_AuditResult(self,AuditResult):
		self.add_query_param('AuditResult',AuditResult)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)