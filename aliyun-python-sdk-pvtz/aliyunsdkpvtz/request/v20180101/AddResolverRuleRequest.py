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
from aliyunsdkpvtz.endpoint import endpoint_data

class AddResolverRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'pvtz', '2018-01-01', 'AddResolverRule','pvtz')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndpointId(self): # String
		return self.get_query_params().get('EndpointId')

	def set_EndpointId(self, EndpointId):  # String
		self.add_query_param('EndpointId', EndpointId)
	def get_ForwardIps(self): # RepeatList
		return self.get_query_params().get('ForwardIp')

	def set_ForwardIps(self, ForwardIp):  # RepeatList
		for depth1 in range(len(ForwardIp)):
			if ForwardIp[depth1].get('Port') is not None:
				self.add_query_param('ForwardIp.' + str(depth1 + 1) + '.Port', ForwardIp[depth1].get('Port'))
			if ForwardIp[depth1].get('Ip') is not None:
				self.add_query_param('ForwardIp.' + str(depth1 + 1) + '.Ip', ForwardIp[depth1].get('Ip'))
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_ZoneName(self): # String
		return self.get_query_params().get('ZoneName')

	def set_ZoneName(self, ZoneName):  # String
		self.add_query_param('ZoneName', ZoneName)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
