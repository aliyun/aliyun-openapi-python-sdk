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
from aliyunsdkdomain.endpoint import endpoint_data

class SaveSingleTaskForSaveArtExtensionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveSingleTaskForSaveArtExtension','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Subject(self): # String
		return self.get_query_params().get('Subject')

	def set_Subject(self, Subject):  # String
		self.add_query_param('Subject', Subject)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_DateOrPeriod(self): # String
		return self.get_query_params().get('DateOrPeriod')

	def set_DateOrPeriod(self, DateOrPeriod):  # String
		self.add_query_param('DateOrPeriod', DateOrPeriod)
	def get_Reference(self): # String
		return self.get_query_params().get('Reference')

	def set_Reference(self, Reference):  # String
		self.add_query_param('Reference', Reference)
	def get_Features(self): # String
		return self.get_query_params().get('Features')

	def set_Features(self, Features):  # String
		self.add_query_param('Features', Features)
	def get_InscriptionsAndMarkings(self): # String
		return self.get_query_params().get('InscriptionsAndMarkings')

	def set_InscriptionsAndMarkings(self, InscriptionsAndMarkings):  # String
		self.add_query_param('InscriptionsAndMarkings', InscriptionsAndMarkings)
	def get_ObjectType(self): # String
		return self.get_query_params().get('ObjectType')

	def set_ObjectType(self, ObjectType):  # String
		self.add_query_param('ObjectType', ObjectType)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_Maker(self): # String
		return self.get_query_params().get('Maker')

	def set_Maker(self, Maker):  # String
		self.add_query_param('Maker', Maker)
	def get_MaterialsAndTechniques(self): # String
		return self.get_query_params().get('MaterialsAndTechniques')

	def set_MaterialsAndTechniques(self, MaterialsAndTechniques):  # String
		self.add_query_param('MaterialsAndTechniques', MaterialsAndTechniques)
	def get_Dimensions(self): # String
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self, Dimensions):  # String
		self.add_query_param('Dimensions', Dimensions)
