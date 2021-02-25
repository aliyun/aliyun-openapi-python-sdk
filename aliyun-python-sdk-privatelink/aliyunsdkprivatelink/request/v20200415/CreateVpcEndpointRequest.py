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


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupIds):
		for depth1 in range(len(SecurityGroupIds)):
			if SecurityGroupIds[depth1] is not None:
				self.add_query_param('SecurityGroupId.' + str(depth1 + 1) , SecurityGroupIds[depth1])

	def get_Zone(self):
		return self.get_query_params().get('Zone')

	def set_Zone(self, Zones):
		for depth1 in range(len(Zones)):
			if Zones[depth1].get('VSwitchId') is not None:
				self.add_query_param('Zone.' + str(depth1 + 1) + '.VSwitchId', Zones[depth1].get('VSwitchId'))
			if Zones[depth1].get('ZoneId') is not None:
				self.add_query_param('Zone.' + str(depth1 + 1) + '.ZoneId', Zones[depth1].get('ZoneId'))

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_EndpointDescription(self):
		return self.get_query_params().get('EndpointDescription')

	def set_EndpointDescription(self,EndpointDescription):
		self.add_query_param('EndpointDescription',EndpointDescription)

	def get_EndpointName(self):
		return self.get_query_params().get('EndpointName')

	def set_EndpointName(self,EndpointName):
		self.add_query_param('EndpointName',EndpointName)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_ServiceId(self):
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self,ServiceId):
		self.add_query_param('ServiceId',ServiceId)