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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeInstanceHistoryEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInstanceHistoryEvents','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventIds(self): # RepeatList
		return self.get_query_params().get('EventId')

	def set_EventIds(self, EventId):  # RepeatList
		for depth1 in range(len(EventId)):
			self.add_query_param('EventId.' + str(depth1 + 1), EventId[depth1])
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_EventCycleStatus(self): # String
		return self.get_query_params().get('EventCycleStatus')

	def set_EventCycleStatus(self, EventCycleStatus):  # String
		self.add_query_param('EventCycleStatus', EventCycleStatus)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ImpactLevel(self): # String
		return self.get_query_params().get('ImpactLevel')

	def set_ImpactLevel(self, ImpactLevel):  # String
		self.add_query_param('ImpactLevel', ImpactLevel)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_InstanceEventCycleStatuss(self): # RepeatList
		return self.get_query_params().get('InstanceEventCycleStatus')

	def set_InstanceEventCycleStatuss(self, InstanceEventCycleStatus):  # RepeatList
		for depth1 in range(len(InstanceEventCycleStatus)):
			self.add_query_param('InstanceEventCycleStatus.' + str(depth1 + 1), InstanceEventCycleStatus[depth1])
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_EventPublishTimeEnd(self): # String
		return self.get_query_params().get('EventPublishTime.End')

	def set_EventPublishTimeEnd(self, EventPublishTimeEnd):  # String
		self.add_query_param('EventPublishTime.End', EventPublishTimeEnd)
	def get_ResourceIds(self): # RepeatList
		return self.get_query_params().get('ResourceId')

	def set_ResourceIds(self, ResourceId):  # RepeatList
		for depth1 in range(len(ResourceId)):
			self.add_query_param('ResourceId.' + str(depth1 + 1), ResourceId[depth1])
	def get_InstanceEventTypes(self): # RepeatList
		return self.get_query_params().get('InstanceEventType')

	def set_InstanceEventTypes(self, InstanceEventType):  # RepeatList
		for depth1 in range(len(InstanceEventType)):
			self.add_query_param('InstanceEventType.' + str(depth1 + 1), InstanceEventType[depth1])
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_NotBeforeStart(self): # String
		return self.get_query_params().get('NotBefore.Start')

	def set_NotBeforeStart(self, NotBeforeStart):  # String
		self.add_query_param('NotBefore.Start', NotBeforeStart)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_EventPublishTimeStart(self): # String
		return self.get_query_params().get('EventPublishTime.Start')

	def set_EventPublishTimeStart(self, EventPublishTimeStart):  # String
		self.add_query_param('EventPublishTime.Start', EventPublishTimeStart)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NotBeforeEnd(self): # String
		return self.get_query_params().get('NotBefore.End')

	def set_NotBeforeEnd(self, NotBeforeEnd):  # String
		self.add_query_param('NotBefore.End', NotBeforeEnd)
	def get_EventType(self): # String
		return self.get_query_params().get('EventType')

	def set_EventType(self, EventType):  # String
		self.add_query_param('EventType', EventType)
