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
from aliyunsdkecd.endpoint import endpoint_data

class ModifyOfficeSiteAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyOfficeSiteAttribute')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OfficeSiteId(self): # String
		return self.get_query_params().get('OfficeSiteId')

	def set_OfficeSiteId(self, OfficeSiteId):  # String
		self.add_query_param('OfficeSiteId', OfficeSiteId)
	def get_DesktopAccessType(self): # String
		return self.get_query_params().get('DesktopAccessType')

	def set_DesktopAccessType(self, DesktopAccessType):  # String
		self.add_query_param('DesktopAccessType', DesktopAccessType)
	def get_OfficeSiteName(self): # String
		return self.get_query_params().get('OfficeSiteName')

	def set_OfficeSiteName(self, OfficeSiteName):  # String
		self.add_query_param('OfficeSiteName', OfficeSiteName)
	def get_NeedVerifyLoginRisk(self): # Boolean
		return self.get_query_params().get('NeedVerifyLoginRisk')

	def set_NeedVerifyLoginRisk(self, NeedVerifyLoginRisk):  # Boolean
		self.add_query_param('NeedVerifyLoginRisk', NeedVerifyLoginRisk)
	def get_NeedVerifyZeroDevice(self): # Boolean
		return self.get_query_params().get('NeedVerifyZeroDevice')

	def set_NeedVerifyZeroDevice(self, NeedVerifyZeroDevice):  # Boolean
		self.add_query_param('NeedVerifyZeroDevice', NeedVerifyZeroDevice)
