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

class UpdateUdfFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateUdfFile')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ReturnValue(self):
		return self.get_body_params().get('ReturnValue')

	def set_ReturnValue(self,ReturnValue):
		self.add_body_params('ReturnValue', ReturnValue)

	def get_Resources(self):
		return self.get_body_params().get('Resources')

	def set_Resources(self,Resources):
		self.add_body_params('Resources', Resources)

	def get_FunctionType(self):
		return self.get_body_params().get('FunctionType')

	def set_FunctionType(self,FunctionType):
		self.add_body_params('FunctionType', FunctionType)

	def get_CmdDescription(self):
		return self.get_body_params().get('CmdDescription')

	def set_CmdDescription(self,CmdDescription):
		self.add_body_params('CmdDescription', CmdDescription)

	def get_UdfDescription(self):
		return self.get_body_params().get('UdfDescription')

	def set_UdfDescription(self,UdfDescription):
		self.add_body_params('UdfDescription', UdfDescription)

	def get_ParameterDescription(self):
		return self.get_body_params().get('ParameterDescription')

	def set_ParameterDescription(self,ParameterDescription):
		self.add_body_params('ParameterDescription', ParameterDescription)

	def get_ProjectIdentifier(self):
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self,ProjectIdentifier):
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)

	def get_Example(self):
		return self.get_body_params().get('Example')

	def set_Example(self,Example):
		self.add_body_params('Example', Example)

	def get_ClassName(self):
		return self.get_body_params().get('ClassName')

	def set_ClassName(self,ClassName):
		self.add_body_params('ClassName', ClassName)

	def get_FileFolderPath(self):
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self,FileFolderPath):
		self.add_body_params('FileFolderPath', FileFolderPath)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_FileId(self):
		return self.get_body_params().get('FileId')

	def set_FileId(self,FileId):
		self.add_body_params('FileId', FileId)