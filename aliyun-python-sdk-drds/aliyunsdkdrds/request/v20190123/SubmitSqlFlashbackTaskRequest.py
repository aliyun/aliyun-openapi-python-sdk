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

class SubmitSqlFlashbackTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SubmitSqlFlashbackTask','drds')

	def get_TraceId(self):
		return self.get_query_params().get('TraceId')

	def set_TraceId(self,TraceId):
		self.add_query_param('TraceId',TraceId)

	def get_SqlType(self):
		return self.get_query_params().get('SqlType')

	def set_SqlType(self,SqlType):
		self.add_query_param('SqlType',SqlType)

	def get_SqlPk(self):
		return self.get_query_params().get('SqlPk')

	def set_SqlPk(self,SqlPk):
		self.add_query_param('SqlPk',SqlPk)

	def get_RecallRestoreType(self):
		return self.get_query_params().get('RecallRestoreType')

	def set_RecallRestoreType(self,RecallRestoreType):
		self.add_query_param('RecallRestoreType',RecallRestoreType)

	def get_RecallType(self):
		return self.get_query_params().get('RecallType')

	def set_RecallType(self,RecallType):
		self.add_query_param('RecallType',RecallType)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)