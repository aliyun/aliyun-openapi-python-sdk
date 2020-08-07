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

class GetTitleDiagnoseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2018-10-12', 'GetTitleDiagnose','alimt')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Language(self):
		return self.get_body_params().get('Language')

	def set_Language(self,Language):
		self.add_body_params('Language', Language)

	def get_Title(self):
		return self.get_body_params().get('Title')

	def set_Title(self,Title):
		self.add_body_params('Title', Title)

	def get_Platform(self):
		return self.get_body_params().get('Platform')

	def set_Platform(self,Platform):
		self.add_body_params('Platform', Platform)

	def get_Extra(self):
		return self.get_body_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_body_params('Extra', Extra)

	def get_CategoryId(self):
		return self.get_body_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_body_params('CategoryId', CategoryId)