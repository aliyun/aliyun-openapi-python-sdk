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

class SmartqAuthorizeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'SmartqAuthorize','2.2.0')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_LlmCubeThemes(self): # String
		return self.get_query_params().get('LlmCubeThemes')

	def set_LlmCubeThemes(self, LlmCubeThemes):  # String
		self.add_query_param('LlmCubeThemes', LlmCubeThemes)
	def get_LlmCubes(self): # String
		return self.get_query_params().get('LlmCubes')

	def set_LlmCubes(self, LlmCubes):  # String
		self.add_query_param('LlmCubes', LlmCubes)
	def get_CubeIds(self): # String
		return self.get_query_params().get('CubeIds')

	def set_CubeIds(self, CubeIds):  # String
		self.add_query_param('CubeIds', CubeIds)
	def get_OperationType(self): # Integer
		return self.get_query_params().get('OperationType')

	def set_OperationType(self, OperationType):  # Integer
		self.add_query_param('OperationType', OperationType)
	def get_ExpireDay(self): # String
		return self.get_query_params().get('ExpireDay')

	def set_ExpireDay(self, ExpireDay):  # String
		self.add_query_param('ExpireDay', ExpireDay)
	def get_UserIds(self): # String
		return self.get_query_params().get('UserIds')

	def set_UserIds(self, UserIds):  # String
		self.add_query_param('UserIds', UserIds)
