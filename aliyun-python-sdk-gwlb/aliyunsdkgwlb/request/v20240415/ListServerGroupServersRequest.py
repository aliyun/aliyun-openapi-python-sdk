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
from aliyunsdkgwlb.endpoint import endpoint_data

class ListServerGroupServersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'ListServerGroupServers','gwlb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Skip(self): # Integer
		return self.get_body_params().get('Skip')

	def set_Skip(self, Skip):  # Integer
		self.add_body_params('Skip', Skip)
	def get_ServerGroupId(self): # String
		return self.get_body_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_body_params('ServerGroupId', ServerGroupId)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_ServerIds(self): # Array
		return self.get_body_params().get('ServerIds')

	def set_ServerIds(self, ServerIds):  # Array
		for index1, value1 in enumerate(ServerIds):
			self.add_body_params('ServerIds.' + str(index1 + 1), value1)
	def get_ServerIps(self): # Array
		return self.get_body_params().get('ServerIps')

	def set_ServerIps(self, ServerIps):  # Array
		for index1, value1 in enumerate(ServerIps):
			self.add_body_params('ServerIps.' + str(index1 + 1), value1)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
