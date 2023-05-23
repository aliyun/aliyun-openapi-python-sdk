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
from aliyunsdkccc.endpoint import endpoint_data

class BridgeRtcCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'BridgeRtcCall','CCC')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ServiceProvider(self): # String
		return self.get_query_params().get('ServiceProvider')

	def set_ServiceProvider(self, ServiceProvider):  # String
		self.add_query_param('ServiceProvider', ServiceProvider)
	def get_Callee(self): # String
		return self.get_query_params().get('Callee')

	def set_Callee(self, Callee):  # String
		self.add_query_param('Callee', Callee)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_DeviceId(self): # String
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self, DeviceId):  # String
		self.add_query_param('DeviceId', DeviceId)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_TimeoutSeconds(self): # Integer
		return self.get_query_params().get('TimeoutSeconds')

	def set_TimeoutSeconds(self, TimeoutSeconds):  # Integer
		self.add_query_param('TimeoutSeconds', TimeoutSeconds)
	def get_Caller(self): # String
		return self.get_query_params().get('Caller')

	def set_Caller(self, Caller):  # String
		self.add_query_param('Caller', Caller)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_VideoEnabled(self): # Boolean
		return self.get_query_params().get('VideoEnabled')

	def set_VideoEnabled(self, VideoEnabled):  # Boolean
		self.add_query_param('VideoEnabled', VideoEnabled)