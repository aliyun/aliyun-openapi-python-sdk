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
from aliyunsdkadcp.endpoint import endpoint_data
import json

class DeployPolicyInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adcp', '2022-01-01', 'DeployPolicyInstance','adcp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_PolicyAction(self): # String
		return self.get_query_params().get('PolicyAction')

	def set_PolicyAction(self, PolicyAction):  # String
		self.add_query_param('PolicyAction', PolicyAction)
	def get_ClusterIds(self): # Array
		return self.get_query_params().get('ClusterIds')

	def set_ClusterIds(self, ClusterIds):  # Array
		self.add_query_param("ClusterIds", json.dumps(ClusterIds))
	def get_PolicyName(self): # String
		return self.get_query_params().get('PolicyName')

	def set_PolicyName(self, PolicyName):  # String
		self.add_query_param('PolicyName', PolicyName)
	def get_Namespaces(self): # Array
		return self.get_query_params().get('Namespaces')

	def set_Namespaces(self, Namespaces):  # Array
		self.add_query_param("Namespaces", json.dumps(Namespaces))
