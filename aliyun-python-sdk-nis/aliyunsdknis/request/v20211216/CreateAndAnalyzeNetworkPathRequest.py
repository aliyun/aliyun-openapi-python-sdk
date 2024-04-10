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

class CreateAndAnalyzeNetworkPathRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nis', '2021-12-16', 'CreateAndAnalyzeNetworkPath','networkana')
		self.set_method('GET')

	def get_TargetId(self): # String
		return self.get_query_params().get('TargetId')

	def set_TargetId(self, TargetId):  # String
		self.add_query_param('TargetId', TargetId)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_TargetIpAddress(self): # String
		return self.get_query_params().get('TargetIpAddress')

	def set_TargetIpAddress(self, TargetIpAddress):  # String
		self.add_query_param('TargetIpAddress', TargetIpAddress)
	def get_SourcePort(self): # Integer
		return self.get_query_params().get('SourcePort')

	def set_SourcePort(self, SourcePort):  # Integer
		self.add_query_param('SourcePort', SourcePort)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_TargetPort(self): # Integer
		return self.get_query_params().get('TargetPort')

	def set_TargetPort(self, TargetPort):  # Integer
		self.add_query_param('TargetPort', TargetPort)
	def get_SourceId(self): # String
		return self.get_query_params().get('SourceId')

	def set_SourceId(self, SourceId):  # String
		self.add_query_param('SourceId', SourceId)
	def get_SourceIpAddress(self): # String
		return self.get_query_params().get('SourceIpAddress')

	def set_SourceIpAddress(self, SourceIpAddress):  # String
		self.add_query_param('SourceIpAddress', SourceIpAddress)
