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
from aliyunsdkopenanalytics_open.endpoint import endpoint_data

class CreateTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'openanalytics-open', '2020-09-28', 'CreateTable','openanalytics')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TableType(self):
		return self.get_query_params().get('TableType')

	def set_TableType(self,TableType):
		self.add_query_param('TableType',TableType)

	def get_ViewOriginalText(self):
		return self.get_query_params().get('ViewOriginalText')

	def set_ViewOriginalText(self,ViewOriginalText):
		self.add_query_param('ViewOriginalText',ViewOriginalText)

	def get_StorageDescriptor(self):
		return self.get_query_params().get('StorageDescriptor')

	def set_StorageDescriptor(self,StorageDescriptor):
		self.add_query_param('StorageDescriptor',StorageDescriptor)

	def get_PartitionKeys(self):
		return self.get_query_params().get('PartitionKeys')

	def set_PartitionKeys(self,PartitionKeys):
		self.add_query_param('PartitionKeys',PartitionKeys)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_ViewExpandedText(self):
		return self.get_query_params().get('ViewExpandedText')

	def set_ViewExpandedText(self,ViewExpandedText):
		self.add_query_param('ViewExpandedText',ViewExpandedText)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_Parameters(self):
		return self.get_query_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_query_param('Parameters',Parameters)