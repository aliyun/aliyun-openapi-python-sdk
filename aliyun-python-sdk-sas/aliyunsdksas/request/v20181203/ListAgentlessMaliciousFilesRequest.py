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
from aliyunsdksas.endpoint import endpoint_data

class ListAgentlessMaliciousFilesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ListAgentlessMaliciousFiles','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventId(self): # Long
		return self.get_query_params().get('EventId')

	def set_EventId(self, EventId):  # Long
		self.add_query_param('EventId', EventId)
	def get_FuzzyMaliciousName(self): # String
		return self.get_query_params().get('FuzzyMaliciousName')

	def set_FuzzyMaliciousName(self, FuzzyMaliciousName):  # String
		self.add_query_param('FuzzyMaliciousName', FuzzyMaliciousName)
	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Uuid(self): # String
		return self.get_query_params().get('Uuid')

	def set_Uuid(self, Uuid):  # String
		self.add_query_param('Uuid', Uuid)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_MaliciousMd5(self): # String
		return self.get_query_params().get('MaliciousMd5')

	def set_MaliciousMd5(self, MaliciousMd5):  # String
		self.add_query_param('MaliciousMd5', MaliciousMd5)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Dealed(self): # String
		return self.get_query_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_query_param('Dealed', Dealed)
	def get_MaliciousType(self): # String
		return self.get_query_params().get('MaliciousType')

	def set_MaliciousType(self, MaliciousType):  # String
		self.add_query_param('MaliciousType', MaliciousType)
	def get_Levels(self): # String
		return self.get_query_params().get('Levels')

	def set_Levels(self, Levels):  # String
		self.add_query_param('Levels', Levels)
