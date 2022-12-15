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

class CreateSDKInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'viapi-oxs-cross', '2020-07-01', 'CreateSDKInstance')
		self.set_method('POST')

	def get_Recipe(self): # String
		return self.get_query_params().get('Recipe')

	def set_Recipe(self, Recipe):  # String
		self.add_query_param('Recipe', Recipe)
	def get_BundleId(self): # String
		return self.get_query_params().get('BundleId')

	def set_BundleId(self, BundleId):  # String
		self.add_query_param('BundleId', BundleId)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_ValidFrom(self): # Long
		return self.get_query_params().get('ValidFrom')

	def set_ValidFrom(self, ValidFrom):  # Long
		self.add_query_param('ValidFrom', ValidFrom)
	def get_Pk(self): # String
		return self.get_query_params().get('Pk')

	def set_Pk(self, Pk):  # String
		self.add_query_param('Pk', Pk)
	def get_ValidTo(self): # Long
		return self.get_query_params().get('ValidTo')

	def set_ValidTo(self, ValidTo):  # Long
		self.add_query_param('ValidTo', ValidTo)
