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

class DescribePlaybooksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'DescribePlaybooks')
		self.set_protocol_type('https')
		self.set_method('GET')

	def get_EndMillis(self): # Long
		return self.get_query_params().get('EndMillis')

	def set_EndMillis(self, EndMillis):  # Long
		self.add_query_param('EndMillis', EndMillis)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_PlaybookUuids(self): # String
		return self.get_query_params().get('PlaybookUuids')

	def set_PlaybookUuids(self, PlaybookUuids):  # String
		self.add_query_param('PlaybookUuids', PlaybookUuids)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
	def get_ParamTypes(self): # String
		return self.get_query_params().get('ParamTypes')

	def set_ParamTypes(self, ParamTypes):  # String
		self.add_query_param('ParamTypes', ParamTypes)
	def get_Active(self): # Integer
		return self.get_query_params().get('Active')

	def set_Active(self, Active):  # Integer
		self.add_query_param('Active', Active)
	def get_OwnType(self): # String
		return self.get_query_params().get('OwnType')

	def set_OwnType(self, OwnType):  # String
		self.add_query_param('OwnType', OwnType)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_StartMillis(self): # Long
		return self.get_query_params().get('StartMillis')

	def set_StartMillis(self, StartMillis):  # Long
		self.add_query_param('StartMillis', StartMillis)
	def get_PlaybookUuid(self): # String
		return self.get_query_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_query_param('PlaybookUuid', PlaybookUuid)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
