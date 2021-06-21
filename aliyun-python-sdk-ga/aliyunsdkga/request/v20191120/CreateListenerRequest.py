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
from aliyunsdkga.endpoint import endpoint_data

class CreateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateListener','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Protocol(self):
		return self.get_query_params().get('Protocol')

	def set_Protocol(self,Protocol):
		self.add_query_param('Protocol',Protocol)

	def get_AcceleratorId(self):
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self,AcceleratorId):
		self.add_query_param('AcceleratorId',AcceleratorId)

	def get_ProxyProtocol(self):
		return self.get_query_params().get('ProxyProtocol')

	def set_ProxyProtocol(self,ProxyProtocol):
		self.add_query_param('ProxyProtocol',ProxyProtocol)

	def get_PortRangess(self):
		return self.get_query_params().get('PortRanges')

	def set_PortRangess(self, PortRangess):
		for depth1 in range(len(PortRangess)):
			if PortRangess[depth1].get('FromPort') is not None:
				self.add_query_param('PortRanges.' + str(depth1 + 1) + '.FromPort', PortRangess[depth1].get('FromPort'))
			if PortRangess[depth1].get('ToPort') is not None:
				self.add_query_param('PortRanges.' + str(depth1 + 1) + '.ToPort', PortRangess[depth1].get('ToPort'))

	def get_Certificatess(self):
		return self.get_query_params().get('Certificates')

	def set_Certificatess(self, Certificatess):
		for depth1 in range(len(Certificatess)):
			if Certificatess[depth1].get('Id') is not None:
				self.add_query_param('Certificates.' + str(depth1 + 1) + '.Id', Certificatess[depth1].get('Id'))

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ClientAffinity(self):
		return self.get_query_params().get('ClientAffinity')

	def set_ClientAffinity(self,ClientAffinity):
		self.add_query_param('ClientAffinity',ClientAffinity)