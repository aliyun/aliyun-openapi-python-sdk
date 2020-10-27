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


	def get_Trend(self):
		return self.get_body_params().get('Trend')

	def set_Trend(self,Trend):
		self.add_body_params('Trend', Trend)

	def get_BlockType(self):
		return self.get_body_params().get('BlockType')

	def set_BlockType(self,BlockType):
		self.add_body_params('BlockType', BlockType)

	def get_PropertyType(self):
		return self.get_body_params().get('PropertyType')

	def set_PropertyType(self,PropertyType):
		self.add_body_params('PropertyType', PropertyType)

	def get_EntityId(self):
		return self.get_body_params().get('EntityId')

	def set_EntityId(self,EntityId):
		self.add_body_params('EntityId', EntityId)

	def get_RuleName(self):
		return self.get_body_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_body_params('RuleName', RuleName)

	def get_Checker(self):
		return self.get_body_params().get('Checker')

	def set_Checker(self,Checker):
		self.add_body_params('Checker', Checker)

	def get_Operator(self):
		return self.get_body_params().get('Operator')

	def set_Operator(self,Operator):
		self.add_body_params('Operator', Operator)

	def get_Property(self):
		return self.get_body_params().get('Property')

	def set_Property(self,Property):
		self.add_body_params('Property', Property)

	def get_Id(self):
		return self.get_body_params().get('Id')

	def set_Id(self,Id):
		self.add_body_params('Id', Id)

	def get_WarningThreshold(self):
		return self.get_body_params().get('WarningThreshold')

	def set_WarningThreshold(self,WarningThreshold):
		self.add_body_params('WarningThreshold', WarningThreshold)

	def get_MethodName(self):
		return self.get_body_params().get('MethodName')

	def set_MethodName(self,MethodName):
		self.add_body_params('MethodName', MethodName)

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_RuleType(self):
		return self.get_body_params().get('RuleType')

	def set_RuleType(self,RuleType):
		self.add_body_params('RuleType', RuleType)

	def get_TemplateId(self):
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_body_params('TemplateId', TemplateId)

	def get_ExpectValue(self):
		return self.get_body_params().get('ExpectValue')

	def set_ExpectValue(self,ExpectValue):
		self.add_body_params('ExpectValue', ExpectValue)

	def get_WhereCondition(self):
		return self.get_body_params().get('WhereCondition')

	def set_WhereCondition(self,WhereCondition):
		self.add_body_params('WhereCondition', WhereCondition)

	def get_CriticalThreshold(self):
		return self.get_body_params().get('CriticalThreshold')

	def set_CriticalThreshold(self,CriticalThreshold):
		self.add_body_params('CriticalThreshold', CriticalThreshold)

	def get_Comment(self):
		return self.get_body_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_body_params('Comment', Comment)

	def get_PredictType(self):
		return self.get_body_params().get('PredictType')

	def set_PredictType(self,PredictType):
		self.add_body_params('PredictType', PredictType)