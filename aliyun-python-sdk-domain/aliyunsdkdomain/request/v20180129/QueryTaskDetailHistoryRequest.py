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


class QueryTaskDetailHistoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryTaskDetailHistory')

	def get_TaskStatus(self):
		return self.get_query_params().get('TaskStatus')

	def set_TaskStatus(self,TaskStatus):
		self.add_query_param('TaskStatus',TaskStatus)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_TaskNo(self):
		return self.get_query_params().get('TaskNo')

	def set_TaskNo(self,TaskNo):
		self.add_query_param('TaskNo',TaskNo)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TaskDetailNoCursor(self):
		return self.get_query_params().get('TaskDetailNoCursor')

	def set_TaskDetailNoCursor(self,TaskDetailNoCursor):
		self.add_query_param('TaskDetailNoCursor',TaskDetailNoCursor)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_DomainNameCursor(self):
		return self.get_query_params().get('DomainNameCursor')

	def set_DomainNameCursor(self,DomainNameCursor):
		self.add_query_param('DomainNameCursor',DomainNameCursor)