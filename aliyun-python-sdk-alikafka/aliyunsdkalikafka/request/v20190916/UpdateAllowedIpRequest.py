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

class UpdateAllowedIpRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alikafka', '2019-09-16', 'UpdateAllowedIp','alikafka')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PortRange(self): # String
		return self.get_query_params().get('PortRange')

	def set_PortRange(self, PortRange):  # String
		self.add_query_param('PortRange', PortRange)
	def get_AllowedListIp(self): # String
		return self.get_query_params().get('AllowedListIp')

	def set_AllowedListIp(self, AllowedListIp):  # String
		self.add_query_param('AllowedListIp', AllowedListIp)
	def get_UpdateType(self): # String
		return self.get_query_params().get('UpdateType')

	def set_UpdateType(self, UpdateType):  # String
		self.add_query_param('UpdateType', UpdateType)
	def get_AllowedListType(self): # String
		return self.get_query_params().get('AllowedListType')

	def set_AllowedListType(self, AllowedListType):  # String
		self.add_query_param('AllowedListType', AllowedListType)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
