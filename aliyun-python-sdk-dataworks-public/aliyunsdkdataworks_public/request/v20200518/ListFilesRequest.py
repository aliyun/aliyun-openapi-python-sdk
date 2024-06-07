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

class ListFilesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListFiles')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_FileTypes(self): # String
		return self.get_body_params().get('FileTypes')

	def set_FileTypes(self, FileTypes):  # String
		self.add_body_params('FileTypes', FileTypes)
	def get_NeedContent(self): # Boolean
		return self.get_body_params().get('NeedContent')

	def set_NeedContent(self, NeedContent):  # Boolean
		self.add_body_params('NeedContent', NeedContent)
	def get_NeedAbsoluteFolderPath(self): # Boolean
		return self.get_body_params().get('NeedAbsoluteFolderPath')

	def set_NeedAbsoluteFolderPath(self, NeedAbsoluteFolderPath):  # Boolean
		self.add_body_params('NeedAbsoluteFolderPath', NeedAbsoluteFolderPath)
	def get_ProjectIdentifier(self): # String
		return self.get_body_params().get('ProjectIdentifier')

	def set_ProjectIdentifier(self, ProjectIdentifier):  # String
		self.add_body_params('ProjectIdentifier', ProjectIdentifier)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_FileIdIn(self): # String
		return self.get_body_params().get('FileIdIn')

	def set_FileIdIn(self, FileIdIn):  # String
		self.add_body_params('FileIdIn', FileIdIn)
	def get_FileFolderPath(self): # String
		return self.get_body_params().get('FileFolderPath')

	def set_FileFolderPath(self, FileFolderPath):  # String
		self.add_body_params('FileFolderPath', FileFolderPath)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ExactFileName(self): # String
		return self.get_body_params().get('ExactFileName')

	def set_ExactFileName(self, ExactFileName):  # String
		self.add_body_params('ExactFileName', ExactFileName)
	def get_Keyword(self): # String
		return self.get_body_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_body_params('Keyword', Keyword)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_UseType(self): # String
		return self.get_body_params().get('UseType')

	def set_UseType(self, UseType):  # String
		self.add_body_params('UseType', UseType)
	def get_NodeId(self): # Long
		return self.get_body_params().get('NodeId')

	def set_NodeId(self, NodeId):  # Long
		self.add_body_params('NodeId', NodeId)
