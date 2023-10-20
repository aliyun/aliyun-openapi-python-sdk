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

class ListAgentlessTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListAgentlessTask','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InternetIp(self): # String
		return self.get_query_params().get('InternetIp')

	def set_InternetIp(self, InternetIp):  # String
		self.add_query_param('InternetIp', InternetIp)
	def get_TargetType(self): # Integer
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # Integer
		self.add_query_param('TargetType', TargetType)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_TargetName(self): # String
		return self.get_query_params().get('TargetName')

	def set_TargetName(self, TargetName):  # String
		self.add_query_param('TargetName', TargetName)
	def get_RootTaskId(self): # String
		return self.get_query_params().get('RootTaskId')

	def set_RootTaskId(self, RootTaskId):  # String
		self.add_query_param('RootTaskId', RootTaskId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_MachineName(self): # String
		return self.get_query_params().get('MachineName')

	def set_MachineName(self, MachineName):  # String
		self.add_query_param('MachineName', MachineName)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_RootTask(self): # Boolean
		return self.get_query_params().get('RootTask')

	def set_RootTask(self, RootTask):  # Boolean
		self.add_query_param('RootTask', RootTask)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
	def get_IntranetIp(self): # String
		return self.get_query_params().get('IntranetIp')

	def set_IntranetIp(self, IntranetIp):  # String
		self.add_query_param('IntranetIp', IntranetIp)
