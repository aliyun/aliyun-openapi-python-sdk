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

class ListDevopsProjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'ListDevopsProjects')
		self.set_method('POST')

	def get_SelectBy(self): # String
		return self.get_body_params().get('SelectBy')

	def set_SelectBy(self, SelectBy):  # String
		self.add_body_params('SelectBy', SelectBy)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_OrderBy(self): # String
		return self.get_body_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_body_params('OrderBy', OrderBy)
	def get_OrgId(self): # String
		return self.get_body_params().get('OrgId')

	def set_OrgId(self, OrgId):  # String
		self.add_body_params('OrgId', OrgId)
	def get_PageToken(self): # String
		return self.get_body_params().get('PageToken')

	def set_PageToken(self, PageToken):  # String
		self.add_body_params('PageToken', PageToken)
