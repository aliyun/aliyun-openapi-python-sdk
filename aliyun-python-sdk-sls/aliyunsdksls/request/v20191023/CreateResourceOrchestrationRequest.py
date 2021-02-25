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
from aliyunsdksls.endpoint import endpoint_data

class CreateResourceOrchestrationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sls', '2019-10-23', 'CreateResourceOrchestration')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Language(self):
		return self.get_query_params().get('Language')

	def set_Language(self,Language):
		self.add_query_param('Language',Language)

	def get_OperationPolicy(self):
		return self.get_query_params().get('OperationPolicy')

	def set_OperationPolicy(self,OperationPolicy):
		self.add_query_param('OperationPolicy',OperationPolicy)

	def get_Tokens(self):
		return self.get_query_params().get('Tokens')

	def set_Tokens(self,Tokens):
		self.add_query_param('Tokens',Tokens)

	def get_AssetsId(self):
		return self.get_query_params().get('AssetsId')

	def set_AssetsId(self,AssetsId):
		self.add_query_param('AssetsId',AssetsId)