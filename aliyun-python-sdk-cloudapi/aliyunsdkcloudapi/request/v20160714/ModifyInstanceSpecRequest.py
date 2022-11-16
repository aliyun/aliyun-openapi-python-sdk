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
from aliyunsdkcloudapi.endpoint import endpoint_data

class ModifyInstanceSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'ModifyInstanceSpec','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_SkipWaitSwitch(self): # Boolean
		return self.get_query_params().get('SkipWaitSwitch')

	def set_SkipWaitSwitch(self, SkipWaitSwitch):  # Boolean
		self.add_query_param('SkipWaitSwitch', SkipWaitSwitch)
	def get_InstanceSpec(self): # String
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self, InstanceSpec):  # String
		self.add_query_param('InstanceSpec', InstanceSpec)
	def get_Token(self): # String
		return self.get_query_params().get('Token')

	def set_Token(self, Token):  # String
		self.add_query_param('Token', Token)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ModifyAction(self): # String
		return self.get_query_params().get('ModifyAction')

	def set_ModifyAction(self, ModifyAction):  # String
		self.add_query_param('ModifyAction', ModifyAction)
