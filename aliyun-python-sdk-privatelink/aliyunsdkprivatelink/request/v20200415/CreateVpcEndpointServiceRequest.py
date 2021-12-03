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

	def get_AutoAcceptEnabled(self): # Boolean
		return self.get_query_params().get('AutoAcceptEnabled')

	def set_AutoAcceptEnabled(self, AutoAcceptEnabled):  # Boolean
		self.add_query_param('AutoAcceptEnabled', AutoAcceptEnabled)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Payer(self): # String
		return self.get_query_params().get('Payer')

	def set_Payer(self, Payer):  # String
		self.add_query_param('Payer', Payer)
	def get_ZoneAffinityEnabled(self): # Boolean
		return self.get_query_params().get('ZoneAffinityEnabled')

	def set_ZoneAffinityEnabled(self, ZoneAffinityEnabled):  # Boolean
		self.add_query_param('ZoneAffinityEnabled', ZoneAffinityEnabled)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Resources(self): # RepeatList
		return self.get_query_params().get('Resource')

	def set_Resources(self, Resource):  # RepeatList
		for depth1 in range(len(Resource)):
			if Resource[depth1].get('ResourceType') is not None:
				self.add_query_param('Resource.' + str(depth1 + 1) + '.ResourceType', Resource[depth1].get('ResourceType'))
			if Resource[depth1].get('ResourceId') is not None:
				self.add_query_param('Resource.' + str(depth1 + 1) + '.ResourceId', Resource[depth1].get('ResourceId'))
	def get_ServiceResourceType(self): # String
		return self.get_query_params().get('ServiceResourceType')

	def set_ServiceResourceType(self, ServiceResourceType):  # String
		self.add_query_param('ServiceResourceType', ServiceResourceType)
	def get_ServiceDescription(self): # String
		return self.get_query_params().get('ServiceDescription')

	def set_ServiceDescription(self, ServiceDescription):  # String
		self.add_query_param('ServiceDescription', ServiceDescription)
