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
from aliyunsdkpush.endpoint import endpoint_data

class PushMessageToAndroidRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'PushMessageToAndroid')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_Body(self): # String
		return self.get_query_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_query_param('Body', Body)
	def get_StoreOffline(self): # Boolean
		return self.get_query_params().get('StoreOffline')

	def set_StoreOffline(self, StoreOffline):  # Boolean
		self.add_query_param('StoreOffline', StoreOffline)
	def get_JobKey(self): # String
		return self.get_query_params().get('JobKey')

	def set_JobKey(self, JobKey):  # String
		self.add_query_param('JobKey', JobKey)
	def get_Target(self): # String
		return self.get_query_params().get('Target')

	def set_Target(self, Target):  # String
		self.add_query_param('Target', Target)
	def get_AppKey(self): # Long
		return self.get_query_params().get('AppKey')

	def set_AppKey(self, AppKey):  # Long
		self.add_query_param('AppKey', AppKey)
	def get_TargetValue(self): # String
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self, TargetValue):  # String
		self.add_query_param('TargetValue', TargetValue)
