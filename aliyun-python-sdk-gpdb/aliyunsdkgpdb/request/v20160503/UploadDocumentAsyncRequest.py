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
from aliyunsdkgpdb.endpoint import endpoint_data
import json

class UploadDocumentAsyncRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'UploadDocumentAsync','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Metadata(self): # Map
		return self.get_body_params().get('Metadata')

	def set_Metadata(self, Metadata):  # Map
		self.add_body_params("Metadata", json.dumps(Metadata))
	def get_VlEnhance(self): # Boolean
		return self.get_body_params().get('VlEnhance')

	def set_VlEnhance(self, VlEnhance):  # Boolean
		self.add_body_params('VlEnhance', VlEnhance)
	def get_SplitterModel(self): # String
		return self.get_body_params().get('SplitterModel')

	def set_SplitterModel(self, SplitterModel):  # String
		self.add_body_params('SplitterModel', SplitterModel)
	def get_ChunkSize(self): # Integer
		return self.get_body_params().get('ChunkSize')

	def set_ChunkSize(self, ChunkSize):  # Integer
		self.add_body_params('ChunkSize', ChunkSize)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_ChunkOverlap(self): # Integer
		return self.get_body_params().get('ChunkOverlap')

	def set_ChunkOverlap(self, ChunkOverlap):  # Integer
		self.add_body_params('ChunkOverlap', ChunkOverlap)
	def get_DocumentLoaderName(self): # String
		return self.get_body_params().get('DocumentLoaderName')

	def set_DocumentLoaderName(self, DocumentLoaderName):  # String
		self.add_body_params('DocumentLoaderName', DocumentLoaderName)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ZhTitleEnhance(self): # Boolean
		return self.get_body_params().get('ZhTitleEnhance')

	def set_ZhTitleEnhance(self, ZhTitleEnhance):  # Boolean
		self.add_body_params('ZhTitleEnhance', ZhTitleEnhance)
	def get_TextSplitterName(self): # String
		return self.get_body_params().get('TextSplitterName')

	def set_TextSplitterName(self, TextSplitterName):  # String
		self.add_body_params('TextSplitterName', TextSplitterName)
	def get_Collection(self): # String
		return self.get_body_params().get('Collection')

	def set_Collection(self, Collection):  # String
		self.add_body_params('Collection', Collection)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NamespacePassword(self): # String
		return self.get_body_params().get('NamespacePassword')

	def set_NamespacePassword(self, NamespacePassword):  # String
		self.add_body_params('NamespacePassword', NamespacePassword)
	def get_FileName(self): # String
		return self.get_body_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_body_params('FileName', FileName)
	def get_Namespace(self): # String
		return self.get_body_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_body_params('Namespace', Namespace)
	def get_FileUrl(self): # String
		return self.get_body_params().get('FileUrl')

	def set_FileUrl(self, FileUrl):  # String
		self.add_body_params('FileUrl', FileUrl)
	def get_Separators(self): # Array
		return self.get_body_params().get('Separators')

	def set_Separators(self, Separators):  # Array
		self.add_body_params("Separators", json.dumps(Separators))
