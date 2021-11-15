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
from aliyunsdkalimt.endpoint import endpoint_data

class GetTitleGenerateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2018-10-12', 'GetTitleGenerate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Language(self): # String
		return self.get_body_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_body_params('Language', Language)
	def get_Title(self): # String
		return self.get_body_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_body_params('Title', Title)
	def get_Platform(self): # String
		return self.get_body_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_body_params('Platform', Platform)
	def get_Extra(self): # String
		return self.get_body_params().get('Extra')

	def set_Extra(self, Extra):  # String
		self.add_body_params('Extra', Extra)
	def get_Attributes(self): # String
		return self.get_body_params().get('Attributes')

	def set_Attributes(self, Attributes):  # String
		self.add_body_params('Attributes', Attributes)
	def get_HotWords(self): # String
		return self.get_body_params().get('HotWords')

	def set_HotWords(self, HotWords):  # String
		self.add_body_params('HotWords', HotWords)
	def get_CategoryId(self): # String
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self, CategoryId):  # String
		self.add_body_params('CategoryId', CategoryId)
