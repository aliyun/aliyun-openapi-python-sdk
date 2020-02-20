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
from aliyunsdkretailcloud.endpoint import endpoint_data

class CreateSlbAPRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateSlbAP','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SslCertId(self):
		return self.get_query_params().get('SslCertId')

	def set_SslCertId(self,SslCertId):
		self.add_query_param('SslCertId',SslCertId)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_Protocol(self):
		return self.get_query_params().get('Protocol')

	def set_Protocol(self,Protocol):
		self.add_query_param('Protocol',Protocol)

	def get_EstablishedTimeout(self):
		return self.get_query_params().get('EstablishedTimeout')

	def set_EstablishedTimeout(self,EstablishedTimeout):
		self.add_query_param('EstablishedTimeout',EstablishedTimeout)

	def get_SlbId(self):
		return self.get_query_params().get('SlbId')

	def set_SlbId(self,SlbId):
		self.add_query_param('SlbId',SlbId)

	def get_RealServerPort(self):
		return self.get_query_params().get('RealServerPort')

	def set_RealServerPort(self,RealServerPort):
		self.add_query_param('RealServerPort',RealServerPort)

	def get_StickySession(self):
		return self.get_query_params().get('StickySession')

	def set_StickySession(self,StickySession):
		self.add_query_param('StickySession',StickySession)

	def get_CookieTimeout(self):
		return self.get_query_params().get('CookieTimeout')

	def set_CookieTimeout(self,CookieTimeout):
		self.add_query_param('CookieTimeout',CookieTimeout)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)