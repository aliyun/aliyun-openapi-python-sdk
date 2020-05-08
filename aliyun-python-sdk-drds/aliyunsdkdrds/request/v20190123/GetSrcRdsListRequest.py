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

class GetSrcRdsListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'GetSrcRdsList','drds')

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_PartitionMappings(self):
		return self.get_query_params().get('PartitionMappings')

	def set_PartitionMappings(self,PartitionMappings):
		for i in range(len(PartitionMappings)):	
			if PartitionMappings[i].get('DbShardValue') is not None:
				self.add_query_param('PartitionMapping.' + str(i + 1) + '.DbShardValue' , PartitionMappings[i].get('DbShardValue'))
			if PartitionMappings[i].get('HotDbName') is not None:
				self.add_query_param('PartitionMapping.' + str(i + 1) + '.HotDbName' , PartitionMappings[i].get('HotDbName'))
			if PartitionMappings[i].get('HotTableName') is not None:
				self.add_query_param('PartitionMapping.' + str(i + 1) + '.HotTableName' , PartitionMappings[i].get('HotTableName'))
			if PartitionMappings[i].get('TbShardValue') is not None:
				self.add_query_param('PartitionMapping.' + str(i + 1) + '.TbShardValue' , PartitionMappings[i].get('TbShardValue'))
			if PartitionMappings[i].get('LogicTable') is not None:
				self.add_query_param('PartitionMapping.' + str(i + 1) + '.LogicTable' , PartitionMappings[i].get('LogicTable'))


	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)