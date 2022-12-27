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
from aliyunsdkdcdn.endpoint import endpoint_data

class DcdnHttpRequestTestToolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'DcdnHttpRequestTestTool')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Args(self): # String
		return self.get_body_params().get('Args')

	def set_Args(self, Args):  # String
		self.add_body_params('Args', Args)
	def get_ProxyIp(self): # String
		return self.get_body_params().get('ProxyIp')

	def set_ProxyIp(self, ProxyIp):  # String
		self.add_body_params('ProxyIp', ProxyIp)
	def get_Method(self): # String
		return self.get_body_params().get('Method')

	def set_Method(self, Method):  # String
		self.add_body_params('Method', Method)
	def get_Scheme(self): # String
		return self.get_body_params().get('Scheme')

	def set_Scheme(self, Scheme):  # String
		self.add_body_params('Scheme', Scheme)
	def get_Host(self): # String
		return self.get_body_params().get('Host')

	def set_Host(self, Host):  # String
		self.add_body_params('Host', Host)
	def get_Header(self): # String
		return self.get_body_params().get('Header')

	def set_Header(self, Header):  # String
		self.add_body_params('Header', Header)
	def get_Body(self): # String
		return self.get_body_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_body_params('Body', Body)
	def get_Uri(self): # String
		return self.get_body_params().get('Uri')

	def set_Uri(self, Uri):  # String
		self.add_body_params('Uri', Uri)
