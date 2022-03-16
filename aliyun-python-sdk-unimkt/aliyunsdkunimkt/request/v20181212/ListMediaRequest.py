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
from aliyunsdkunimkt.endpoint import endpoint_data

class ListMediaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'ListMedia')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_OriginSiteUserId(self): # String
		return self.get_query_params().get('OriginSiteUserId')

	def set_OriginSiteUserId(self, OriginSiteUserId):  # String
		self.add_query_param('OriginSiteUserId', OriginSiteUserId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_MediaName(self): # String
		return self.get_query_params().get('MediaName')

	def set_MediaName(self, MediaName):  # String
		self.add_query_param('MediaName', MediaName)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_TenantId(self): # String
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_query_param('TenantId', TenantId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_AccessStatus(self): # String
		return self.get_query_params().get('AccessStatus')

	def set_AccessStatus(self, AccessStatus):  # String
		self.add_query_param('AccessStatus', AccessStatus)
	def get_FirstScene(self): # String
		return self.get_query_params().get('FirstScene')

	def set_FirstScene(self, FirstScene):  # String
		self.add_query_param('FirstScene', FirstScene)
	def get_EndCreateTime(self): # Long
		return self.get_query_params().get('EndCreateTime')

	def set_EndCreateTime(self, EndCreateTime):  # Long
		self.add_query_param('EndCreateTime', EndCreateTime)
	def get_Business(self): # String
		return self.get_query_params().get('Business')

	def set_Business(self, Business):  # String
		self.add_query_param('Business', Business)
	def get_Os(self): # String
		return self.get_query_params().get('Os')

	def set_Os(self, Os):  # String
		self.add_query_param('Os', Os)
	def get_MediaStatus(self): # String
		return self.get_query_params().get('MediaStatus')

	def set_MediaStatus(self, MediaStatus):  # String
		self.add_query_param('MediaStatus', MediaStatus)
	def get_Environment(self): # String
		return self.get_query_params().get('Environment')

	def set_Environment(self, Environment):  # String
		self.add_query_param('Environment', Environment)
	def get_StartCreateTime(self): # Long
		return self.get_query_params().get('StartCreateTime')

	def set_StartCreateTime(self, StartCreateTime):  # Long
		self.add_query_param('StartCreateTime', StartCreateTime)
	def get_UserSite(self): # String
		return self.get_query_params().get('UserSite')

	def set_UserSite(self, UserSite):  # String
		self.add_query_param('UserSite', UserSite)
	def get_SecondScene(self): # String
		return self.get_query_params().get('SecondScene')

	def set_SecondScene(self, SecondScene):  # String
		self.add_query_param('SecondScene', SecondScene)
	def get_MediaType(self): # String
		return self.get_query_params().get('MediaType')

	def set_MediaType(self, MediaType):  # String
		self.add_query_param('MediaType', MediaType)
