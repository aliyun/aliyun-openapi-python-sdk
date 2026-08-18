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

class DescriberPython3ScriptLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescriberPython3ScriptLogs')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_RequestUuid(self): # String
		return self.get_query_params().get('RequestUuid')

	def set_RequestUuid(self, RequestUuid):  # String
		self.add_query_param('RequestUuid', RequestUuid)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
