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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateUdfFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateUdfFile')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReturnValue(self): # String
		return self.get_body_params().get('ReturnValue')

	def set_ReturnValue(self, ReturnValue):  # String
		self.add_body_params('ReturnValue', ReturnValue)
	def get_Resources(self): # String
		return self.get_body_params().get('Resources')

	def set_Resources(self, Resources):  # String
		self.add_body_params('Resources', Resources)
	def get_FunctionType(self): # String
		return self.get_body_params().get('FunctionType')

	def set_FunctionType(self, FunctionType):  # String
		self.add_body_params('FunctionType', FunctionType)
	def get_CmdDescription(self): # String
		return self.get_body_params().get('CmdDescription')

	def set_CmdDescription(self, CmdDescription):  # String
		self.add_body_params('CmdDescription', CmdDescription)
	def get_UdfDescription(self): # String
		return self.get_body_params().get('UdfDescription')

	def set_UdfDescription(self, UdfDescription):  # String
		self.add_body_params('UdfDescription', UdfDescription)
	def get_ParameterDescription(self): # String
		return self.get_body_params().get('ParameterDescription')

	def set_ParameterDescription(self, ParameterDescription):  # String
		self.add_body_params('ParameterDescription', ParameterDescription)
	def get_ProjectIdentifier(self): # String
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self, ProjectIdentifier):  # String
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)
	def get_Example(self): # String
		return self.get_body_params().get('Example')

	def set_Example(self, Example):  # String
		self.add_body_params('Example', Example)
	def get_FileName(self): # String
		return self.get_body_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_body_params('FileName', FileName)
	def get_ClassName(self): # String
		return self.get_body_params().get('ClassName')

	def set_ClassName(self, ClassName):  # String
		self.add_body_params('ClassName', ClassName)
	def get_FileFolderPath(self): # String
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self, FileFolderPath):  # String
		self.add_body_params('FileFolderPath', FileFolderPath)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
