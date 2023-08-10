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

class DeleteHubClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adcp', '2022-01-01', 'DeleteHubCluster','adcp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RetainResources(self): # Array
		return self.get_query_params().get('RetainResources')

	def set_RetainResources(self, RetainResources):  # Array
		self.add_query_param("RetainResources", json.dumps(RetainResources))
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_Force(self): # Boolean
		return self.get_query_params().get('Force')

	def set_Force(self, Force):  # Boolean
		self.add_query_param('Force', Force)
