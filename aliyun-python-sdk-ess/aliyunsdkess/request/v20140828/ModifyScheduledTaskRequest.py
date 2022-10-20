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
from aliyunsdkess.endpoint import endpoint_data

class ModifyScheduledTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyScheduledTask','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ScheduledAction(self): # String
		return self.get_query_params().get('ScheduledAction')

	def set_ScheduledAction(self, ScheduledAction):  # String
		self.add_query_param('ScheduledAction', ScheduledAction)
	def get_MaxValue(self): # Integer
		return self.get_query_params().get('MaxValue')

	def set_MaxValue(self, MaxValue):  # Integer
		self.add_query_param('MaxValue', MaxValue)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RecurrenceEndTime(self): # String
		return self.get_query_params().get('RecurrenceEndTime')

	def set_RecurrenceEndTime(self, RecurrenceEndTime):  # String
		self.add_query_param('RecurrenceEndTime', RecurrenceEndTime)
	def get_LaunchTime(self): # String
		return self.get_query_params().get('LaunchTime')

	def set_LaunchTime(self, LaunchTime):  # String
		self.add_query_param('LaunchTime', LaunchTime)
	def get_DesiredCapacity(self): # Integer
		return self.get_query_params().get('DesiredCapacity')

	def set_DesiredCapacity(self, DesiredCapacity):  # Integer
		self.add_query_param('DesiredCapacity', DesiredCapacity)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_RecurrenceValue(self): # String
		return self.get_query_params().get('RecurrenceValue')

	def set_RecurrenceValue(self, RecurrenceValue):  # String
		self.add_query_param('RecurrenceValue', RecurrenceValue)
	def get_LaunchExpirationTime(self): # Integer
		return self.get_query_params().get('LaunchExpirationTime')

	def set_LaunchExpirationTime(self, LaunchExpirationTime):  # Integer
		self.add_query_param('LaunchExpirationTime', LaunchExpirationTime)
	def get_MinValue(self): # Integer
		return self.get_query_params().get('MinValue')

	def set_MinValue(self, MinValue):  # Integer
		self.add_query_param('MinValue', MinValue)
	def get_ScheduledTaskName(self): # String
		return self.get_query_params().get('ScheduledTaskName')

	def set_ScheduledTaskName(self, ScheduledTaskName):  # String
		self.add_query_param('ScheduledTaskName', ScheduledTaskName)
	def get_TaskEnabled(self): # Boolean
		return self.get_query_params().get('TaskEnabled')

	def set_TaskEnabled(self, TaskEnabled):  # Boolean
		self.add_query_param('TaskEnabled', TaskEnabled)
	def get_ScheduledTaskId(self): # String
		return self.get_query_params().get('ScheduledTaskId')

	def set_ScheduledTaskId(self, ScheduledTaskId):  # String
		self.add_query_param('ScheduledTaskId', ScheduledTaskId)
	def get_RecurrenceType(self): # String
		return self.get_query_params().get('RecurrenceType')

	def set_RecurrenceType(self, RecurrenceType):  # String
		self.add_query_param('RecurrenceType', RecurrenceType)
