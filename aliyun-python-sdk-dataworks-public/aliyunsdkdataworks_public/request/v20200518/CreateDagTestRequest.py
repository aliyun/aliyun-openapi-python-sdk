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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateDagTestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateDagTest')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProjectEnv(self): # String
		return self.get_body_params().get('ProjectEnv')

	def set_ProjectEnv(self, ProjectEnv):  # String
		self.add_body_params('ProjectEnv', ProjectEnv)
	def get_Bizdate(self): # String
		return self.get_body_params().get('Bizdate')

	def set_Bizdate(self, Bizdate):  # String
		self.add_body_params('Bizdate', Bizdate)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_NodeParams(self): # String
		return self.get_body_params().get('NodeParams')

	def set_NodeParams(self, NodeParams):  # String
		self.add_body_params('NodeParams', NodeParams)
	def get_NodeId(self): # Long
		return self.get_body_params().get('NodeId')

	def set_NodeId(self, NodeId):  # Long
		self.add_body_params('NodeId', NodeId)
