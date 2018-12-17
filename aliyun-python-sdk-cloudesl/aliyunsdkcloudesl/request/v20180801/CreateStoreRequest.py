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
class CreateStoreRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2018-08-01', 'CreateStore')

	def get_CompanyId(self):
		return self.get_query_params().get('CompanyId')

	def set_CompanyId(self,CompanyId):
		self.add_query_param('CompanyId',CompanyId)

	def get_Comments(self):
		return self.get_query_params().get('Comments')

	def set_Comments(self,Comments):
		self.add_query_param('Comments',Comments)

	def get_Phone(self):
		return self.get_query_params().get('Phone')

	def set_Phone(self,Phone):
		self.add_query_param('Phone',Phone)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Groups(self):
		return self.get_query_params().get('Groups')

	def set_Groups(self,Groups):
		self.add_query_param('Groups',Groups)

	def get_OutId(self):
		return self.get_query_params().get('OutId')

	def set_OutId(self,OutId):
		self.add_query_param('OutId',OutId)

	def get_Brand(self):
		return self.get_query_params().get('Brand')

	def set_Brand(self,Brand):
		self.add_query_param('Brand',Brand)

	def get_ParentId(self):
		return self.get_query_params().get('ParentId')

	def set_ParentId(self,ParentId):
		self.add_query_param('ParentId',ParentId)