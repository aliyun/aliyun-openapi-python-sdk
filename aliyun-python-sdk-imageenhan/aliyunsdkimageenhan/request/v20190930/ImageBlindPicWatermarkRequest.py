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

class ImageBlindPicWatermarkRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageenhan', '2019-09-30', 'ImageBlindPicWatermark','imageenhan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_WatermarkImageURL(self):
		return self.get_body_params().get('WatermarkImageURL')

	def set_WatermarkImageURL(self,WatermarkImageURL):
		self.add_body_params('WatermarkImageURL', WatermarkImageURL)

	def get_QualityFactor(self):
		return self.get_body_params().get('QualityFactor')

	def set_QualityFactor(self,QualityFactor):
		self.add_body_params('QualityFactor', QualityFactor)

	def get_FunctionType(self):
		return self.get_body_params().get('FunctionType')

	def set_FunctionType(self,FunctionType):
		self.add_body_params('FunctionType', FunctionType)

	def get_LogoURL(self):
		return self.get_body_params().get('LogoURL')

	def set_LogoURL(self,LogoURL):
		self.add_body_params('LogoURL', LogoURL)

	def get_OutputFileType(self):
		return self.get_body_params().get('OutputFileType')

	def set_OutputFileType(self,OutputFileType):
		self.add_body_params('OutputFileType', OutputFileType)

	def get_OriginImageURL(self):
		return self.get_body_params().get('OriginImageURL')

	def set_OriginImageURL(self,OriginImageURL):
		self.add_body_params('OriginImageURL', OriginImageURL)