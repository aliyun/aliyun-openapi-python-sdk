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

class PunishResourceSearchRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'PunishResourceSearch')
		self.set_method('GET')

	def get_SourceCodes(self): # Array
		return self.get_query_params().get('SourceCodes')

	def set_SourceCodes(self, SourceCodes):  # Array
		self.add_query_param("SourceCodes", json.dumps(SourceCodes))
	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_StartDate(self): # Long
		return self.get_query_params().get('StartDate')

	def set_StartDate(self, StartDate):  # Long
		self.add_query_param('StartDate', StartDate)
	def get_ActionCodes(self): # Array
		return self.get_query_params().get('ActionCodes')

	def set_ActionCodes(self, ActionCodes):  # Array
		self.add_query_param("ActionCodes", json.dumps(ActionCodes))
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_EndDate(self): # Long
		return self.get_query_params().get('EndDate')

	def set_EndDate(self, EndDate):  # Long
		self.add_query_param('EndDate', EndDate)
	def get_UserIds(self): # Array
		return self.get_query_params().get('UserIds')

	def set_UserIds(self, UserIds):  # Array
		self.add_query_param("UserIds", json.dumps(UserIds))
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_BussinessCodes(self): # Array
		return self.get_query_params().get('BussinessCodes')

	def set_BussinessCodes(self, BussinessCodes):  # Array
		self.add_query_param("BussinessCodes", json.dumps(BussinessCodes))
	def get_Page(self): # Long
		return self.get_query_params().get('Page')

	def set_Page(self, Page):  # Long
		self.add_query_param('Page', Page)
	def get_Class(self): # String
		return self.get_query_params().get('Class')

	def set_Class(self, _Class):  # String
		self.add_query_param('Class', _Class)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
