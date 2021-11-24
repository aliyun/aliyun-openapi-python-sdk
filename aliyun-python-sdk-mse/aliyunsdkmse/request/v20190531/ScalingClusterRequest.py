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
from aliyunsdkmse.endpoint import endpoint_data

class ScalingClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'ScalingCluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterSpecification(self): # String
		return self.get_query_params().get('ClusterSpecification')

	def set_ClusterSpecification(self, ClusterSpecification):  # String
		self.add_query_param('ClusterSpecification', ClusterSpecification)
	def get_Cpu(self): # Integer
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # Integer
		self.add_query_param('Cpu', Cpu)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_MemoryCapacity(self): # Long
		return self.get_query_params().get('MemoryCapacity')

	def set_MemoryCapacity(self, MemoryCapacity):  # Long
		self.add_query_param('MemoryCapacity', MemoryCapacity)
	def get_InstanceCount(self): # Integer
		return self.get_query_params().get('InstanceCount')

	def set_InstanceCount(self, InstanceCount):  # Integer
		self.add_query_param('InstanceCount', InstanceCount)
