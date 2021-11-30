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
from aliyunsdkalb.endpoint import endpoint_data

class ReplaceServersInServerGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'ReplaceServersInServerGroup','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ServerGroupId(self): # String
		return self.get_query_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_query_param('ServerGroupId', ServerGroupId)
	def get_AddedServers(self): # Array
		return self.get_query_params().get('AddedServers')

	def set_AddedServers(self, AddedServers):  # Array
		for index1, value1 in enumerate(AddedServers):
			if value1.get('RemoteIpEnabled') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.RemoteIpEnabled', value1.get('RemoteIpEnabled'))
			if value1.get('ServerType') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.ServerType', value1.get('ServerType'))
			if value1.get('Port') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.Port', value1.get('Port'))
			if value1.get('Description') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.Description', value1.get('Description'))
			if value1.get('ServerIp') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.ServerIp', value1.get('ServerIp'))
			if value1.get('Weight') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.Weight', value1.get('Weight'))
			if value1.get('ServerId') is not None:
				self.add_query_param('AddedServers.' + str(index1 + 1) + '.ServerId', value1.get('ServerId'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_RemovedServers(self): # Array
		return self.get_query_params().get('RemovedServers')

	def set_RemovedServers(self, RemovedServers):  # Array
		for index1, value1 in enumerate(RemovedServers):
			if value1.get('ServerType') is not None:
				self.add_query_param('RemovedServers.' + str(index1 + 1) + '.ServerType', value1.get('ServerType'))
			if value1.get('Port') is not None:
				self.add_query_param('RemovedServers.' + str(index1 + 1) + '.Port', value1.get('Port'))
			if value1.get('ServerIp') is not None:
				self.add_query_param('RemovedServers.' + str(index1 + 1) + '.ServerIp', value1.get('ServerIp'))
			if value1.get('ServerId') is not None:
				self.add_query_param('RemovedServers.' + str(index1 + 1) + '.ServerId', value1.get('ServerId'))
