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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class UpdateQualityRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateQualityRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Trend(self): # String
		return self.get_body_params().get('Trend')

	def set_Trend(self, Trend):  # String
		self.add_body_params('Trend', Trend)
	def get_BlockType(self): # Integer
		return self.get_body_params().get('BlockType')

	def set_BlockType(self, BlockType):  # Integer
		self.add_body_params('BlockType', BlockType)
	def get_PropertyType(self): # String
		return self.get_body_params().get('PropertyType')

	def set_PropertyType(self, PropertyType):  # String
		self.add_body_params('PropertyType', PropertyType)
	def get_EntityId(self): # Long
		return self.get_body_params().get('EntityId')

	def set_EntityId(self, EntityId):  # Long
		self.add_body_params('EntityId', EntityId)
	def get_RuleName(self): # String
		return self.get_body_params().get('RuleName')

	def set_RuleName(self, RuleName):  # String
		self.add_body_params('RuleName', RuleName)
	def get_Checker(self): # Integer
		return self.get_body_params().get('Checker')

	def set_Checker(self, Checker):  # Integer
		self.add_body_params('Checker', Checker)
	def get_Operator(self): # String
		return self.get_body_params().get('Operator')

	def set_Operator(self, Operator):  # String
		self.add_body_params('Operator', Operator)
	def get_Property(self): # String
		return self.get_body_params().get('Property')

	def set_Property(self, Property):  # String
		self.add_body_params('Property', Property)
	def get_Id(self): # Long
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_body_params('Id', Id)
	def get_WarningThreshold(self): # String
		return self.get_body_params().get('WarningThreshold')

	def set_WarningThreshold(self, WarningThreshold):  # String
		self.add_body_params('WarningThreshold', WarningThreshold)
	def get_MethodName(self): # String
		return self.get_body_params().get('MethodName')

	def set_MethodName(self, MethodName):  # String
		self.add_body_params('MethodName', MethodName)
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_RuleType(self): # Integer
		return self.get_body_params().get('RuleType')

	def set_RuleType(self, RuleType):  # Integer
		self.add_body_params('RuleType', RuleType)
	def get_TemplateId(self): # Integer
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # Integer
		self.add_body_params('TemplateId', TemplateId)
	def get_ExpectValue(self): # String
		return self.get_body_params().get('ExpectValue')

	def set_ExpectValue(self, ExpectValue):  # String
		self.add_body_params('ExpectValue', ExpectValue)
	def get_WhereCondition(self): # String
		return self.get_body_params().get('WhereCondition')

	def set_WhereCondition(self, WhereCondition):  # String
		self.add_body_params('WhereCondition', WhereCondition)
	def get_CriticalThreshold(self): # String
		return self.get_body_params().get('CriticalThreshold')

	def set_CriticalThreshold(self, CriticalThreshold):  # String
		self.add_body_params('CriticalThreshold', CriticalThreshold)
	def get_OpenSwitch(self): # Boolean
		return self.get_body_params().get('OpenSwitch')

	def set_OpenSwitch(self, OpenSwitch):  # Boolean
		self.add_body_params('OpenSwitch', OpenSwitch)
	def get_Comment(self): # String
		return self.get_body_params().get('Comment')

	def set_Comment(self, Comment):  # String
		self.add_body_params('Comment', Comment)
	def get_PredictType(self): # Integer
		return self.get_body_params().get('PredictType')

	def set_PredictType(self, PredictType):  # Integer
		self.add_body_params('PredictType', PredictType)
