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
from aliyunsdkbaas.endpoint import endpoint_data

class CreateEcosphereRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateEcosphere')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OrderersCount(self):
		return self.get_body_params().get('OrderersCount')

	def set_OrderersCount(self,OrderersCount):
		self.add_body_params('OrderersCount', OrderersCount)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Duration(self):
		return self.get_body_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_body_params('Duration', Duration)

	def get_ConsortiumName(self):
		return self.get_body_params().get('ConsortiumName')

	def set_ConsortiumName(self,ConsortiumName):
		self.add_body_params('ConsortiumName', ConsortiumName)

	def get_SpecName(self):
		return self.get_body_params().get('SpecName')

	def set_SpecName(self,SpecName):
		self.add_body_params('SpecName', SpecName)

	def get_ChannelPolicy(self):
		return self.get_body_params().get('ChannelPolicy')

	def set_ChannelPolicy(self,ChannelPolicy):
		self.add_body_params('ChannelPolicy', ChannelPolicy)

	def get_Organizations(self):
		return self.get_body_params().get('Organizations')

	def set_Organizations(self, Organizations):
		for depth1 in range(len(Organizations)):
			if Organizations[depth1].get('Domain') is not None:
				self.add_body_params('Organization.' + str(depth1 + 1) + '.Domain', Organizations[depth1].get('Domain'))
			if Organizations[depth1].get('Name') is not None:
				self.add_body_params('Organization.' + str(depth1 + 1) + '.Name', Organizations[depth1].get('Name'))
			if Organizations[depth1].get('Description') is not None:
				self.add_body_params('Organization.' + str(depth1 + 1) + '.Description', Organizations[depth1].get('Description'))

	def get_ZoneId(self):
		return self.get_body_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_body_params('ZoneId', ZoneId)

	def get_OrdererType(self):
		return self.get_body_params().get('OrdererType')

	def set_OrdererType(self,OrdererType):
		self.add_body_params('OrdererType', OrdererType)

	def get_OrdererDomain(self):
		return self.get_body_params().get('OrdererDomain')

	def set_OrdererDomain(self,OrdererDomain):
		self.add_body_params('OrdererDomain', OrdererDomain)

	def get_Location(self):
		return self.get_body_params().get('Location')

	def set_Location(self,Location):
		self.add_body_params('Location', Location)

	def get_PeersCount(self):
		return self.get_body_params().get('PeersCount')

	def set_PeersCount(self,PeersCount):
		self.add_body_params('PeersCount', PeersCount)

	def get_PricingCycle(self):
		return self.get_body_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_body_params('PricingCycle', PricingCycle)