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
from aliyunsdkccc.endpoint import endpoint_data

class AddAgentDeviceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'AddAgentDevice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Remark(self):
		return self.get_body_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_body_params('Remark', Remark)

	def get_ClientPort(self):
		return self.get_query_params().get('ClientPort')

	def set_ClientPort(self,ClientPort):
		self.add_query_param('ClientPort',ClientPort)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ClientIp(self):
		return self.get_query_params().get('ClientIp')

	def set_ClientIp(self,ClientIp):
		self.add_query_param('ClientIp',ClientIp)

	def get_BrowserVersion(self):
		return self.get_body_params().get('BrowserVersion')

	def set_BrowserVersion(self,BrowserVersion):
		self.add_body_params('BrowserVersion', BrowserVersion)