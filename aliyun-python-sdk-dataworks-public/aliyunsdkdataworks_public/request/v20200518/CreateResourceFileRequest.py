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

class CreateResourceFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateResourceFile')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FileType(self): # Integer
		return self.get_body_params().get('FileType')

	def set_FileType(self, FileType):  # Integer
		self.add_body_params('FileType', FileType)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
	def get_ResourceFile(self): # String
		return self.get_body_params().get('ResourceFile')

	def set_ResourceFile(self, ResourceFile):  # String
		self.add_body_params('ResourceFile', ResourceFile)
	def get_OriginResourceName(self): # String
		return self.get_body_params().get('OriginResourceName')

	def set_OriginResourceName(self, OriginResourceName):  # String
		self.add_body_params('OriginResourceName', OriginResourceName)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_StorageURL(self): # String
		return self.get_body_params().get('StorageURL')

	def set_StorageURL(self, StorageURL):  # String
		self.add_body_params('StorageURL', StorageURL)
	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_RegisterToCalcEngine(self): # Boolean
		return self.get_body_params().get('RegisterToCalcEngine')

	def set_RegisterToCalcEngine(self, RegisterToCalcEngine):  # Boolean
		self.add_body_params('RegisterToCalcEngine', RegisterToCalcEngine)
	def get_UploadMode(self): # Boolean
		return self.get_body_params().get('UploadMode')

	def set_UploadMode(self, UploadMode):  # Boolean
		self.add_body_params('UploadMode', UploadMode)
	def get_FileName(self): # String
		return self.get_body_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_body_params('FileName', FileName)
	def get_FileFolderPath(self): # String
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self, FileFolderPath):  # String
		self.add_body_params('FileFolderPath', FileFolderPath)
	def get_FileDescription(self): # String
		return self.get_body_params().get('FileDescription')

	def set_FileDescription(self, FileDescription):  # String
		self.add_body_params('FileDescription', FileDescription)
