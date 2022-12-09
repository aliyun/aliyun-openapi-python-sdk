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

class CreateBasicEndpointsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateBasicEndpoints','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Endpoints(self): # Array
		return self.get_query_params().get('Endpoints')

	def set_Endpoints(self, Endpoints):  # Array
		for index1, value1 in enumerate(Endpoints):
			if value1.get('Name') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.Name', value1.get('Name'))
			if value1.get('EndpointType') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.EndpointType', value1.get('EndpointType'))
			if value1.get('EndpointAddress') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.EndpointAddress', value1.get('EndpointAddress'))
			if value1.get('EndpointSubAddress') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.EndpointSubAddress', value1.get('EndpointSubAddress'))
			if value1.get('EndpointSubAddressType') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.EndpointSubAddressType', value1.get('EndpointSubAddressType'))
			if value1.get('EndpointZoneId') is not None:
				self.add_query_param('Endpoints.' + str(index1 + 1) + '.EndpointZoneId', value1.get('EndpointZoneId'))
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
	def get_EndpointGroupId(self): # String
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self, EndpointGroupId):  # String
		self.add_query_param('EndpointGroupId', EndpointGroupId)
