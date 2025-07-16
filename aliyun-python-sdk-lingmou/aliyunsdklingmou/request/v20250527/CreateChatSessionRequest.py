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

class CreateChatSessionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'LingMou', '2025-05-27', 'CreateChatSession')
		self.set_protocol_type('https')
		self.set_uri_pattern('/openapi/chat/init/[id]')
		self.set_method('POST')

	def get_license(self): # String
		return self.get_query_params().get('license')

	def set_license(self, license):  # String
		self.add_query_param('license', license)
	def get_instanceId(self): # String
		return self.get_query_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_query_param('instanceId', instanceId)
	def get_id(self): # String
		return self.get_path_params().get('id')

	def set_id(self, id):  # String
		self.add_path_param('id', id)
	def get_platform(self): # String
		return self.get_query_params().get('platform')

	def set_platform(self, platform):  # String
		self.add_query_param('platform', platform)
