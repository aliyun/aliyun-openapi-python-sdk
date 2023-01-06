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
from aliyunsdkecd.endpoint import endpoint_data

class DetachEndUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DetachEndUser')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientType(self): # String
		return self.get_query_params().get('ClientType')

	def set_ClientType(self, ClientType):  # String
		self.add_query_param('ClientType', ClientType)
	def get_DeviceId(self): # String
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self, DeviceId):  # String
		self.add_query_param('DeviceId', DeviceId)
	def get_AdDomain(self): # String
		return self.get_query_params().get('AdDomain')

	def set_AdDomain(self, AdDomain):  # String
		self.add_query_param('AdDomain', AdDomain)
	def get_EndUserId(self): # String
		return self.get_query_params().get('EndUserId')

	def set_EndUserId(self, EndUserId):  # String
		self.add_query_param('EndUserId', EndUserId)
	def get_DirectoryId(self): # String
		return self.get_query_params().get('DirectoryId')

	def set_DirectoryId(self, DirectoryId):  # String
		self.add_query_param('DirectoryId', DirectoryId)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
