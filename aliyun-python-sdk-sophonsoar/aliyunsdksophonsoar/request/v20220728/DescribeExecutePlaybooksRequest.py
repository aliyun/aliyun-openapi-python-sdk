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

class DescribeExecutePlaybooksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescribeExecutePlaybooks')
		self.set_method('GET')

	def get_PlaybookName(self): # String
		return self.get_query_params().get('PlaybookName')

	def set_PlaybookName(self, PlaybookName):  # String
		self.add_query_param('PlaybookName', PlaybookName)
	def get_ParamType(self): # String
		return self.get_query_params().get('ParamType')

	def set_ParamType(self, ParamType):  # String
		self.add_query_param('ParamType', ParamType)
	def get_InputMode(self): # String
		return self.get_query_params().get('InputMode')

	def set_InputMode(self, InputMode):  # String
		self.add_query_param('InputMode', InputMode)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
