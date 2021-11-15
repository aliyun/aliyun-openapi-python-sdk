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
from aliyunsdkalimt.endpoint import endpoint_data

class TranslateImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2018-10-12', 'TranslateImage')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Ext(self): # String
		return self.get_body_params().get('Ext')

	def set_Ext(self, Ext):  # String
		self.add_body_params('Ext', Ext)
	def get_SourceLanguage(self): # String
		return self.get_body_params().get('SourceLanguage')

	def set_SourceLanguage(self, SourceLanguage):  # String
		self.add_body_params('SourceLanguage', SourceLanguage)
	def get_Field(self): # String
		return self.get_body_params().get('Field')

	def set_Field(self, Field):  # String
		self.add_body_params('Field', Field)
	def get_ImageUrl(self): # String
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_body_params('ImageUrl', ImageUrl)
	def get_TargetLanguage(self): # String
		return self.get_body_params().get('TargetLanguage')

	def set_TargetLanguage(self, TargetLanguage):  # String
		self.add_body_params('TargetLanguage', TargetLanguage)
	def get_ImageBase64(self): # String
		return self.get_body_params().get('ImageBase64')

	def set_ImageBase64(self, ImageBase64):  # String
		self.add_body_params('ImageBase64', ImageBase64)
