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
from aliyunsdkrds.endpoint import endpoint_data
import json

class RunRCCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'RunRCCommand','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceTags(self): # Array
		return self.get_query_params().get('ResourceTags')

	def set_ResourceTags(self, ResourceTags):  # Array
		self.add_query_param("ResourceTags", json.dumps(ResourceTags))
	def get_ContainerName(self): # String
		return self.get_query_params().get('ContainerName')

	def set_ContainerName(self, ContainerName):  # String
		self.add_query_param('ContainerName', ContainerName)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_WorkingDir(self): # String
		return self.get_query_params().get('WorkingDir')

	def set_WorkingDir(self, WorkingDir):  # String
		self.add_query_param('WorkingDir', WorkingDir)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_CommandContent(self): # String
		return self.get_query_params().get('CommandContent')

	def set_CommandContent(self, CommandContent):  # String
		self.add_query_param('CommandContent', CommandContent)
	def get_Timeout(self): # Long
		return self.get_query_params().get('Timeout')

	def set_Timeout(self, Timeout):  # Long
		self.add_query_param('Timeout', Timeout)
	def get_Frequency(self): # String
		return self.get_query_params().get('Frequency')

	def set_Frequency(self, Frequency):  # String
		self.add_query_param('Frequency', Frequency)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ContentEncoding(self): # String
		return self.get_query_params().get('ContentEncoding')

	def set_ContentEncoding(self, ContentEncoding):  # String
		self.add_query_param('ContentEncoding', ContentEncoding)
	def get_RepeatMode(self): # String
		return self.get_query_params().get('RepeatMode')

	def set_RepeatMode(self, RepeatMode):  # String
		self.add_query_param('RepeatMode', RepeatMode)
	def get_WindowsPasswordName(self): # String
		return self.get_query_params().get('WindowsPasswordName')

	def set_WindowsPasswordName(self, WindowsPasswordName):  # String
		self.add_query_param('WindowsPasswordName', WindowsPasswordName)
	def get_KeepCommand(self): # Boolean
		return self.get_query_params().get('KeepCommand')

	def set_KeepCommand(self, KeepCommand):  # Boolean
		self.add_query_param('KeepCommand', KeepCommand)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		self.add_query_param("Tags", json.dumps(Tags))
	def get_TerminationMode(self): # String
		return self.get_query_params().get('TerminationMode')

	def set_TerminationMode(self, TerminationMode):  # String
		self.add_query_param('TerminationMode', TerminationMode)
	def get_InstanceIds(self): # Array
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # Array
		self.add_query_param("InstanceIds", json.dumps(InstanceIds))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ContainerId(self): # String
		return self.get_query_params().get('ContainerId')

	def set_ContainerId(self, ContainerId):  # String
		self.add_query_param('ContainerId', ContainerId)
	def get_Parameters(self): # Map
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # Map
		self.add_query_param("Parameters", json.dumps(Parameters))
	def get_EnableParameter(self): # Boolean
		return self.get_query_params().get('EnableParameter')

	def set_EnableParameter(self, EnableParameter):  # Boolean
		self.add_query_param('EnableParameter', EnableParameter)
	def get_Username(self): # String
		return self.get_query_params().get('Username')

	def set_Username(self, Username):  # String
		self.add_query_param('Username', Username)
	def get_Launcher(self): # String
		return self.get_query_params().get('Launcher')

	def set_Launcher(self, Launcher):  # String
		self.add_query_param('Launcher', Launcher)
