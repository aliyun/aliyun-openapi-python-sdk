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

class PushNoticeToiOSRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'PushNoticeToiOS')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ExtParameters(self):
		return self.get_query_params().get('ExtParameters')

	def set_ExtParameters(self,ExtParameters):
		self.add_query_param('ExtParameters',ExtParameters)

	def get_ApnsEnv(self):
		return self.get_query_params().get('ApnsEnv')

	def set_ApnsEnv(self,ApnsEnv):
		self.add_query_param('ApnsEnv',ApnsEnv)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_Body(self):
		return self.get_query_params().get('Body')

	def set_Body(self,Body):
		self.add_query_param('Body',Body)

	def get_JobKey(self):
		return self.get_query_params().get('JobKey')

	def set_JobKey(self,JobKey):
		self.add_query_param('JobKey',JobKey)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)

	def get_TargetValue(self):
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self,TargetValue):
		self.add_query_param('TargetValue',TargetValue)