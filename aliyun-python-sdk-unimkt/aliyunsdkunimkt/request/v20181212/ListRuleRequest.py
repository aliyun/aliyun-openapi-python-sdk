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

class ListRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'ListRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AdSlotType(self): # String
		return self.get_query_params().get('AdSlotType')

	def set_AdSlotType(self, AdSlotType):  # String
		self.add_query_param('AdSlotType', AdSlotType)
	def get_RuleName(self): # String
		return self.get_query_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_query_param('RuleName', RuleName)
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
	def get_AdSlotId(self): # String
		return self.get_query_params().get('AdSlotId')

	def set_AdSlotId(self, AdSlotId):  # String
		self.add_query_param('AdSlotId', AdSlotId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EndCreateTime(self): # Long
		return self.get_query_params().get('EndCreateTime')

	def set_EndCreateTime(self, EndCreateTime):  # Long
		self.add_query_param('EndCreateTime', EndCreateTime)
	def get_Business(self): # String
		return self.get_query_params().get('Business')

	def set_Business(self, Business):  # String
		self.add_query_param('Business', Business)
	def get_RuleType(self): # String
		return self.get_query_params().get('RuleType')

	def set_RuleType(self, RuleType):  # String
		self.add_query_param('RuleType', RuleType)
	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
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
	def get_AdSlotName(self): # String
		return self.get_query_params().get('AdSlotName')

	def set_AdSlotName(self, AdSlotName):  # String
		self.add_query_param('AdSlotName', AdSlotName)
	def get_RuleId(self): # String
		return self.get_query_params().get('RuleId')

	def set_RuleId(self, RuleId):  # String
		self.add_query_param('RuleId', RuleId)
