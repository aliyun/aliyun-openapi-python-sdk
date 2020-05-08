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
from aliyunsdkemr.endpoint import endpoint_data

class MetastoreUpdateTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'MetastoreUpdateTable','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AddColumns(self):
		return self.get_query_params().get('AddColumns')

	def set_AddColumns(self,AddColumns):
		for i in range(len(AddColumns)):	
			if AddColumns[i].get('Name') is not None:
				self.add_query_param('AddColumn.' + str(i + 1) + '.Name' , AddColumns[i].get('Name'))
			if AddColumns[i].get('Comment') is not None:
				self.add_query_param('AddColumn.' + str(i + 1) + '.Comment' , AddColumns[i].get('Comment'))
			if AddColumns[i].get('Type') is not None:
				self.add_query_param('AddColumn.' + str(i + 1) + '.Type' , AddColumns[i].get('Type'))


	def get_AddPartitions(self):
		return self.get_query_params().get('AddPartitions')

	def set_AddPartitions(self,AddPartitions):
		for i in range(len(AddPartitions)):	
			if AddPartitions[i].get('Name') is not None:
				self.add_query_param('AddPartition.' + str(i + 1) + '.Name' , AddPartitions[i].get('Name'))
			if AddPartitions[i].get('Comment') is not None:
				self.add_query_param('AddPartition.' + str(i + 1) + '.Comment' , AddPartitions[i].get('Comment'))
			if AddPartitions[i].get('Type') is not None:
				self.add_query_param('AddPartition.' + str(i + 1) + '.Type' , AddPartitions[i].get('Type'))


	def get_DeleteColumnNames(self):
		return self.get_query_params().get('DeleteColumnNames')

	def set_DeleteColumnNames(self,DeleteColumnNames):
		for i in range(len(DeleteColumnNames)):	
			if DeleteColumnNames[i] is not None:
				self.add_query_param('DeleteColumnName.' + str(i + 1) , DeleteColumnNames[i]);

	def get_TableId(self):
		return self.get_query_params().get('TableId')

	def set_TableId(self,TableId):
		self.add_query_param('TableId',TableId)

	def get_DeletePartitionNames(self):
		return self.get_query_params().get('DeletePartitionNames')

	def set_DeletePartitionNames(self,DeletePartitionNames):
		for i in range(len(DeletePartitionNames)):	
			if DeletePartitionNames[i] is not None:
				self.add_query_param('DeletePartitionName.' + str(i + 1) , DeletePartitionNames[i]);