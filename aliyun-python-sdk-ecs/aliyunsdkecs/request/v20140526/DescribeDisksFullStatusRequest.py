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
class DescribeDisksFullStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeDisksFullStatus','ecs')

	def get_EventIds(self):
		return self.get_query_params().get('EventIds')

	def set_EventIds(self,EventIds):
		for i in range(len(EventIds)):	
			if EventIds[i] is not None:
				self.add_query_param('EventId.' + str(i + 1) , EventIds[i]);

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_EventTimeStart(self):
		return self.get_query_params().get('EventTime.Start')

	def set_EventTimeStart(self,EventTimeStart):
		self.add_query_param('EventTime.Start',EventTimeStart)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DiskIds(self):
		return self.get_query_params().get('DiskIds')

	def set_DiskIds(self,DiskIds):
		for i in range(len(DiskIds)):	
			if DiskIds[i] is not None:
				self.add_query_param('DiskId.' + str(i + 1) , DiskIds[i]);

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_EventTimeEnd(self):
		return self.get_query_params().get('EventTime.End')

	def set_EventTimeEnd(self,EventTimeEnd):
		self.add_query_param('EventTime.End',EventTimeEnd)

	def get_HealthStatus(self):
		return self.get_query_params().get('HealthStatus')

	def set_HealthStatus(self,HealthStatus):
		self.add_query_param('HealthStatus',HealthStatus)

	def get_EventType(self):
		return self.get_query_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_query_param('EventType',EventType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)