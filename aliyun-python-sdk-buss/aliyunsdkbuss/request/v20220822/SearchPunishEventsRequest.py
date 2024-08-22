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

class SearchPunishEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'SearchPunishEvents')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_CaseCodes(self): # Array
		return self.get_query_params().get('CaseCodes')

	def set_CaseCodes(self, CaseCodes):  # Array
		self.add_query_param("CaseCodes", json.dumps(CaseCodes))
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_BussinessCodes(self): # Array
		return self.get_query_params().get('BussinessCodes')

	def set_BussinessCodes(self, BussinessCodes):  # Array
		self.add_query_param("BussinessCodes", json.dumps(BussinessCodes))
	def get_AliUid(self): # String
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # String
		self.add_query_param('AliUid', AliUid)
	def get_EventCodes(self): # Array
		return self.get_query_params().get('EventCodes')

	def set_EventCodes(self, EventCodes):  # Array
		self.add_query_param("EventCodes", json.dumps(EventCodes))
