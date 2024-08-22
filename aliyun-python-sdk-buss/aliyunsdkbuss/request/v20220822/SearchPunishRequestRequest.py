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
import json

class SearchPunishRequestRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'SearchPunishRequest')
		self.set_method('GET')

	def get_SourceCodes(self): # Array
		return self.get_query_params().get('SourceCodes')

	def set_SourceCodes(self, SourceCodes):  # Array
		self.add_query_param("SourceCodes", json.dumps(SourceCodes))
	def get_PunishUrl(self): # String
		return self.get_query_params().get('PunishUrl')

	def set_PunishUrl(self, PunishUrl):  # String
		self.add_query_param('PunishUrl', PunishUrl)
	def get_ExtRequestId(self): # String
		return self.get_query_params().get('ExtRequestId')

	def set_ExtRequestId(self, ExtRequestId):  # String
		self.add_query_param('ExtRequestId', ExtRequestId)
	def get_PunishStatuses(self): # Array
		return self.get_query_params().get('PunishStatuses')

	def set_PunishStatuses(self, PunishStatuses):  # Array
		self.add_query_param("PunishStatuses", json.dumps(PunishStatuses))
	def get_AntiStatuses(self): # Array
		return self.get_query_params().get('AntiStatuses')

	def set_AntiStatuses(self, AntiStatuses):  # Array
		self.add_query_param("AntiStatuses", json.dumps(AntiStatuses))
	def get_PunishUrlFull(self): # String
		return self.get_query_params().get('PunishUrlFull')

	def set_PunishUrlFull(self, PunishUrlFull):  # String
		self.add_query_param('PunishUrlFull', PunishUrlFull)
	def get_StartDate(self): # Long
		return self.get_query_params().get('StartDate')

	def set_StartDate(self, StartDate):  # Long
		self.add_query_param('StartDate', StartDate)
	def get_EventCodes(self): # Array
		return self.get_query_params().get('EventCodes')

	def set_EventCodes(self, EventCodes):  # Array
		self.add_query_param("EventCodes", json.dumps(EventCodes))
	def get_IdType(self): # String
		return self.get_query_params().get('IdType')

	def set_IdType(self, IdType):  # String
		self.add_query_param('IdType', IdType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_EndDate(self): # Long
		return self.get_query_params().get('EndDate')

	def set_EndDate(self, EndDate):  # Long
		self.add_query_param('EndDate', EndDate)
	def get_PunishIp(self): # String
		return self.get_query_params().get('PunishIp')

	def set_PunishIp(self, PunishIp):  # String
		self.add_query_param('PunishIp', PunishIp)
	def get_UserIds(self): # Array
		return self.get_query_params().get('UserIds')

	def set_UserIds(self, UserIds):  # Array
		self.add_query_param("UserIds", json.dumps(UserIds))
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_PunishDomain(self): # String
		return self.get_query_params().get('PunishDomain')

	def set_PunishDomain(self, PunishDomain):  # String
		self.add_query_param('PunishDomain', PunishDomain)
	def get_BussinessCodes(self): # Array
		return self.get_query_params().get('BussinessCodes')

	def set_BussinessCodes(self, BussinessCodes):  # Array
		self.add_query_param("BussinessCodes", json.dumps(BussinessCodes))
	def get_Page(self): # Long
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Long
		self.add_query_param('Page', Page)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Class(self): # String
		return self.get_query_params().get('Class')

	def set_Class(self, _Class):  # String
		self.add_query_param('Class', _Class)
