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
class ExportOssResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'ExportOssResult','green')

	def get_TotalCount(self):
		return self.get_query_params().get('TotalCount')

	def set_TotalCount(self,TotalCount):
		self.add_query_param('TotalCount',TotalCount)

	def get_MinScore(self):
		return self.get_query_params().get('MinScore')

	def set_MinScore(self,MinScore):
		self.add_query_param('MinScore',MinScore)

	def get_Suggestion(self):
		return self.get_query_params().get('Suggestion')

	def set_Suggestion(self,Suggestion):
		self.add_query_param('Suggestion',Suggestion)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_MaxScore(self):
		return self.get_query_params().get('MaxScore')

	def set_MaxScore(self,MaxScore):
		self.add_query_param('MaxScore',MaxScore)

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

	def get_Bucket(self):
		return self.get_query_params().get('Bucket')

	def set_Bucket(self,Bucket):
		self.add_query_param('Bucket',Bucket)

	def get_EndDate(self):
		return self.get_query_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_query_param('EndDate',EndDate)

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

	def get_Stock(self):
		return self.get_query_params().get('Stock')

	def set_Stock(self,Stock):
		self.add_query_param('Stock',Stock)