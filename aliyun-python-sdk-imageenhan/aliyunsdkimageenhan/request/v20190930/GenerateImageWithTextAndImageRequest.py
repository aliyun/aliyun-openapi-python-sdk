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
from aliyunsdkimageenhan.endpoint import endpoint_data

class GenerateImageWithTextAndImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageenhan', '2019-09-30', 'GenerateImageWithTextAndImage','imageenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Resolution(self): # String
		return self.get_body_params().get('Resolution')

	def set_Resolution(self, Resolution):  # String
		self.add_body_params('Resolution', Resolution)
	def get_Number(self): # Integer
		return self.get_body_params().get('Number')

	def set_Number(self, Number):  # Integer
		self.add_body_params('Number', Number)
	def get_Similarity(self): # Float
		return self.get_body_params().get('Similarity')

	def set_Similarity(self, Similarity):  # Float
		self.add_body_params('Similarity', Similarity)
	def get_AspectRatioMode(self): # String
		return self.get_body_params().get('AspectRatioMode')

	def set_AspectRatioMode(self, AspectRatioMode):  # String
		self.add_body_params('AspectRatioMode', AspectRatioMode)
	def get_Text(self): # String
		return self.get_body_params().get('Text')

	def set_Text(self, Text):  # String
		self.add_body_params('Text', Text)
	def get_RefImageUrl(self): # String
		return self.get_body_params().get('RefImageUrl')

	def set_RefImageUrl(self, RefImageUrl):  # String
		self.add_body_params('RefImageUrl', RefImageUrl)
