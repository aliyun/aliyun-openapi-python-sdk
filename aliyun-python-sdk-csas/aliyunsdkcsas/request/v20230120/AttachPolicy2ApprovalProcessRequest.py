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

class AttachPolicy2ApprovalProcessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'AttachPolicy2ApprovalProcess')
		self.set_method('POST')

	def get_PolicyType(self): # String
		return self.get_body_params().get('PolicyType')

	def set_PolicyType(self, PolicyType):  # String
		self.add_body_params('PolicyType', PolicyType)
	def get_PolicyId(self): # String
		return self.get_body_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_body_params('PolicyId', PolicyId)
	def get_ProcessId(self): # String
		return self.get_body_params().get('ProcessId')

	def set_ProcessId(self, ProcessId):  # String
		self.add_body_params('ProcessId', ProcessId)
