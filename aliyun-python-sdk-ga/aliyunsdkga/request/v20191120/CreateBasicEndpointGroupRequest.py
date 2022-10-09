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

class CreateBasicEndpointGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateBasicEndpointGroup','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_EndpointAddress(self): # String
		return self.get_query_params().get('EndpointAddress')

	def set_EndpointAddress(self, EndpointAddress):  # String
		self.add_query_param('EndpointAddress', EndpointAddress)
	def get_EndpointGroupRegion(self): # String
		return self.get_query_params().get('EndpointGroupRegion')

	def set_EndpointGroupRegion(self, EndpointGroupRegion):  # String
		self.add_query_param('EndpointGroupRegion', EndpointGroupRegion)
	def get_EndpointType(self): # String
		return self.get_query_params().get('EndpointType')

	def set_EndpointType(self, EndpointType):  # String
		self.add_query_param('EndpointType', EndpointType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
	def get_EndpointSubAddress(self): # String
		return self.get_query_params().get('EndpointSubAddress')

	def set_EndpointSubAddress(self, EndpointSubAddress):  # String
		self.add_query_param('EndpointSubAddress', EndpointSubAddress)
