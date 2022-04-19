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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CheckMetaPartitionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CheckMetaPartition')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DataSourceType(self):
		return self.get_query_params().get('DataSourceType')

	def set_DataSourceType(self,DataSourceType):
		self.add_query_param('DataSourceType',DataSourceType)

	def get_Partition(self):
		return self.get_query_params().get('Partition')

	def set_Partition(self,Partition):
		self.add_query_param('Partition',Partition)

	def get_TableGuid(self):
		return self.get_query_params().get('TableGuid')

	def set_TableGuid(self,TableGuid):
		self.add_query_param('TableGuid',TableGuid)

	def get_DatabaseName(self):
		return self.get_query_params().get('DatabaseName')

	def set_DatabaseName(self,DatabaseName):
		self.add_query_param('DatabaseName',DatabaseName)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)