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
from aliyunsdkehpc.endpoint import endpoint_data
import json

class SubmitServerlessJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SubmitServerlessJob')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Container(self): # Struct
		return self.get_query_params().get('Container')

	def set_Container(self, Container):  # Struct
		self.add_query_param("Container", json.dumps(Container))
	def get_Memory(self): # Float
		return self.get_query_params().get('Memory')

	def set_Memory(self, Memory):  # Float
		self.add_query_param('Memory', Memory)
	def get_DependsOn(self): # Array
		return self.get_query_params().get('DependsOn')

	def set_DependsOn(self, DependsOn):  # Array
		self.add_query_param("DependsOn", json.dumps(DependsOn))
	def get_SpotPriceLimit(self): # Float
		return self.get_query_params().get('SpotPriceLimit')

	def set_SpotPriceLimit(self, SpotPriceLimit):  # Float
		self.add_query_param('SpotPriceLimit', SpotPriceLimit)
	def get_Timeout(self): # Long
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Long
		self.add_query_param('Timeout', Timeout)
	def get_InstanceType(self): # Array
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # Array
		for index1, value1 in enumerate(InstanceType):
			self.add_query_param('InstanceType.' + str(index1 + 1), value1)
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_JobPriority(self): # Long
		return self.get_query_params().get('JobPriority')

	def set_JobPriority(self, JobPriority):  # Long
		self.add_query_param('JobPriority', JobPriority)
	def get_Cpu(self): # Float
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Float
		self.add_query_param('Cpu', Cpu)
	def get_RamRoleName(self): # String
		return self.get_query_params().get('RamRoleName')

	def set_RamRoleName(self, RamRoleName):  # String
		self.add_query_param('RamRoleName', RamRoleName)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_VSwitchId(self): # Array
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # Array
		for index1, value1 in enumerate(VSwitchId):
			self.add_query_param('VSwitchId.' + str(index1 + 1), value1)
	def get_EphemeralStorage(self): # Integer
		return self.get_query_params().get('EphemeralStorage')

	def set_EphemeralStorage(self, EphemeralStorage):  # Integer
		self.add_query_param('EphemeralStorage', EphemeralStorage)
	def get_ArrayProperties(self): # Struct
		return self.get_query_params().get('ArrayProperties')

	def set_ArrayProperties(self, ArrayProperties):  # Struct
		self.add_query_param("ArrayProperties", json.dumps(ArrayProperties))
