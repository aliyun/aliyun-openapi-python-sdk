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

class DescribeProcessTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescribeProcessTasks')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_EntityName(self): # String
		return self.get_query_params().get('EntityName')

	def set_EntityName(self, EntityName):  # String
		self.add_query_param('EntityName', EntityName)
	def get_YunCode(self): # String
		return self.get_query_params().get('YunCode')

	def set_YunCode(self, YunCode):  # String
		self.add_query_param('YunCode', YunCode)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_TaskStatus(self): # String
		return self.get_query_params().get('TaskStatus')

	def set_TaskStatus(self, TaskStatus):  # String
		self.add_query_param('TaskStatus', TaskStatus)
	def get_ProcessRemoveEnd(self): # Long
		return self.get_query_params().get('ProcessRemoveEnd')

	def set_ProcessRemoveEnd(self, ProcessRemoveEnd):  # Long
		self.add_query_param('ProcessRemoveEnd', ProcessRemoveEnd)
	def get_ParamContent(self): # String
		return self.get_query_params().get('ParamContent')

	def set_ParamContent(self, ParamContent):  # String
		self.add_query_param('ParamContent', ParamContent)
	def get_Scope(self): # String
		return self.get_query_params().get('Scope')

	def set_Scope(self, Scope):  # String
		self.add_query_param('Scope', Scope)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TriggerSource(self): # String
		return self.get_query_params().get('TriggerSource')

	def set_TriggerSource(self, TriggerSource):  # String
		self.add_query_param('TriggerSource', TriggerSource)
	def get_ProcessRemoveStart(self): # Long
		return self.get_query_params().get('ProcessRemoveStart')

	def set_ProcessRemoveStart(self, ProcessRemoveStart):  # Long
		self.add_query_param('ProcessRemoveStart', ProcessRemoveStart)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_OrderField(self): # String
		return self.get_query_params().get('OrderField')

	def set_OrderField(self, OrderField):  # String
		self.add_query_param('OrderField', OrderField)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_SceneCode(self): # String
		return self.get_query_params().get('SceneCode')

	def set_SceneCode(self, SceneCode):  # String
		self.add_query_param('SceneCode', SceneCode)
	def get_ProcessActionStart(self): # Long
		return self.get_query_params().get('ProcessActionStart')

	def set_ProcessActionStart(self, ProcessActionStart):  # Long
		self.add_query_param('ProcessActionStart', ProcessActionStart)
	def get_ProcessActionEnd(self): # Long
		return self.get_query_params().get('ProcessActionEnd')

	def set_ProcessActionEnd(self, ProcessActionEnd):  # Long
		self.add_query_param('ProcessActionEnd', ProcessActionEnd)
	def get_ProcessStrategyUuid(self): # String
		return self.get_query_params().get('ProcessStrategyUuid')

	def set_ProcessStrategyUuid(self, ProcessStrategyUuid):  # String
		self.add_query_param('ProcessStrategyUuid', ProcessStrategyUuid)
	def get_EntityType(self): # String
		return self.get_query_params().get('EntityType')

	def set_EntityType(self, EntityType):  # String
		self.add_query_param('EntityType', EntityType)
	def get_EntityUuid(self): # String
		return self.get_query_params().get('EntityUuid')

	def set_EntityUuid(self, EntityUuid):  # String
		self.add_query_param('EntityUuid', EntityUuid)
	def get_EventUuid(self): # String
		return self.get_query_params().get('EventUuid')

	def set_EventUuid(self, EventUuid):  # String
		self.add_query_param('EventUuid', EventUuid)
