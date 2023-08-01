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

class GetFabricTopologyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'GetFabricTopology','eflo')
		self.set_method('POST')

	def get_VpdId(self): # String
		return self.get_body_params().get('VpdId')

	def set_VpdId(self, VpdId):  # String
		self.add_body_params('VpdId', VpdId)
	def get_LniIdss(self): # RepeatList
		return self.get_body_params().get('LniIds')

	def set_LniIdss(self, LniIds):  # RepeatList
		for depth1 in range(len(LniIds)):
			self.add_body_params('LniIds.' + str(depth1 + 1), LniIds[depth1])
	def get_NodeIdss(self): # RepeatList
		return self.get_body_params().get('NodeIds')

	def set_NodeIdss(self, NodeIds):  # RepeatList
		for depth1 in range(len(NodeIds)):
			self.add_body_params('NodeIds.' + str(depth1 + 1), NodeIds[depth1])
