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
class TaskConfigCreateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'TaskConfigCreate','cms')

	def get_InstanceLists(self):
		return self.get_query_params().get('InstanceLists')

	def set_InstanceLists(self,InstanceLists):
		for i in range(len(InstanceLists)):	
			if InstanceLists[i] is not None:
				self.add_query_param('InstanceList.' + str(i + 1) , InstanceLists[i]);

	def get_JsonData(self):
		return self.get_query_params().get('JsonData')

	def set_JsonData(self,JsonData):
		self.add_query_param('JsonData',JsonData)

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_TaskScope(self):
		return self.get_query_params().get('TaskScope')

	def set_TaskScope(self,TaskScope):
		self.add_query_param('TaskScope',TaskScope)

	def get_AlertConfig(self):
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfig(self,AlertConfig):
		self.add_query_param('AlertConfig',AlertConfig)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_GroupName(self):
		return self.get_query_params().get('GroupName')

	def set_GroupName(self,GroupName):
		self.add_query_param('GroupName',GroupName)