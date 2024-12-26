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

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SchedulerX3', '2024-06-24', 'CreateCluster')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ClusterName(self): # String
		return self.get_body_params().get('ClusterName')

	def set_ClusterName(self, ClusterName):  # String
		self.add_body_params('ClusterName', ClusterName)
	def get_EngineType(self): # String
		return self.get_body_params().get('EngineType')

	def set_EngineType(self, EngineType):  # String
		self.add_body_params('EngineType', EngineType)
	def get_VSwitches(self): # Array
		return self.get_body_params().get('VSwitches')

	def set_VSwitches(self, VSwitches):  # Array
		self.add_body_params("VSwitches", json.dumps(VSwitches))
	def get_ClusterSpec(self): # String
		return self.get_body_params().get('ClusterSpec')

	def set_ClusterSpec(self, ClusterSpec):  # String
		self.add_body_params('ClusterSpec', ClusterSpec)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
