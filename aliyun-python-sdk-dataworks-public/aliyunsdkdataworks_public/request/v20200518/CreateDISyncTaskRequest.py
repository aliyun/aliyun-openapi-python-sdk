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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateDISyncTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateDISyncTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskType(self): # String
		return self.get_query_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_query_param('TaskType', TaskType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TaskParam(self): # String
		return self.get_query_params().get('TaskParam')

	def set_TaskParam(self, TaskParam):  # String
		self.add_query_param('TaskParam', TaskParam)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_TaskContent(self): # String
		return self.get_body_params().get('TaskContent')

	def set_TaskContent(self, TaskContent):  # String
		self.add_body_params('TaskContent', TaskContent)
	def get_ProjectId(self): # Long
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_query_param('ProjectId', ProjectId)
