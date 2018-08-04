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
class ModifyScheduledTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyScheduledTask','ess')

	def get_LaunchTime(self):
		return self.get_query_params().get('LaunchTime')

	def set_LaunchTime(self,LaunchTime):
		self.add_query_param('LaunchTime',LaunchTime)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ScheduledAction(self):
		return self.get_query_params().get('ScheduledAction')

	def set_ScheduledAction(self,ScheduledAction):
		self.add_query_param('ScheduledAction',ScheduledAction)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RecurrenceValue(self):
		return self.get_query_params().get('RecurrenceValue')

	def set_RecurrenceValue(self,RecurrenceValue):
		self.add_query_param('RecurrenceValue',RecurrenceValue)

	def get_LaunchExpirationTime(self):
		return self.get_query_params().get('LaunchExpirationTime')

	def set_LaunchExpirationTime(self,LaunchExpirationTime):
		self.add_query_param('LaunchExpirationTime',LaunchExpirationTime)

	def get_RecurrenceEndTime(self):
		return self.get_query_params().get('RecurrenceEndTime')

	def set_RecurrenceEndTime(self,RecurrenceEndTime):
		self.add_query_param('RecurrenceEndTime',RecurrenceEndTime)

	def get_ScheduledTaskName(self):
		return self.get_query_params().get('ScheduledTaskName')

	def set_ScheduledTaskName(self,ScheduledTaskName):
		self.add_query_param('ScheduledTaskName',ScheduledTaskName)

	def get_TaskEnabled(self):
		return self.get_query_params().get('TaskEnabled')

	def set_TaskEnabled(self,TaskEnabled):
		self.add_query_param('TaskEnabled',TaskEnabled)

	def get_ScheduledTaskId(self):
		return self.get_query_params().get('ScheduledTaskId')

	def set_ScheduledTaskId(self,ScheduledTaskId):
		self.add_query_param('ScheduledTaskId',ScheduledTaskId)

	def get_RecurrenceType(self):
		return self.get_query_params().get('RecurrenceType')

	def set_RecurrenceType(self,RecurrenceType):
		self.add_query_param('RecurrenceType',RecurrenceType)