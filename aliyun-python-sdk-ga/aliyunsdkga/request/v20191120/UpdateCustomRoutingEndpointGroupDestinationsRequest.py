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

class UpdateCustomRoutingEndpointGroupDestinationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'UpdateCustomRoutingEndpointGroupDestinations','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DestinationConfigurationss(self): # RepeatList
		return self.get_query_params().get('DestinationConfigurations')

	def set_DestinationConfigurationss(self, DestinationConfigurations):  # RepeatList
		for depth1 in range(len(DestinationConfigurations)):
			if DestinationConfigurations[depth1].get('Protocols') is not None:
				for depth2 in range(len(DestinationConfigurations[depth1].get('Protocols'))):
					self.add_query_param('DestinationConfigurations.' + str(depth1 + 1) + '.Protocols.' + str(depth2 + 1), DestinationConfigurations[depth1].get('Protocols')[depth2])
			if DestinationConfigurations[depth1].get('FromPort') is not None:
				self.add_query_param('DestinationConfigurations.' + str(depth1 + 1) + '.FromPort', DestinationConfigurations[depth1].get('FromPort'))
			if DestinationConfigurations[depth1].get('ToPort') is not None:
				self.add_query_param('DestinationConfigurations.' + str(depth1 + 1) + '.ToPort', DestinationConfigurations[depth1].get('ToPort'))
			if DestinationConfigurations[depth1].get('DestinationId') is not None:
				self.add_query_param('DestinationConfigurations.' + str(depth1 + 1) + '.DestinationId', DestinationConfigurations[depth1].get('DestinationId'))
	def get_EndpointGroupId(self): # String
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self, EndpointGroupId):  # String
		self.add_query_param('EndpointGroupId', EndpointGroupId)
