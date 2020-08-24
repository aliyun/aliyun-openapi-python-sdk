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

class CreateDevopsProjectTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'CreateDevopsProjectTask')
		self.set_method('POST')

	def get_Note(self):
		return self.get_body_params().get('Note')

	def set_Note(self,Note):
		self.add_body_params('Note', Note)

	def get_Visible(self):
		return self.get_body_params().get('Visible')

	def set_Visible(self,Visible):
		self.add_body_params('Visible', Visible)

	def get_ExecutorId(self):
		return self.get_body_params().get('ExecutorId')

	def set_ExecutorId(self,ExecutorId):
		self.add_body_params('ExecutorId', ExecutorId)

	def get_TaskFlowStatusId(self):
		return self.get_body_params().get('TaskFlowStatusId')

	def set_TaskFlowStatusId(self,TaskFlowStatusId):
		self.add_body_params('TaskFlowStatusId', TaskFlowStatusId)

	def get_StartDate(self):
		return self.get_body_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_body_params('StartDate', StartDate)

	def get_Priority(self):
		return self.get_body_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_body_params('Priority', Priority)

	def get_ParentTaskId(self):
		return self.get_body_params().get('ParentTaskId')

	def set_ParentTaskId(self,ParentTaskId):
		self.add_body_params('ParentTaskId', ParentTaskId)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_SprintId(self):
		return self.get_body_params().get('SprintId')

	def set_SprintId(self,SprintId):
		self.add_body_params('SprintId', SprintId)

	def get_DueDate(self):
		return self.get_body_params().get('DueDate')

	def set_DueDate(self,DueDate):
		self.add_body_params('DueDate', DueDate)

	def get_ScenarioFieldConfigId(self):
		return self.get_body_params().get('ScenarioFieldConfigId')

	def set_ScenarioFieldConfigId(self,ScenarioFieldConfigId):
		self.add_body_params('ScenarioFieldConfigId', ScenarioFieldConfigId)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_TaskListId(self):
		return self.get_body_params().get('TaskListId')

	def set_TaskListId(self,TaskListId):
		self.add_body_params('TaskListId', TaskListId)