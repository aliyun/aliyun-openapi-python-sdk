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
from aliyunsdkehpc.endpoint import endpoint_data

class CreateJobTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2017-07-14', 'CreateJobTemplate')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StderrRedirectPath(self): # String
		return self.get_query_params().get('StderrRedirectPath')

	def set_StderrRedirectPath(self, StderrRedirectPath):  # String
		self.add_query_param('StderrRedirectPath', StderrRedirectPath)
	def get_CommandLine(self): # String
		return self.get_query_params().get('CommandLine')

	def set_CommandLine(self, CommandLine):  # String
		self.add_query_param('CommandLine', CommandLine)
	def get_ArrayRequest(self): # String
		return self.get_query_params().get('ArrayRequest')

	def set_ArrayRequest(self, ArrayRequest):  # String
		self.add_query_param('ArrayRequest', ArrayRequest)
	def get_PackagePath(self): # String
		return self.get_query_params().get('PackagePath')

	def set_PackagePath(self, PackagePath):  # String
		self.add_query_param('PackagePath', PackagePath)
	def get_StdoutRedirectPath(self): # String
		return self.get_query_params().get('StdoutRedirectPath')

	def set_StdoutRedirectPath(self, StdoutRedirectPath):  # String
		self.add_query_param('StdoutRedirectPath', StdoutRedirectPath)
	def get_Variables(self): # String
		return self.get_query_params().get('Variables')

	def set_Variables(self, Variables):  # String
		self.add_query_param('Variables', Variables)
	def get_RunasUser(self): # String
		return self.get_query_params().get('RunasUser')

	def set_RunasUser(self, RunasUser):  # String
		self.add_query_param('RunasUser', RunasUser)
	def get_ReRunable(self): # Boolean
		return self.get_query_params().get('ReRunable')

	def set_ReRunable(self, ReRunable):  # Boolean
		self.add_query_param('ReRunable', ReRunable)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
