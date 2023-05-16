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
from aliyunsdkcomputenest.endpoint import endpoint_data

class ContinueDeployServiceInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ComputeNest', '2021-06-01', 'ContinueDeployServiceInstance','computenest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ServiceInstanceId(self): # String
		return self.get_query_params().get('ServiceInstanceId')

	def set_ServiceInstanceId(self, ServiceInstanceId):  # String
		self.add_query_param('ServiceInstanceId', ServiceInstanceId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
	def get_Options(self): # RepeatList
		return self.get_query_params().get('Option')

	def set_Options(self, Option):  # RepeatList
		for depth1 in range(len(Option)):
			self.add_query_param('Option.' + str(depth1 + 1), Option[depth1])
