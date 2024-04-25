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

class UpdateIdpDepartmentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'UpdateIdpDepartment')
		self.set_method('POST')

	def get_DepartmentId(self): # String
		return self.get_query_params().get('DepartmentId')

	def set_DepartmentId(self, DepartmentId):  # String
		self.add_query_param('DepartmentId', DepartmentId)
	def get_IdpConfigId(self): # String
		return self.get_query_params().get('IdpConfigId')

	def set_IdpConfigId(self, IdpConfigId):  # String
		self.add_query_param('IdpConfigId', IdpConfigId)
	def get_DepartmentName(self): # String
		return self.get_query_params().get('DepartmentName')

	def set_DepartmentName(self, DepartmentName):  # String
		self.add_query_param('DepartmentName', DepartmentName)
