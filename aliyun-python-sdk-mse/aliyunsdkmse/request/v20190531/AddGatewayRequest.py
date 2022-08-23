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
from aliyunsdkmse.endpoint import endpoint_data

class AddGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'AddGateway','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_InternetSlbSpec(self): # String
		return self.get_query_params().get('InternetSlbSpec')

	def set_InternetSlbSpec(self, InternetSlbSpec):  # String
		self.add_query_param('InternetSlbSpec', InternetSlbSpec)
	def get_EnableXtrace(self): # Boolean
		return self.get_query_params().get('EnableXtrace')

	def set_EnableXtrace(self, EnableXtrace):  # Boolean
		self.add_query_param('EnableXtrace', EnableXtrace)
	def get_XtraceRatio(self): # String
		return self.get_query_params().get('XtraceRatio')

	def set_XtraceRatio(self, XtraceRatio):  # String
		self.add_query_param('XtraceRatio', XtraceRatio)
	def get_Replica(self): # Integer
		return self.get_query_params().get('Replica')

	def set_Replica(self, Replica):  # Integer
		self.add_query_param('Replica', Replica)
	def get_VSwitchId2(self): # String
		return self.get_query_params().get('VSwitchId2')

	def set_VSwitchId2(self, VSwitchId2):  # String
		self.add_query_param('VSwitchId2', VSwitchId2)
	def get_EnableHardwareAcceleration(self): # Boolean
		return self.get_query_params().get('EnableHardwareAcceleration')

	def set_EnableHardwareAcceleration(self, EnableHardwareAcceleration):  # Boolean
		self.add_query_param('EnableHardwareAcceleration', EnableHardwareAcceleration)
	def get_EnableSls(self): # Boolean
		return self.get_query_params().get('EnableSls')

	def set_EnableSls(self, EnableSls):  # Boolean
		self.add_query_param('EnableSls', EnableSls)
	def get_Spec(self): # String
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # String
		self.add_query_param('Spec', Spec)
	def get_EnterpriseSecurityGroup(self): # Boolean
		return self.get_query_params().get('EnterpriseSecurityGroup')

	def set_EnterpriseSecurityGroup(self, EnterpriseSecurityGroup):  # Boolean
		self.add_query_param('EnterpriseSecurityGroup', EnterpriseSecurityGroup)
	def get_Vpc(self): # String
		return self.get_query_params().get('Vpc')

	def set_Vpc(self, Vpc):  # String
		self.add_query_param('Vpc', Vpc)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_SlbSpec(self): # String
		return self.get_query_params().get('SlbSpec')

	def set_SlbSpec(self, SlbSpec):  # String
		self.add_query_param('SlbSpec', SlbSpec)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
