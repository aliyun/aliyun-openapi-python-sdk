# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
class ListApisRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ProductCatalog', '2018-09-18', 'ListApis')
		self.set_uri_pattern('/products/some_tests/public/[ProductId]/versions/[VersionId]/apis/')
		self.set_method('GET')

	def get_VersionId(self):
		return self.get_path_params().get('VersionId')

	def set_VersionId(self,VersionId):
		self.add_path_param('VersionId',VersionId)

	def get_ProductId(self):
		return self.get_path_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_path_param('ProductId',ProductId)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_Language(self):
		return self.get_query_params().get('Language')

	def set_Language(self,Language):
		self.add_query_param('Language',Language)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)