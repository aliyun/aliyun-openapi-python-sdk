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

class SubmitHotExpandTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SubmitHotExpandTask','drds')

	def get_InstanceDbMappings(self):
		return self.get_query_params().get('InstanceDbMappings')

	def set_InstanceDbMappings(self,InstanceDbMappings):
		for i in range(len(InstanceDbMappings)):	
			if InstanceDbMappings[i].get('DbList') is not None:
				self.add_query_param('InstanceDbMapping.' + str(i + 1) + '.DbList' , InstanceDbMappings[i].get('DbList'))
			if InstanceDbMappings[i].get('InstanceName') is not None:
				self.add_query_param('InstanceDbMapping.' + str(i + 1) + '.InstanceName' , InstanceDbMappings[i].get('InstanceName'))


	def get_Mappings(self):
		return self.get_query_params().get('Mappings')

	def set_Mappings(self,Mappings):
		for i in range(len(Mappings)):	
			if Mappings[i].get('DbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.DbShardColumn' , Mappings[i].get('DbShardColumn'))
			if Mappings[i].get('TbShardColumn') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.TbShardColumn' , Mappings[i].get('TbShardColumn'))
			if Mappings[i].get('ShardTbValue') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.ShardTbValue' , Mappings[i].get('ShardTbValue'))
			if Mappings[i].get('HotDbName') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.HotDbName' , Mappings[i].get('HotDbName'))
			if Mappings[i].get('ShardDbValue') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.ShardDbValue' , Mappings[i].get('ShardDbValue'))
			if Mappings[i].get('HotTableName') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.HotTableName' , Mappings[i].get('HotTableName'))
			if Mappings[i].get('LogicTable') is not None:
				self.add_query_param('Mapping.' + str(i + 1) + '.LogicTable' , Mappings[i].get('LogicTable'))


	def get_TaskDesc(self):
		return self.get_query_params().get('TaskDesc')

	def set_TaskDesc(self,TaskDesc):
		self.add_query_param('TaskDesc',TaskDesc)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_SupperAccountMappings(self):
		return self.get_query_params().get('SupperAccountMappings')

	def set_SupperAccountMappings(self,SupperAccountMappings):
		for i in range(len(SupperAccountMappings)):	
			if SupperAccountMappings[i].get('InstanceName') is not None:
				self.add_query_param('SupperAccountMapping.' + str(i + 1) + '.InstanceName' , SupperAccountMappings[i].get('InstanceName'))
			if SupperAccountMappings[i].get('SupperAccount') is not None:
				self.add_query_param('SupperAccountMapping.' + str(i + 1) + '.SupperAccount' , SupperAccountMappings[i].get('SupperAccount'))
			if SupperAccountMappings[i].get('SupperPassword') is not None:
				self.add_query_param('SupperAccountMapping.' + str(i + 1) + '.SupperPassword' , SupperAccountMappings[i].get('SupperPassword'))


	def get_ExtendedMappings(self):
		return self.get_query_params().get('ExtendedMappings')

	def set_ExtendedMappings(self,ExtendedMappings):
		for i in range(len(ExtendedMappings)):	
			if ExtendedMappings[i].get('SrcInstanceId') is not None:
				self.add_query_param('ExtendedMapping.' + str(i + 1) + '.SrcInstanceId' , ExtendedMappings[i].get('SrcInstanceId'))
			if ExtendedMappings[i].get('SrcDb') is not None:
				self.add_query_param('ExtendedMapping.' + str(i + 1) + '.SrcDb' , ExtendedMappings[i].get('SrcDb'))


	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)