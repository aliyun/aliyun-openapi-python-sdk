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
from aliyunsdkarms.endpoint import endpoint_data

class UpdateRumAppRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'UpdateRumApp','arms')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Restart(self): # Boolean
		return self.get_query_params().get('Restart')

	def set_Restart(self, Restart):  # Boolean
		self.add_query_param('Restart', Restart)
	def get_AutoRestart(self): # Boolean
		return self.get_query_params().get('AutoRestart')

	def set_AutoRestart(self, AutoRestart):  # Boolean
		self.add_query_param('AutoRestart', AutoRestart)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Pid(self): # String
		return self.get_query_params().get('Pid')

	def set_Pid(self, Pid):  # String
		self.add_query_param('Pid', Pid)
	def get_Stop(self): # Boolean
		return self.get_query_params().get('Stop')

	def set_Stop(self, Stop):  # Boolean
		self.add_query_param('Stop', Stop)
	def get_Nickname(self): # String
		return self.get_query_params().get('Nickname')

	def set_Nickname(self, Nickname):  # String
		self.add_query_param('Nickname', Nickname)
	def get_ServiceDomainOperationJson(self): # String
		return self.get_query_params().get('ServiceDomainOperationJson')

	def set_ServiceDomainOperationJson(self, ServiceDomainOperationJson):  # String
		self.add_query_param('ServiceDomainOperationJson', ServiceDomainOperationJson)
	def get_IsSubscribe(self): # Boolean
		return self.get_query_params().get('IsSubscribe')

	def set_IsSubscribe(self, IsSubscribe):  # Boolean
		self.add_query_param('IsSubscribe', IsSubscribe)
	def get_BonreeSDKConfigJson(self): # String
		return self.get_query_params().get('BonreeSDKConfigJson')

	def set_BonreeSDKConfigJson(self, BonreeSDKConfigJson):  # String
		self.add_query_param('BonreeSDKConfigJson', BonreeSDKConfigJson)
