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

class ListFreeNodesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo-controller', '2022-12-15', 'ListFreeNodes','eflo')
		self.set_method('POST')

	def get_MachineType(self): # String
		return self.get_body_params().get('MachineType')

	def set_MachineType(self, MachineType):  # String
		self.add_body_params('MachineType', MachineType)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_MaxResults(self): # Long
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_body_params('MaxResults', MaxResults)
