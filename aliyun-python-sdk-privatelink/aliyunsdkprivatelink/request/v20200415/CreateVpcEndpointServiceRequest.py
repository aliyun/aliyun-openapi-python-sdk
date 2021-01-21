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
from aliyunsdkprivatelink.endpoint import endpoint_data

class CreateVpcEndpointServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Privatelink', '2020-04-15', 'CreateVpcEndpointService','privatelink')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoAcceptEnabled(self):
		return self.get_query_params().get('AutoAcceptEnabled')

	def set_AutoAcceptEnabled(self,AutoAcceptEnabled):
		self.add_query_param('AutoAcceptEnabled',AutoAcceptEnabled)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_Payer(self):
		return self.get_query_params().get('Payer')

	def set_Payer(self,Payer):
		self.add_query_param('Payer',Payer)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_Resource(self):
		return self.get_query_params().get('Resource')

	def set_Resource(self, Resources):
		for depth1 in range(len(Resources)):
			if Resources[depth1].get('ResourceId') is not None:
				self.add_query_param('Resource.' + str(depth1 + 1) + '.ResourceId', Resources[depth1].get('ResourceId'))
			if Resources[depth1].get('ResourceType') is not None:
				self.add_query_param('Resource.' + str(depth1 + 1) + '.ResourceType', Resources[depth1].get('ResourceType'))

	def get_ServiceDescription(self):
		return self.get_query_params().get('ServiceDescription')

	def set_ServiceDescription(self,ServiceDescription):
		self.add_query_param('ServiceDescription',ServiceDescription)