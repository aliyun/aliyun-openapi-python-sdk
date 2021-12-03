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

class CreateVpcEndpointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Privatelink', '2020-04-15', 'CreateVpcEndpoint','privatelink')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SecurityGroupIds(self): # RepeatList
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupIds(self, SecurityGroupId):  # RepeatList
		for depth1 in range(len(SecurityGroupId)):
			self.add_query_param('SecurityGroupId.' + str(depth1 + 1), SecurityGroupId[depth1])
	def get_EndpointType(self): # String
		return self.get_query_params().get('EndpointType')

	def set_EndpointType(self, EndpointType):  # String
		self.add_query_param('EndpointType', EndpointType)
	def get_Zones(self): # RepeatList
		return self.get_query_params().get('Zone')

	def set_Zones(self, Zone):  # RepeatList
		for depth1 in range(len(Zone)):
			if Zone[depth1].get('VSwitchId') is not None:
				self.add_query_param('Zone.' + str(depth1 + 1) + '.VSwitchId', Zone[depth1].get('VSwitchId'))
			if Zone[depth1].get('ZoneId') is not None:
				self.add_query_param('Zone.' + str(depth1 + 1) + '.ZoneId', Zone[depth1].get('ZoneId'))
			if Zone[depth1].get('ip') is not None:
				self.add_query_param('Zone.' + str(depth1 + 1) + '.ip', Zone[depth1].get('ip'))
	def get_ServiceName(self): # String
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_query_param('ServiceName', ServiceName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_EndpointDescription(self): # String
		return self.get_query_params().get('EndpointDescription')

	def set_EndpointDescription(self, EndpointDescription):  # String
		self.add_query_param('EndpointDescription', EndpointDescription)
	def get_ZonePrivateIpAddressCount(self): # Long
		return self.get_query_params().get('ZonePrivateIpAddressCount')

	def set_ZonePrivateIpAddressCount(self, ZonePrivateIpAddressCount):  # Long
		self.add_query_param('ZonePrivateIpAddressCount', ZonePrivateIpAddressCount)
	def get_EndpointName(self): # String
		return self.get_query_params().get('EndpointName')

	def set_EndpointName(self, EndpointName):  # String
		self.add_query_param('EndpointName', EndpointName)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_ServiceId(self): # String
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self, ServiceId):  # String
		self.add_query_param('ServiceId', ServiceId)
