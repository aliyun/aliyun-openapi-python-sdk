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
class ExportSuspEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'ExportSuspEvents','vipaegis')

	def get_TimeEnd(self):
		return self.get_query_params().get('TimeEnd')

	def set_TimeEnd(self,TimeEnd):
		self.add_query_param('TimeEnd',TimeEnd)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Dealed(self):
		return self.get_query_params().get('Dealed')

	def set_Dealed(self,Dealed):
		self.add_query_param('Dealed',Dealed)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get__From(self):
		return self.get_query_params().get('From')

	def set__From(self,_From):
		self.add_query_param('From',_From)

	def get_TimeStart(self):
		return self.get_query_params().get('TimeStart')

	def set_TimeStart(self,TimeStart):
		self.add_query_param('TimeStart',TimeStart)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

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