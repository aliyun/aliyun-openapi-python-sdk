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

from aliyunsdkcore.request import RpcRequest
class CreateDocIndexTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'CreateDocIndexTask','imm')

	def get_CustomKey1(self):
		return self.get_query_params().get('CustomKey1')

	def set_CustomKey1(self,CustomKey1):
		self.add_query_param('CustomKey1',CustomKey1)

	def get_Set(self):
		return self.get_query_params().get('Set')

	def set_Set(self,Set):
		self.add_query_param('Set',Set)

	def get_CustomKey5(self):
		return self.get_query_params().get('CustomKey5')

	def set_CustomKey5(self,CustomKey5):
		self.add_query_param('CustomKey5',CustomKey5)

	def get_CustomKey4(self):
		return self.get_query_params().get('CustomKey4')

	def set_CustomKey4(self,CustomKey4):
		self.add_query_param('CustomKey4',CustomKey4)

	def get_CustomKey3(self):
		return self.get_query_params().get('CustomKey3')

	def set_CustomKey3(self,CustomKey3):
		self.add_query_param('CustomKey3',CustomKey3)

	def get_CustomKey2(self):
		return self.get_query_params().get('CustomKey2')

	def set_CustomKey2(self,CustomKey2):
		self.add_query_param('CustomKey2',CustomKey2)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_CustomKey6(self):
		return self.get_query_params().get('CustomKey6')

	def set_CustomKey6(self,CustomKey6):
		self.add_query_param('CustomKey6',CustomKey6)

	def get_ContentType(self):
		return self.get_query_params().get('ContentType')

	def set_ContentType(self,ContentType):
		self.add_query_param('ContentType',ContentType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_SrcUri(self):
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self,SrcUri):
		self.add_query_param('SrcUri',SrcUri)

	def get_UniqueId(self):
		return self.get_query_params().get('UniqueId')

	def set_UniqueId(self,UniqueId):
		self.add_query_param('UniqueId',UniqueId)