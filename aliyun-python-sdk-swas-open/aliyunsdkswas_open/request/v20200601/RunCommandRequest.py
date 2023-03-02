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
import json

class RunCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'RunCommand','SWAS-OPEN')
		self.set_method('POST')

	def get_WorkingDir(self): # String
		return self.get_query_params().get('WorkingDir')

	def set_WorkingDir(self, WorkingDir):  # String
		self.add_query_param('WorkingDir', WorkingDir)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_CommandContent(self): # String
		return self.get_query_params().get('CommandContent')

	def set_CommandContent(self, CommandContent):  # String
		self.add_query_param('CommandContent', CommandContent)
	def get_Timeout(self): # Integer
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Integer
		self.add_query_param('Timeout', Timeout)
	def get_WindowsPasswordName(self): # String
		return self.get_query_params().get('WindowsPasswordName')

	def set_WindowsPasswordName(self, WindowsPasswordName):  # String
		self.add_query_param('WindowsPasswordName', WindowsPasswordName)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_WorkingUser(self): # String
		return self.get_query_params().get('WorkingUser')

	def set_WorkingUser(self, WorkingUser):  # String
		self.add_query_param('WorkingUser', WorkingUser)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Parameters(self): # Map
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # Map
		self.add_query_param("Parameters", json.dumps(Parameters))
	def get_EnableParameter(self): # Boolean
		return self.get_query_params().get('EnableParameter')

	def set_EnableParameter(self, EnableParameter):  # Boolean
		self.add_query_param('EnableParameter', EnableParameter)
