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
from aliyunsdkice.endpoint import endpoint_data

class SetEventCallbackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'SetEventCallback','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AuthKey(self): # String
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self, AuthKey):  # String
		self.add_query_param('AuthKey', AuthKey)
	def get_CallbackType(self): # String
		return self.get_query_params().get('CallbackType')

	def set_CallbackType(self, CallbackType):  # String
		self.add_query_param('CallbackType', CallbackType)
	def get_CallbackQueueName(self): # String
		return self.get_query_params().get('CallbackQueueName')

	def set_CallbackQueueName(self, CallbackQueueName):  # String
		self.add_query_param('CallbackQueueName', CallbackQueueName)
	def get_EventTypeList(self): # String
		return self.get_query_params().get('EventTypeList')

	def set_EventTypeList(self, EventTypeList):  # String
		self.add_query_param('EventTypeList', EventTypeList)
	def get_AuthSwitch(self): # String
		return self.get_query_params().get('AuthSwitch')

	def set_AuthSwitch(self, AuthSwitch):  # String
		self.add_query_param('AuthSwitch', AuthSwitch)
	def get_CallbackURL(self): # String
		return self.get_query_params().get('CallbackURL')

	def set_CallbackURL(self, CallbackURL):  # String
		self.add_query_param('CallbackURL', CallbackURL)
