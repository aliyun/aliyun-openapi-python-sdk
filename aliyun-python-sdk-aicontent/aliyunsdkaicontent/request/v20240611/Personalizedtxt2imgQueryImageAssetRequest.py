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

from aliyunsdkcore.request import RoaRequest

class Personalizedtxt2imgQueryImageAssetRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'AiContent', '20240611', 'Personalizedtxt2imgQueryImageAsset')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v1/personalizedtxt2img/queryImageAsset')
		self.set_method('GET')

	def get_imageId(self): # String
		return self.get_query_params().get('imageId')

	def set_imageId(self, imageId):  # String
		self.add_query_param('imageId', imageId)
	def get_modelId(self): # String
		return self.get_query_params().get('modelId')

	def set_modelId(self, modelId):  # String
		self.add_query_param('modelId', modelId)
	def get_encodeFormat(self): # String
		return self.get_query_params().get('encodeFormat')

	def set_encodeFormat(self, encodeFormat):  # String
		self.add_query_param('encodeFormat', encodeFormat)
	def get_promptId(self): # String
		return self.get_query_params().get('promptId')

	def set_promptId(self, promptId):  # String
		self.add_query_param('promptId', promptId)
