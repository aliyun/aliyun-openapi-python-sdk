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


	def get_Mappings(self):
		return self.get_query_params().get('Mapping')

	def set_Mappings(self, Mappings):
		for depth1 in range(len(Mappings)):
			if Mappings[depth1].get('DbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.DbShardColumn', Mappings[depth1].get('DbShardColumn'))
			if Mappings[depth1].get('TbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.TbShardColumn', Mappings[depth1].get('TbShardColumn'))
			if Mappings[depth1].get('ShardTbValue') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.ShardTbValue', Mappings[depth1].get('ShardTbValue'))
			if Mappings[depth1].get('HotDbName') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.HotDbName', Mappings[depth1].get('HotDbName'))
			if Mappings[depth1].get('ShardDbValue') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.ShardDbValue', Mappings[depth1].get('ShardDbValue'))
			if Mappings[depth1].get('HotTableName') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.HotTableName', Mappings[depth1].get('HotTableName'))
			if Mappings[depth1].get('LogicTable') is not None:
				self.add_query_param('Mapping.' + str(depth1 + 1) + '.LogicTable', Mappings[depth1].get('LogicTable'))

	def get_TaskDesc(self):
		return self.get_query_params().get('TaskDesc')

	def set_TaskDesc(self,TaskDesc):
		self.add_query_param('TaskDesc',TaskDesc)

	def get_SupperAccountMappings(self):
		return self.get_query_params().get('SupperAccountMapping')

	def set_SupperAccountMappings(self, SupperAccountMappings):
		for depth1 in range(len(SupperAccountMappings)):
			if SupperAccountMappings[depth1].get('InstanceName') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.InstanceName', SupperAccountMappings[depth1].get('InstanceName'))
			if SupperAccountMappings[depth1].get('SupperAccount') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.SupperAccount', SupperAccountMappings[depth1].get('SupperAccount'))
			if SupperAccountMappings[depth1].get('SupperPassword') is not None:
				self.add_query_param('SupperAccountMapping.' + str(depth1 + 1) + '.SupperPassword', SupperAccountMappings[depth1].get('SupperPassword'))

	def get_ExtendedMappings(self):
		return self.get_query_params().get('ExtendedMapping')

	def set_ExtendedMappings(self, ExtendedMappings):
		for depth1 in range(len(ExtendedMappings)):
			if ExtendedMappings[depth1].get('SrcInstanceId') is not None:
				self.add_query_param('ExtendedMapping.' + str(depth1 + 1) + '.SrcInstanceId', ExtendedMappings[depth1].get('SrcInstanceId'))
			if ExtendedMappings[depth1].get('SrcDb') is not None:
				self.add_query_param('ExtendedMapping.' + str(depth1 + 1) + '.SrcDb', ExtendedMappings[depth1].get('SrcDb'))

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_InstanceDbMappings(self):
		return self.get_query_params().get('InstanceDbMapping')

	def set_InstanceDbMappings(self, InstanceDbMappings):
		for depth1 in range(len(InstanceDbMappings)):
			if InstanceDbMappings[depth1].get('DbList') is not None:
				self.add_query_param('InstanceDbMapping.' + str(depth1 + 1) + '.DbList', InstanceDbMappings[depth1].get('DbList'))
			if InstanceDbMappings[depth1].get('InstanceName') is not None:
				self.add_query_param('InstanceDbMapping.' + str(depth1 + 1) + '.InstanceName', InstanceDbMappings[depth1].get('InstanceName'))

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)