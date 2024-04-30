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
from aliyunsdkrds.endpoint import endpoint_data

class DescribeHistoryEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeHistoryEvents','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventId(self): # String
		return self.get_query_params().get('EventId')

	def set_EventId(self, EventId):  # String
		self.add_query_param('EventId', EventId)
	def get_ToStartTime(self): # String
		return self.get_query_params().get('ToStartTime')

	def set_ToStartTime(self, ToStartTime):  # String
		self.add_query_param('ToStartTime', ToStartTime)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_FromStartTime(self): # String
		return self.get_query_params().get('FromStartTime')

	def set_FromStartTime(self, FromStartTime):  # String
		self.add_query_param('FromStartTime', FromStartTime)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_ArchiveStatus(self): # String
		return self.get_query_params().get('ArchiveStatus')

	def set_ArchiveStatus(self, ArchiveStatus):  # String
		self.add_query_param('ArchiveStatus', ArchiveStatus)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_EventLevel(self): # String
		return self.get_query_params().get('EventLevel')

	def set_EventLevel(self, EventLevel):  # String
		self.add_query_param('EventLevel', EventLevel)
	def get_EventCategory(self): # String
		return self.get_query_params().get('EventCategory')

	def set_EventCategory(self, EventCategory):  # String
		self.add_query_param('EventCategory', EventCategory)
	def get_EventType(self): # String
		return self.get_query_params().get('EventType')

	def set_EventType(self, EventType):  # String
		self.add_query_param('EventType', EventType)
	def get_EventStatus(self): # String
		return self.get_query_params().get('EventStatus')

	def set_EventStatus(self, EventStatus):  # String
		self.add_query_param('EventStatus', EventStatus)
