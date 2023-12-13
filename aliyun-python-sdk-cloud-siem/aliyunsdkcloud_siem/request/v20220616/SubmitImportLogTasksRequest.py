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

class SubmitImportLogTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'SubmitImportLogTasks','cloud-siem')
		self.set_method('POST')

	def get_CloudCode(self): # String
		return self.get_body_params().get('CloudCode')

	def set_CloudCode(self, CloudCode):  # String
		self.add_body_params('CloudCode', CloudCode)
	def get_LogCodes(self): # String
		return self.get_body_params().get('LogCodes')

	def set_LogCodes(self, LogCodes):  # String
		self.add_body_params('LogCodes', LogCodes)
	def get_ProdCode(self): # String
		return self.get_body_params().get('ProdCode')

	def set_ProdCode(self, ProdCode):  # String
		self.add_body_params('ProdCode', ProdCode)
	def get_AutoImported(self): # Integer
		return self.get_body_params().get('AutoImported')

	def set_AutoImported(self, AutoImported):  # Integer
		self.add_body_params('AutoImported', AutoImported)
	def get_Accounts(self): # String
		return self.get_body_params().get('Accounts')

	def set_Accounts(self, Accounts):  # String
		self.add_body_params('Accounts', Accounts)
