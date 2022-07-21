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
from aliyunsdkdomain.endpoint import endpoint_data

class QueryRegistrantProfilesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'QueryRegistrantProfiles')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RegistrantProfileId(self): # Long
		return self.get_query_params().get('RegistrantProfileId')

	def set_RegistrantProfileId(self, RegistrantProfileId):  # Long
		self.add_query_param('RegistrantProfileId', RegistrantProfileId)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_RealNameStatus(self): # String
		return self.get_query_params().get('RealNameStatus')

	def set_RealNameStatus(self, RealNameStatus):  # String
		self.add_query_param('RealNameStatus', RealNameStatus)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_ZhRegistrantOrganization(self): # String
		return self.get_query_params().get('ZhRegistrantOrganization')

	def set_ZhRegistrantOrganization(self, ZhRegistrantOrganization):  # String
		self.add_query_param('ZhRegistrantOrganization', ZhRegistrantOrganization)
	def get_RegistrantType(self): # String
		return self.get_query_params().get('RegistrantType')

	def set_RegistrantType(self, RegistrantType):  # String
		self.add_query_param('RegistrantType', RegistrantType)
	def get_RegistrantProfileType(self): # String
		return self.get_query_params().get('RegistrantProfileType')

	def set_RegistrantProfileType(self, RegistrantProfileType):  # String
		self.add_query_param('RegistrantProfileType', RegistrantProfileType)
	def get_DefaultRegistrantProfile(self): # Boolean
		return self.get_query_params().get('DefaultRegistrantProfile')

	def set_DefaultRegistrantProfile(self, DefaultRegistrantProfile):  # Boolean
		self.add_query_param('DefaultRegistrantProfile', DefaultRegistrantProfile)
	def get_RegistrantOrganization(self): # String
		return self.get_query_params().get('RegistrantOrganization')

	def set_RegistrantOrganization(self, RegistrantOrganization):  # String
		self.add_query_param('RegistrantOrganization', RegistrantOrganization)
	def get_UserClientIp(self): # String
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self, UserClientIp):  # String
		self.add_query_param('UserClientIp', UserClientIp)
