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

class UpdateMetaTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateMetaTable')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_query_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_query_param('Schema', Schema)
	def get_Visibility(self): # Integer
		return self.get_query_params().get('Visibility')

	def set_Visibility(self, Visibility):  # Integer
		self.add_query_param('Visibility', Visibility)
	def get_Caption(self): # String
		return self.get_query_params().get('Caption')

	def set_Caption(self, Caption):  # String
		self.add_query_param('Caption', Caption)
	def get_NewOwnerId(self): # String
		return self.get_query_params().get('NewOwnerId')

	def set_NewOwnerId(self, NewOwnerId):  # String
		self.add_query_param('NewOwnerId', NewOwnerId)
	def get_TableGuid(self): # String
		return self.get_query_params().get('TableGuid')

	def set_TableGuid(self, TableGuid):  # String
		self.add_query_param('TableGuid', TableGuid)
	def get_AddedLabels(self): # String
		return self.get_body_params().get('AddedLabels')

	def set_AddedLabels(self, AddedLabels):  # String
		self.add_body_params('AddedLabels', AddedLabels)
	def get_RemovedLabels(self): # String
		return self.get_body_params().get('RemovedLabels')

	def set_RemovedLabels(self, RemovedLabels):  # String
		self.add_body_params('RemovedLabels', RemovedLabels)
	def get_EnvType(self): # Integer
		return self.get_query_params().get('EnvType')

	def set_EnvType(self, EnvType):  # Integer
		self.add_query_param('EnvType', EnvType)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_ProjectId(self): # Long
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_query_param('ProjectId', ProjectId)
	def get_CategoryId(self): # Long
		return self.get_query_params().get('CategoryId')

	def set_CategoryId(self, CategoryId):  # Long
		self.add_query_param('CategoryId', CategoryId)
