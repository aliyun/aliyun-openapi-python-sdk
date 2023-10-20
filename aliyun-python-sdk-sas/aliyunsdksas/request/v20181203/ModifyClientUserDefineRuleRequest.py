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
from aliyunsdksas.endpoint import endpoint_data

class ModifyClientUserDefineRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyClientUserDefineRule','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ActionType(self): # Integer
		return self.get_query_params().get('ActionType')

	def set_ActionType(self, ActionType):  # Integer
		self.add_query_param('ActionType', ActionType)
	def get_NewFilePath(self): # String
		return self.get_query_params().get('NewFilePath')

	def set_NewFilePath(self, NewFilePath):  # String
		self.add_query_param('NewFilePath', NewFilePath)
	def get_Type(self): # Integer
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # Integer
		self.add_query_param('Type', Type)
	def get_Platform(self): # String
		return self.get_query_params().get('Platform')

	def set_Platform(self, Platform):  # String
		self.add_query_param('Platform', Platform)
	def get_RegistryKey(self): # String
		return self.get_query_params().get('RegistryKey')

	def set_RegistryKey(self, RegistryKey):  # String
		self.add_query_param('RegistryKey', RegistryKey)
	def get_Cmdline(self): # String
		return self.get_query_params().get('Cmdline')

	def set_Cmdline(self, Cmdline):  # String
		self.add_query_param('Cmdline', Cmdline)
	def get_FilePath(self): # String
		return self.get_query_params().get('FilePath')

	def set_FilePath(self, FilePath):  # String
		self.add_query_param('FilePath', FilePath)
	def get_Md5List(self): # String
		return self.get_query_params().get('Md5List')

	def set_Md5List(self, Md5List):  # String
		self.add_query_param('Md5List', Md5List)
	def get_ParentProcPath(self): # String
		return self.get_query_params().get('ParentProcPath')

	def set_ParentProcPath(self, ParentProcPath):  # String
		self.add_query_param('ParentProcPath', ParentProcPath)
	def get_Id(self): # Long
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # Long
		self.add_query_param('Id', Id)
	def get_ProcPath(self): # String
		return self.get_query_params().get('ProcPath')

	def set_ProcPath(self, ProcPath):  # String
		self.add_query_param('ProcPath', ProcPath)
	def get_ParentCmdline(self): # String
		return self.get_query_params().get('ParentCmdline')

	def set_ParentCmdline(self, ParentCmdline):  # String
		self.add_query_param('ParentCmdline', ParentCmdline)
	def get_IP(self): # String
		return self.get_query_params().get('IP')

	def set_IP(self, IP):  # String
		self.add_query_param('IP', IP)
	def get_RegistryContent(self): # String
		return self.get_query_params().get('RegistryContent')

	def set_RegistryContent(self, RegistryContent):  # String
		self.add_query_param('RegistryContent', RegistryContent)
	def get_PortStr(self): # String
		return self.get_query_params().get('PortStr')

	def set_PortStr(self, PortStr):  # String
		self.add_query_param('PortStr', PortStr)
	def get_Port(self): # Integer
		return self.get_query_params().get('Port')

	def set_Port(self, Port):  # Integer
		self.add_query_param('Port', Port)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
