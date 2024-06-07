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

class EditRecognizeRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'EditRecognizeRule')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_level(self): # String
		return self.get_body_params().get('level')

	def set_level(self, level):  # String
		self.add_body_params('level', level)
	def get_ColScan(self): # String
		return self.get_body_params().get('ColScan')

	def set_ColScan(self, ColScan):  # String
		self.add_body_params('ColScan', ColScan)
	def get_ColExclude(self): # String
		return self.get_body_params().get('ColExclude')

	def set_ColExclude(self, ColExclude):  # String
		self.add_body_params('ColExclude', ColExclude)
	def get_ContentScan(self): # String
		return self.get_body_params().get('ContentScan')

	def set_ContentScan(self, ContentScan):  # String
		self.add_body_params('ContentScan', ContentScan)
	def get_OperationType(self): # Integer
		return self.get_body_params().get('OperationType')

	def set_OperationType(self, OperationType):  # Integer
		self.add_body_params('OperationType', OperationType)
	def get_TemplateId(self): # String
		return self.get_body_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_body_params('TemplateId', TemplateId)
	def get_RecognizeRulesType(self): # String
		return self.get_body_params().get('RecognizeRulesType')

	def set_RecognizeRulesType(self, RecognizeRulesType):  # String
		self.add_body_params('RecognizeRulesType', RecognizeRulesType)
	def get_CommentScan(self): # String
		return self.get_body_params().get('CommentScan')

	def set_CommentScan(self, CommentScan):  # String
		self.add_body_params('CommentScan', CommentScan)
	def get_AccountName(self): # String
		return self.get_body_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_body_params('AccountName', AccountName)
	def get_SensitiveDescription(self): # String
		return self.get_body_params().get('SensitiveDescription')

	def set_SensitiveDescription(self, SensitiveDescription):  # String
		self.add_body_params('SensitiveDescription', SensitiveDescription)
	def get_SensitiveId(self): # String
		return self.get_body_params().get('SensitiveId')

	def set_SensitiveId(self, SensitiveId):  # String
		self.add_body_params('SensitiveId', SensitiveId)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_RecognizeRules(self): # String
		return self.get_body_params().get('RecognizeRules')

	def set_RecognizeRules(self, RecognizeRules):  # String
		self.add_body_params('RecognizeRules', RecognizeRules)
	def get_HitThreshold(self): # Integer
		return self.get_body_params().get('HitThreshold')

	def set_HitThreshold(self, HitThreshold):  # Integer
		self.add_body_params('HitThreshold', HitThreshold)
	def get_SensitiveName(self): # String
		return self.get_body_params().get('SensitiveName')

	def set_SensitiveName(self, SensitiveName):  # String
		self.add_body_params('SensitiveName', SensitiveName)
	def get_NodeParent(self): # String
		return self.get_body_params().get('NodeParent')

	def set_NodeParent(self, NodeParent):  # String
		self.add_body_params('NodeParent', NodeParent)
	def get_LevelName(self): # String
		return self.get_body_params().get('LevelName')

	def set_LevelName(self, LevelName):  # String
		self.add_body_params('LevelName', LevelName)
	def get_NodeId(self): # String
		return self.get_body_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_body_params('NodeId', NodeId)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
