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

class SearchPunishRecordsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'SearchPunishRecords')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_CaseCodes(self): # Array
		return self.get_query_params().get('CaseCodes')

	def set_CaseCodes(self, CaseCodes):  # Array
		self.add_query_param("CaseCodes", json.dumps(CaseCodes))
	def get_SourceCodes(self): # Array
		return self.get_query_params().get('SourceCodes')

	def set_SourceCodes(self, SourceCodes):  # Array
		self.add_query_param("SourceCodes", json.dumps(SourceCodes))
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_StartTime(self): # Long
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_query_param('StartTime', StartTime)
	def get_ActionCodes(self): # Array
		return self.get_query_params().get('ActionCodes')

	def set_ActionCodes(self, ActionCodes):  # Array
		self.add_query_param("ActionCodes", json.dumps(ActionCodes))
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_EventCodes(self): # Array
		return self.get_query_params().get('EventCodes')

	def set_EventCodes(self, EventCodes):  # Array
		self.add_query_param("EventCodes", json.dumps(EventCodes))
	def get_UrlFuzzy(self): # String
		return self.get_query_params().get('UrlFuzzy')

	def set_UrlFuzzy(self, UrlFuzzy):  # String
		self.add_query_param('UrlFuzzy', UrlFuzzy)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_BussinessCodes(self): # String
		return self.get_query_params().get('BussinessCodes')

	def set_BussinessCodes(self, BussinessCodes):  # String
		self.add_query_param('BussinessCodes', BussinessCodes)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_AliUid(self): # String
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # String
		self.add_query_param('AliUid', AliUid)
	def get_Page(self): # String
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # String
		self.add_query_param('Page', Page)
	def get_PunishStatus(self): # Array
		return self.get_query_params().get('PunishStatus')

	def set_PunishStatus(self, PunishStatus):  # Array
		self.add_query_param("PunishStatus", json.dumps(PunishStatus))
