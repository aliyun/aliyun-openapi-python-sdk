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
from aliyunsdkdas.endpoint import endpoint_data

class CreateKillInstanceSessionTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'CreateKillInstanceSessionTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_KillAllSessions(self): # String
		return self.get_query_params().get('KillAllSessions')

	def set_KillAllSessions(self, KillAllSessions):  # String
		self.add_query_param('KillAllSessions', KillAllSessions)
	def get_DbUser(self): # String
		return self.get_query_params().get('DbUser')

	def set_DbUser(self, DbUser):  # String
		self.add_query_param('DbUser', DbUser)
	def get_SessionIds(self): # String
		return self.get_query_params().get('SessionIds')

	def set_SessionIds(self, SessionIds):  # String
		self.add_query_param('SessionIds', SessionIds)
	def get_DbUserPassword(self): # String
		return self.get_query_params().get('DbUserPassword')

	def set_DbUserPassword(self, DbUserPassword):  # String
		self.add_query_param('DbUserPassword', DbUserPassword)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_IgnoredUsers(self): # String
		return self.get_query_params().get('IgnoredUsers')

	def set_IgnoredUsers(self, IgnoredUsers):  # String
		self.add_query_param('IgnoredUsers', IgnoredUsers)
	def get_NodeId(self): # String
		return self.get_query_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_query_param('NodeId', NodeId)
