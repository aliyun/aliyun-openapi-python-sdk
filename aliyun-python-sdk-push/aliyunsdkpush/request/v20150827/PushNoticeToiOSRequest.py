# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class PushNoticeToiOSRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2015-08-27', 'PushNoticeToiOS')

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)

	def get_Target(self):
		return self.get_query_params().get('Target')

	def set_Target(self,Target):
		self.add_query_param('Target',Target)

	def get_TargetValue(self):
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self,TargetValue):
		self.add_query_param('TargetValue',TargetValue)

	def get_Ext(self):
		return self.get_query_params().get('Ext')

	def set_Ext(self,Ext):
		self.add_query_param('Ext',Ext)

	def get_Env(self):
		return self.get_query_params().get('Env')

	def set_Env(self,Env):
		self.add_query_param('Env',Env)

	def get_Summary(self):
		return self.get_query_params().get('Summary')

	def set_Summary(self,Summary):
		self.add_query_param('Summary',Summary)

	def get_iOSExtParameters(self):
		return self.get_query_params().get('iOSExtParameters')

	def set_iOSExtParameters(self,iOSExtParameters):
		self.add_query_param('iOSExtParameters',iOSExtParameters)