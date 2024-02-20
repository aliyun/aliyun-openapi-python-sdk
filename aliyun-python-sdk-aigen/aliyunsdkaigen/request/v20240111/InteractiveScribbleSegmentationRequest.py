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

class InteractiveScribbleSegmentationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aigen', '2024-01-11', 'InteractiveScribbleSegmentation')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PosScribbleImageUrl(self): # String
		return self.get_body_params().get('PosScribbleImageUrl')

	def set_PosScribbleImageUrl(self, PosScribbleImageUrl):  # String
		self.add_body_params('PosScribbleImageUrl', PosScribbleImageUrl)
	def get_IntegratedMaskUrl(self): # String
		return self.get_body_params().get('IntegratedMaskUrl')

	def set_IntegratedMaskUrl(self, IntegratedMaskUrl):  # String
		self.add_body_params('IntegratedMaskUrl', IntegratedMaskUrl)
	def get_MaskImageUrl(self): # String
		return self.get_body_params().get('MaskImageUrl')

	def set_MaskImageUrl(self, MaskImageUrl):  # String
		self.add_body_params('MaskImageUrl', MaskImageUrl)
	def get_ReturnForm(self): # String
		return self.get_body_params().get('ReturnForm')

	def set_ReturnForm(self, ReturnForm):  # String
		self.add_body_params('ReturnForm', ReturnForm)
	def get_NegScribbleImageUrl(self): # String
		return self.get_body_params().get('NegScribbleImageUrl')

	def set_NegScribbleImageUrl(self, NegScribbleImageUrl):  # String
		self.add_body_params('NegScribbleImageUrl', NegScribbleImageUrl)
	def get_ReturnFormat(self): # String
		return self.get_body_params().get('ReturnFormat')

	def set_ReturnFormat(self, ReturnFormat):  # String
		self.add_body_params('ReturnFormat', ReturnFormat)
	def get_EdgeFeathering(self): # String
		return self.get_body_params().get('EdgeFeathering')

	def set_EdgeFeathering(self, EdgeFeathering):  # String
		self.add_body_params('EdgeFeathering', EdgeFeathering)
	def get_ImageUrl(self): # String
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_body_params('ImageUrl', ImageUrl)
	def get_PostprocessOption(self): # String
		return self.get_body_params().get('PostprocessOption')

	def set_PostprocessOption(self, PostprocessOption):  # String
		self.add_body_params('PostprocessOption', PostprocessOption)
