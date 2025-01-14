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
import json

class CreateApprovalProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreateApprovalProcess')
		self.set_method('POST')

	def get_ProcessNodes(self): # Array
		return self.get_body_params().get('ProcessNodes')

	def set_ProcessNodes(self, ProcessNodes):  # Array
		for index1, value1 in enumerate(ProcessNodes):
			for index2, value2 in enumerate(value1):
				self.add_body_params('ProcessNodes.' + str(index1 + 1), value2)
	def get_MatchSchemas(self): # Struct
		return self.get_body_params().get('MatchSchemas')

	def set_MatchSchemas(self, MatchSchemas):  # Struct
		self.add_body_params("MatchSchemas", json.dumps(MatchSchemas))
	def get_ProcessName(self): # String
		return self.get_body_params().get('ProcessName')

	def set_ProcessName(self, ProcessName):  # String
		self.add_body_params('ProcessName', ProcessName)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
