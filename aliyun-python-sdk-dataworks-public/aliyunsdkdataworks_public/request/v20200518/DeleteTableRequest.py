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

class DeleteTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'DeleteTable')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Schema(self): # String
		return self.get_query_params().get('Schema')

	def set_Schema(self, Schema):  # String
		self.add_query_param('Schema', Schema)
	def get_EnvType(self): # Integer
		return self.get_query_params().get('EnvType')

	def set_EnvType(self, EnvType):  # Integer
		self.add_query_param('EnvType', EnvType)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_AppGuid(self): # String
		return self.get_query_params().get('AppGuid')

	def set_AppGuid(self, AppGuid):  # String
		self.add_query_param('AppGuid', AppGuid)
	def get_ProjectId(self): # Long
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_query_param('ProjectId', ProjectId)
