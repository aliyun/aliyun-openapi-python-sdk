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
from aliyunsdkrds.endpoint import endpoint_data

class CreateCloudMigrationTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateCloudMigrationTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_SourceAccount(self): # String
		return self.get_query_params().get('SourceAccount')

	def set_SourceAccount(self, SourceAccount):  # String
		self.add_query_param('SourceAccount', SourceAccount)
	def get_SourcePort(self): # Long
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self, SourcePort):  # Long
		self.add_query_param('SourcePort', SourcePort)
	def get_SourcePassword(self): # String
		return self.get_query_params().get('SourcePassword')

	def set_SourcePassword(self, SourcePassword):  # String
		self.add_query_param('SourcePassword', SourcePassword)
	def get_SourceIpAddress(self): # String
		return self.get_query_params().get('SourceIpAddress')

	def set_SourceIpAddress(self, SourceIpAddress):  # String
		self.add_query_param('SourceIpAddress', SourceIpAddress)
	def get_SourceCategory(self): # String
		return self.get_query_params().get('SourceCategory')

	def set_SourceCategory(self, SourceCategory):  # String
		self.add_query_param('SourceCategory', SourceCategory)
