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
from aliyunsdklive.endpoint import endpoint_data

class UpdateLiveAIProduceRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveAIProduceRules','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Suffix(self): # String
		return self.get_query_params().get('Suffix')

	def set_Suffix(self, Suffix):  # String
		self.add_query_param('Suffix', Suffix)
	def get_SubtitleName(self): # String
		return self.get_query_params().get('SubtitleName')

	def set_SubtitleName(self, SubtitleName):  # String
		self.add_query_param('SubtitleName', SubtitleName)
	def get_RulesId(self): # String
		return self.get_query_params().get('RulesId')

	def set_RulesId(self, RulesId):  # String
		self.add_query_param('RulesId', RulesId)
	def get_App(self): # String
		return self.get_query_params().get('App')

	def set_App(self, App):  # String
		self.add_query_param('App', App)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_IsLazy(self): # Boolean
		return self.get_query_params().get('IsLazy')

	def set_IsLazy(self, IsLazy):  # Boolean
		self.add_query_param('IsLazy', IsLazy)
	def get_StudioName(self): # String
		return self.get_query_params().get('StudioName')

	def set_StudioName(self, StudioName):  # String
		self.add_query_param('StudioName', StudioName)
	def get_LiveTemplate(self): # String
		return self.get_query_params().get('LiveTemplate')

	def set_LiveTemplate(self, LiveTemplate):  # String
		self.add_query_param('LiveTemplate', LiveTemplate)
	def get_Domain(self): # String
		return self.get_query_params().get('Domain')

	def set_Domain(self, Domain):  # String
		self.add_query_param('Domain', Domain)
	def get_SubtitleId(self): # String
		return self.get_query_params().get('SubtitleId')

	def set_SubtitleId(self, SubtitleId):  # String
		self.add_query_param('SubtitleId', SubtitleId)
