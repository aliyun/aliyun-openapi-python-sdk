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
from aliyunsdkcloudapi.endpoint import endpoint_data

class EnableInstanceAccessControlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'EnableInstanceAccessControl','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AclId(self): # String
		return self.get_query_params().get('AclId')

	def set_AclId(self, AclId):  # String
		self.add_query_param('AclId', AclId)
	def get_AddressIPVersion(self): # String
		return self.get_query_params().get('AddressIPVersion')

	def set_AddressIPVersion(self, AddressIPVersion):  # String
		self.add_query_param('AddressIPVersion', AddressIPVersion)
	def get_AclType(self): # String
		return self.get_query_params().get('AclType')

	def set_AclType(self, AclType):  # String
		self.add_query_param('AclType', AclType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
