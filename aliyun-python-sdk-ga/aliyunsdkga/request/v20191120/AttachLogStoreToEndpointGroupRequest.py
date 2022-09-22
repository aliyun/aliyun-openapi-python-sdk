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

class AttachLogStoreToEndpointGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'AttachLogStoreToEndpointGroup','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SlsLogStoreName(self): # String
		return self.get_query_params().get('SlsLogStoreName')

	def set_SlsLogStoreName(self, SlsLogStoreName):  # String
		self.add_query_param('SlsLogStoreName', SlsLogStoreName)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_EndpointGroupIdss(self): # RepeatList
		return self.get_query_params().get('EndpointGroupIds')

	def set_EndpointGroupIdss(self, EndpointGroupIds):  # RepeatList
		for depth1 in range(len(EndpointGroupIds)):
			self.add_query_param('EndpointGroupIds.' + str(depth1 + 1), EndpointGroupIds[depth1])
	def get_SlsProjectName(self): # String
		return self.get_query_params().get('SlsProjectName')

	def set_SlsProjectName(self, SlsProjectName):  # String
		self.add_query_param('SlsProjectName', SlsProjectName)
	def get_SlsRegionId(self): # String
		return self.get_query_params().get('SlsRegionId')

	def set_SlsRegionId(self, SlsRegionId):  # String
		self.add_query_param('SlsRegionId', SlsRegionId)
	def get_AcceleratorId(self): # String
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self, AcceleratorId):  # String
		self.add_query_param('AcceleratorId', AcceleratorId)
