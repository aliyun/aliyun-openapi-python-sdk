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

class TriggerSophonPlaybookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'TriggerSophonPlaybook')
		self.set_method('POST')

	def get_InputParams(self): # String
		return self.get_query_params().get('InputParams')

	def set_InputParams(self, InputParams):  # String
		self.add_query_param('InputParams', InputParams)
	def get_CommandName(self): # String
		return self.get_query_params().get('CommandName')

	def set_CommandName(self, CommandName):  # String
		self.add_query_param('CommandName', CommandName)
	def get_SophonTaskId(self): # String
		return self.get_query_params().get('SophonTaskId')

	def set_SophonTaskId(self, SophonTaskId):  # String
		self.add_query_param('SophonTaskId', SophonTaskId)
	def get_TriggerType(self): # String
		return self.get_query_params().get('TriggerType')

	def set_TriggerType(self, TriggerType):  # String
		self.add_query_param('TriggerType', TriggerType)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
