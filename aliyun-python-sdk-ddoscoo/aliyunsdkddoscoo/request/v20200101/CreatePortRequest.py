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
from aliyunsdkddoscoo.endpoint import endpoint_data

class CreatePortRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ddoscoo', '2020-01-01', 'CreatePort')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BackendPort(self):
		return self.get_query_params().get('BackendPort')

	def set_BackendPort(self,BackendPort):
		self.add_query_param('BackendPort',BackendPort)

	def get_FrontendProtocol(self):
		return self.get_query_params().get('FrontendProtocol')

	def set_FrontendProtocol(self,FrontendProtocol):
		self.add_query_param('FrontendProtocol',FrontendProtocol)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_RealServerss(self):
		return self.get_query_params().get('RealServers')

	def set_RealServerss(self, RealServerss):
		for depth1 in range(len(RealServerss)):
			if RealServerss[depth1] is not None:
				self.add_query_param('RealServers.' + str(depth1 + 1) , RealServerss[depth1])

	def get_FrontendPort(self):
		return self.get_query_params().get('FrontendPort')

	def set_FrontendPort(self,FrontendPort):
		self.add_query_param('FrontendPort',FrontendPort)