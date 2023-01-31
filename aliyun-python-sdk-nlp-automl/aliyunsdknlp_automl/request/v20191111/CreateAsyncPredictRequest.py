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
from aliyunsdknlp_automl.endpoint import endpoint_data

class CreateAsyncPredictRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nlp-automl', '2019-11-11', 'CreateAsyncPredict')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TopK(self): # Integer
		return self.get_body_params().get('TopK')

	def set_TopK(self, TopK):  # Integer
		self.add_body_params('TopK', TopK)
	def get_FileType(self): # String
		return self.get_body_params().get('FileType')

	def set_FileType(self, FileType):  # String
		self.add_body_params('FileType', FileType)
	def get_DetailTag(self): # String
		return self.get_body_params().get('DetailTag')

	def set_DetailTag(self, DetailTag):  # String
		self.add_body_params('DetailTag', DetailTag)
	def get_FetchContent(self): # String
		return self.get_body_params().get('FetchContent')

	def set_FetchContent(self, FetchContent):  # String
		self.add_body_params('FetchContent', FetchContent)
	def get_Content(self): # String
		return self.get_body_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_body_params('Content', Content)
	def get_FileContent(self): # String
		return self.get_body_params().get('FileContent')

	def set_FileContent(self, FileContent):  # String
		self.add_body_params('FileContent', FileContent)
	def get_ServiceName(self): # String
		return self.get_body_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_body_params('ServiceName', ServiceName)
	def get_ModelId(self): # Integer
		return self.get_body_params().get('ModelId')

	def set_ModelId(self, ModelId):  # Integer
		self.add_body_params('ModelId', ModelId)
	def get_ServiceVersion(self): # String
		return self.get_body_params().get('ServiceVersion')

	def set_ServiceVersion(self, ServiceVersion):  # String
		self.add_body_params('ServiceVersion', ServiceVersion)
	def get_FileUrl(self): # String
		return self.get_body_params().get('FileUrl')

	def set_FileUrl(self, FileUrl):  # String
		self.add_body_params('FileUrl', FileUrl)
	def get_ModelVersion(self): # String
		return self.get_body_params().get('ModelVersion')

	def set_ModelVersion(self, ModelVersion):  # String
		self.add_body_params('ModelVersion', ModelVersion)
