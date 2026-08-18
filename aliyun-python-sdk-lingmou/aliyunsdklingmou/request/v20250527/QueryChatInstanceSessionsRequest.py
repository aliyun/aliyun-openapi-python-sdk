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

from aliyunsdkcore.request import RoaRequest

class QueryChatInstanceSessionsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'LingMou', '2025-05-27', 'QueryChatInstanceSessions')
		self.set_protocol_type('https')
		self.set_uri_pattern('/openapi/chat/instances/[instanceId]/sessions')
		self.set_method('GET')

	def get_instanceId(self): # String
		return self.get_path_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_path_param('instanceId', instanceId)
	def get_sessionIds(self): # String
		return self.get_query_params().get('sessionIds')

	def set_sessionIds(self, sessionIds):  # String
		self.add_query_param('sessionIds', sessionIds)
