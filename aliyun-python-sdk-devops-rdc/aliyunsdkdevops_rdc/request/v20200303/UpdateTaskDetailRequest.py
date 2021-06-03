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

class UpdateTaskDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'UpdateTaskDetail')
		self.set_method('POST')

	def get_Note(self):
		return self.get_body_params().get('Note')

	def set_Note(self,Note):
		self.add_body_params('Note', Note)

	def get_ExecutorId(self):
		return self.get_body_params().get('ExecutorId')

	def set_ExecutorId(self,ExecutorId):
		self.add_body_params('ExecutorId', ExecutorId)

	def get_StartDate(self):
		return self.get_body_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_body_params('StartDate', StartDate)

	def get_DelInvolvers(self):
		return self.get_body_params().get('DelInvolvers')

	def set_DelInvolvers(self,DelInvolvers):
		self.add_body_params('DelInvolvers', DelInvolvers)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_SprintId(self):
		return self.get_body_params().get('SprintId')

	def set_SprintId(self,SprintId):
		self.add_body_params('SprintId', SprintId)

	def get_CustomFieldId(self):
		return self.get_body_params().get('CustomFieldId')

	def set_CustomFieldId(self,CustomFieldId):
		self.add_body_params('CustomFieldId', CustomFieldId)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_TaskId(self):
		return self.get_body_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_body_params('TaskId', TaskId)

	def get_TaskFlowStatusId(self):
		return self.get_body_params().get('TaskFlowStatusId')

	def set_TaskFlowStatusId(self,TaskFlowStatusId):
		self.add_body_params('TaskFlowStatusId', TaskFlowStatusId)

	def get_TagIds(self):
		return self.get_body_params().get('TagIds')

	def set_TagIds(self,TagIds):
		self.add_body_params('TagIds', TagIds)

	def get_AddInvolvers(self):
		return self.get_body_params().get('AddInvolvers')

	def set_AddInvolvers(self,AddInvolvers):
		self.add_body_params('AddInvolvers', AddInvolvers)

	def get_Priority(self):
		return self.get_body_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_body_params('Priority', Priority)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_DueDate(self):
		return self.get_body_params().get('DueDate')

	def set_DueDate(self,DueDate):
		self.add_body_params('DueDate', DueDate)

	def get_WorkTimes(self):
		return self.get_body_params().get('WorkTimes')

	def set_WorkTimes(self,WorkTimes):
		self.add_body_params('WorkTimes', WorkTimes)

	def get_StoryPoint(self):
		return self.get_body_params().get('StoryPoint')

	def set_StoryPoint(self,StoryPoint):
		self.add_body_params('StoryPoint', StoryPoint)

	def get_CustomFieldValues(self):
		return self.get_body_params().get('CustomFieldValues')

	def set_CustomFieldValues(self,CustomFieldValues):
		self.add_body_params('CustomFieldValues', CustomFieldValues)