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
from aliyunsdksddp.endpoint import endpoint_data

class ModifyRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'ModifyRule','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WarnLevel(self): # Integer
		return self.get_query_params().get('WarnLevel')

	def set_WarnLevel(self, WarnLevel):  # Integer
		self.add_query_param('WarnLevel', WarnLevel)
	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_ProductId(self): # Long
		return self.get_query_params().get('ProductId')

	def set_ProductId(self, ProductId):  # Long
		self.add_query_param('ProductId', ProductId)
	def get_RiskLevelId(self): # Long
		return self.get_query_params().get('RiskLevelId')

	def set_RiskLevelId(self, RiskLevelId):  # Long
		self.add_query_param('RiskLevelId', RiskLevelId)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_RuleType(self): # Integer
		return self.get_query_params().get('RuleType')

	def set_RuleType(self, RuleType):  # Integer
		self.add_query_param('RuleType', RuleType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Category(self): # Integer
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # Integer
		self.add_query_param('Category', Category)
