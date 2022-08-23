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
from aliyunsdkmse.endpoint import endpoint_data
import json

class CreateOrUpdateSwimmingLaneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'CreateOrUpdateSwimmingLane','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MseSessionId(self): # String
		return self.get_query_params().get('MseSessionId')

	def set_MseSessionId(self, MseSessionId):  # String
		self.add_query_param('MseSessionId', MseSessionId)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_GmtModified(self): # String
		return self.get_query_params().get('GmtModified')

	def set_GmtModified(self, GmtModified):  # String
		self.add_query_param('GmtModified', GmtModified)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_LicenseKey(self): # String
		return self.get_query_params().get('LicenseKey')

	def set_LicenseKey(self, LicenseKey):  # String
		self.add_query_param('LicenseKey', LicenseKey)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Tag(self): # String
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_query_param('Tag', Tag)
	def get_EntryRules(self): # Array
		return self.get_query_params().get('EntryRules')

	def set_EntryRules(self, EntryRules):  # Array
		self.add_query_param("EntryRules", json.dumps(EntryRules))
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_GmtCreate(self): # String
		return self.get_query_params().get('GmtCreate')

	def set_GmtCreate(self, GmtCreate):  # String
		self.add_query_param('GmtCreate', GmtCreate)
	def get_EnableRules(self): # Boolean
		return self.get_query_params().get('EnableRules')

	def set_EnableRules(self, EnableRules):  # Boolean
		self.add_query_param('EnableRules', EnableRules)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_Status(self): # Integer
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_query_param('Status', Status)
