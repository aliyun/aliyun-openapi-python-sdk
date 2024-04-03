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
from aliyunsdkalikafka.endpoint import endpoint_data

class CreateAclRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'CreateAcl','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AclResourcePatternType(self): # String
		return self.get_query_params().get('AclResourcePatternType')

	def set_AclResourcePatternType(self, AclResourcePatternType):  # String
		self.add_query_param('AclResourcePatternType', AclResourcePatternType)
	def get_AclResourceType(self): # String
		return self.get_query_params().get('AclResourceType')

	def set_AclResourceType(self, AclResourceType):  # String
		self.add_query_param('AclResourceType', AclResourceType)
	def get_AclOperationTypes(self): # String
		return self.get_query_params().get('AclOperationTypes')

	def set_AclOperationTypes(self, AclOperationTypes):  # String
		self.add_query_param('AclOperationTypes', AclOperationTypes)
	def get_AclOperationType(self): # String
		return self.get_query_params().get('AclOperationType')

	def set_AclOperationType(self, AclOperationType):  # String
		self.add_query_param('AclOperationType', AclOperationType)
	def get_AclResourceName(self): # String
		return self.get_query_params().get('AclResourceName')

	def set_AclResourceName(self, AclResourceName):  # String
		self.add_query_param('AclResourceName', AclResourceName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Host(self): # String
		return self.get_query_params().get('Host')

	def set_Host(self, Host):  # String
		self.add_query_param('Host', Host)
	def get_AclPermissionType(self): # String
		return self.get_query_params().get('AclPermissionType')

	def set_AclPermissionType(self, AclPermissionType):  # String
		self.add_query_param('AclPermissionType', AclPermissionType)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
