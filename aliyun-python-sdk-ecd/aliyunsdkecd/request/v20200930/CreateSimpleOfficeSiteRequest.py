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

class CreateSimpleOfficeSiteRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'CreateSimpleOfficeSite')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_CenOwnerId(self): # Long
		return self.get_query_params().get('CenOwnerId')

	def set_CenOwnerId(self, CenOwnerId):  # Long
		self.add_query_param('CenOwnerId', CenOwnerId)
	def get_EnableInternetAccess(self): # Boolean
		return self.get_query_params().get('EnableInternetAccess')

	def set_EnableInternetAccess(self, EnableInternetAccess):  # Boolean
		self.add_query_param('EnableInternetAccess', EnableInternetAccess)
	def get_VerifyCode(self): # String
		return self.get_query_params().get('VerifyCode')

	def set_VerifyCode(self, VerifyCode):  # String
		self.add_query_param('VerifyCode', VerifyCode)
	def get_NeedVerifyZeroDevice(self): # Boolean
		return self.get_query_params().get('NeedVerifyZeroDevice')

	def set_NeedVerifyZeroDevice(self, NeedVerifyZeroDevice):  # Boolean
		self.add_query_param('NeedVerifyZeroDevice', NeedVerifyZeroDevice)
	def get_EnableAdminAccess(self): # Boolean
		return self.get_query_params().get('EnableAdminAccess')

	def set_EnableAdminAccess(self, EnableAdminAccess):  # Boolean
		self.add_query_param('EnableAdminAccess', EnableAdminAccess)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_DesktopAccessType(self): # String
		return self.get_query_params().get('DesktopAccessType')

	def set_DesktopAccessType(self, DesktopAccessType):  # String
		self.add_query_param('DesktopAccessType', DesktopAccessType)
	def get_OfficeSiteName(self): # String
		return self.get_query_params().get('OfficeSiteName')

	def set_OfficeSiteName(self, OfficeSiteName):  # String
		self.add_query_param('OfficeSiteName', OfficeSiteName)
	def get_CloudBoxOfficeSite(self): # Boolean
		return self.get_query_params().get('CloudBoxOfficeSite')

	def set_CloudBoxOfficeSite(self, CloudBoxOfficeSite):  # Boolean
		self.add_query_param('CloudBoxOfficeSite', CloudBoxOfficeSite)
	def get_VSwitchIds(self): # RepeatList
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchIds(self, VSwitchId):  # RepeatList
		for depth1 in range(len(VSwitchId)):
			self.add_query_param('VSwitchId.' + str(depth1 + 1), VSwitchId[depth1])
	def get_CidrBlock(self): # String
		return self.get_query_params().get('CidrBlock')

	def set_CidrBlock(self, CidrBlock):  # String
		self.add_query_param('CidrBlock', CidrBlock)
