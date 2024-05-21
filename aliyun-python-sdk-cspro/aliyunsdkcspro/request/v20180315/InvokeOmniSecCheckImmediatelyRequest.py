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
from aliyunsdkcspro.endpoint import endpoint_data

class InvokeOmniSecCheckImmediatelyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cspro', '2018-03-15', 'InvokeOmniSecCheckImmediately','cspro')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CheckType(self):
		return self.get_body_params().get('CheckType')

	def set_CheckType(self,CheckType):
		self.add_body_params('CheckType', CheckType)

	def get_CheckTarget(self):
		return self.get_body_params().get('CheckTarget')

	def set_CheckTarget(self,CheckTarget):
		self.add_body_params('CheckTarget', CheckTarget)

	def get_ConfType(self):
		return self.get_body_params().get('ConfType')

	def set_ConfType(self,ConfType):
		self.add_body_params('ConfType', ConfType)