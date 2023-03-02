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

class AddBsnFabricBizChainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lto', '2021-07-07', 'AddBsnFabricBizChain')
		self.set_method('POST')

	def get_Remark(self): # String
		return self.get_query_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_query_param('Remark', Remark)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_AppCode(self): # String
		return self.get_query_params().get('AppCode')

	def set_AppCode(self, AppCode):  # String
		self.add_query_param('AppCode', AppCode)
	def get_NodeList(self): # String
		return self.get_query_params().get('NodeList')

	def set_NodeList(self, NodeList):  # String
		self.add_query_param('NodeList', NodeList)
	def get_UserCode(self): # String
		return self.get_query_params().get('UserCode')

	def set_UserCode(self, UserCode):  # String
		self.add_query_param('UserCode', UserCode)
