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
from aliyunsdkdrds.endpoint import endpoint_data

class SubmitHotExpandTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SubmitHotExpandTask','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TaskDesc(self): # String
		return self.get_query_params().get('TaskDesc')

	def set_TaskDesc(self, TaskDesc):  # String
		self.add_query_param('TaskDesc', TaskDesc)
	def get_Mappings(self): # RepeatList
		return self.get_query_params().get('Mapping')

	def set_Mappings(self, Mapping):  # RepeatList
		for depth1 in range(len(Mapping)):
			if Mapping[depth1].get('TbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.TbShardColumn', Mapping[depth1].get('TbShardColumn'))
			if Mapping[depth1].get('DbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.DbShardColumn', Mapping[depth1].get('DbShardColumn'))
			if Mapping[depth1].get('ShardTbValue') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.ShardTbValue', Mapping[depth1].get('ShardTbValue'))
			if Mapping[depth1].get('HotDbName') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.HotDbName', Mapping[depth1].get('HotDbName'))
			if Mapping[depth1].get('ShardDbValue') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.ShardDbValue', Mapping[depth1].get('ShardDbValue'))
			if Mapping[depth1].get('HotTableName') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.HotTableName', Mapping[depth1].get('HotTableName'))
			if Mapping[depth1].get('LogicTable') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.LogicTable', Mapping[depth1].get('LogicTable'))
	def get_SupperAccountMappings(self): # RepeatList
		return self.get_query_params().get('SupperAccountMapping')

	def set_SupperAccountMappings(self, SupperAccountMapping):  # RepeatList
		for depth1 in range(len(SupperAccountMapping)):
			if SupperAccountMapping[depth1].get('InstanceName') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.InstanceName', SupperAccountMapping[depth1].get('InstanceName'))
			if SupperAccountMapping[depth1].get('SupperAccount') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.SupperAccount', SupperAccountMapping[depth1].get('SupperAccount'))
			if SupperAccountMapping[depth1].get('SupperPassword') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.SupperPassword', SupperAccountMapping[depth1].get('SupperPassword'))
	def get_ExtendedMappings(self): # RepeatList
		return self.get_query_params().get('ExtendedMapping')

	def set_ExtendedMappings(self, ExtendedMapping):  # RepeatList
		for depth1 in range(len(ExtendedMapping)):
			if ExtendedMapping[depth1].get('SrcInstanceId') is not None:
				self.add_query_param('ExtendedMapping.' + str(depth1 + 1) + '.SrcInstanceId', ExtendedMapping[depth1].get('SrcInstanceId'))
			if ExtendedMapping[depth1].get('SrcDb') is not None:
				self.add_query_param('ExtendedMapping.' + str(depth1 + 1) + '.SrcDb', ExtendedMapping[depth1].get('SrcDb'))
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
	def get_InstanceDbMappings(self): # RepeatList
		return self.get_query_params().get('InstanceDbMapping')

	def set_InstanceDbMappings(self, InstanceDbMapping):  # RepeatList
		for depth1 in range(len(InstanceDbMapping)):
			if InstanceDbMapping[depth1].get('DbList') is not None:
				self.add_query_param('InstanceDbMapping.' + str(depth1 + 1) + '.DbList', InstanceDbMapping[depth1].get('DbList'))
			if InstanceDbMapping[depth1].get('InstanceName') is not None:
				self.add_query_param('InstanceDbMapping.' + str(depth1 + 1) + '.InstanceName', InstanceDbMapping[depth1].get('InstanceName'))
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
