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
from aliyunsdkmts.endpoint import endpoint_data

class UpdateSmarttagTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'UpdateSmarttagTemplate','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_KnowledgeConfig(self): # String
		return self.get_query_params().get('KnowledgeConfig')

	def set_KnowledgeConfig(self, KnowledgeConfig):  # String
		self.add_query_param('KnowledgeConfig', KnowledgeConfig)
	def get_Industry(self): # String
		return self.get_query_params().get('Industry')

	def set_Industry(self, Industry):  # String
		self.add_query_param('Industry', Industry)
	def get_LabelVersion(self): # String
		return self.get_query_params().get('LabelVersion')

	def set_LabelVersion(self, LabelVersion):  # String
		self.add_query_param('LabelVersion', LabelVersion)
	def get_Scene(self): # String
		return self.get_query_params().get('Scene')

	def set_Scene(self, Scene):  # String
		self.add_query_param('Scene', Scene)
	def get_FaceCustomParamsConfig(self): # String
		return self.get_query_params().get('FaceCustomParamsConfig')

	def set_FaceCustomParamsConfig(self, FaceCustomParamsConfig):  # String
		self.add_query_param('FaceCustomParamsConfig', FaceCustomParamsConfig)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_IsDefault(self): # Boolean
		return self.get_query_params().get('IsDefault')

	def set_IsDefault(self, IsDefault):  # Boolean
		self.add_query_param('IsDefault', IsDefault)
	def get_FaceCategoryIds(self): # String
		return self.get_query_params().get('FaceCategoryIds')

	def set_FaceCategoryIds(self, FaceCategoryIds):  # String
		self.add_query_param('FaceCategoryIds', FaceCategoryIds)
	def get_KeywordConfig(self): # String
		return self.get_query_params().get('KeywordConfig')

	def set_KeywordConfig(self, KeywordConfig):  # String
		self.add_query_param('KeywordConfig', KeywordConfig)
	def get_LandmarkGroupIds(self): # String
		return self.get_query_params().get('LandmarkGroupIds')

	def set_LandmarkGroupIds(self, LandmarkGroupIds):  # String
		self.add_query_param('LandmarkGroupIds', LandmarkGroupIds)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_ObjectGroupIds(self): # String
		return self.get_query_params().get('ObjectGroupIds')

	def set_ObjectGroupIds(self, ObjectGroupIds):  # String
		self.add_query_param('ObjectGroupIds', ObjectGroupIds)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_AnalyseTypes(self): # String
		return self.get_query_params().get('AnalyseTypes')

	def set_AnalyseTypes(self, AnalyseTypes):  # String
		self.add_query_param('AnalyseTypes', AnalyseTypes)
	def get_LabelType(self): # String
		return self.get_query_params().get('LabelType')

	def set_LabelType(self, LabelType):  # String
		self.add_query_param('LabelType', LabelType)
