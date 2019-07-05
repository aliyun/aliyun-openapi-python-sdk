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


class SaveSingleTaskForSaveArtExtensionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveSingleTaskForSaveArtExtension')

	def get_Reference(self):
		return self.get_query_params().get('Reference')

	def set_Reference(self,Reference):
		self.add_query_param('Reference',Reference)

	def get_Features(self):
		return self.get_query_params().get('Features')

	def set_Features(self,Features):
		self.add_query_param('Features',Features)

	def get_InscriptionsAndMarkings(self):
		return self.get_query_params().get('InscriptionsAndMarkings')

	def set_InscriptionsAndMarkings(self,InscriptionsAndMarkings):
		self.add_query_param('InscriptionsAndMarkings',InscriptionsAndMarkings)

	def get_Subject(self):
		return self.get_query_params().get('Subject')

	def set_Subject(self,Subject):
		self.add_query_param('Subject',Subject)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_Maker(self):
		return self.get_query_params().get('Maker')

	def set_Maker(self,Maker):
		self.add_query_param('Maker',Maker)

	def get_ObjectType(self):
		return self.get_query_params().get('ObjectType')

	def set_ObjectType(self,ObjectType):
		self.add_query_param('ObjectType',ObjectType)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_MaterialsAndTechniques(self):
		return self.get_query_params().get('MaterialsAndTechniques')

	def set_MaterialsAndTechniques(self,MaterialsAndTechniques):
		self.add_query_param('MaterialsAndTechniques',MaterialsAndTechniques)

	def get_DateOrPeriod(self):
		return self.get_query_params().get('DateOrPeriod')

	def set_DateOrPeriod(self,DateOrPeriod):
		self.add_query_param('DateOrPeriod',DateOrPeriod)

	def get_Dimensions(self):
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self,Dimensions):
		self.add_query_param('Dimensions',Dimensions)