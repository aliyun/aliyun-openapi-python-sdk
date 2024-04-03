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
from aliyunsdkcloudauth.endpoint import endpoint_data

class CompareFaceVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'CompareFaceVerify','cloudauth')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_TargetCertifyId(self): # String
		return self.get_body_params().get('TargetCertifyId')

	def set_TargetCertifyId(self, TargetCertifyId):  # String
		self.add_body_params('TargetCertifyId', TargetCertifyId)
	def get_TargetFaceContrastPicture(self): # String
		return self.get_body_params().get('TargetFaceContrastPicture')

	def set_TargetFaceContrastPicture(self, TargetFaceContrastPicture):  # String
		self.add_body_params('TargetFaceContrastPicture', TargetFaceContrastPicture)
	def get_TargetOssBucketName(self): # String
		return self.get_body_params().get('TargetOssBucketName')

	def set_TargetOssBucketName(self, TargetOssBucketName):  # String
		self.add_body_params('TargetOssBucketName', TargetOssBucketName)
	def get_OuterOrderNo(self): # String
		return self.get_body_params().get('OuterOrderNo')

	def set_OuterOrderNo(self, OuterOrderNo):  # String
		self.add_body_params('OuterOrderNo', OuterOrderNo)
	def get_SourceFaceContrastPicture(self): # String
		return self.get_body_params().get('SourceFaceContrastPicture')

	def set_SourceFaceContrastPicture(self, SourceFaceContrastPicture):  # String
		self.add_body_params('SourceFaceContrastPicture', SourceFaceContrastPicture)
	def get_SourceCertifyId(self): # String
		return self.get_body_params().get('SourceCertifyId')

	def set_SourceCertifyId(self, SourceCertifyId):  # String
		self.add_body_params('SourceCertifyId', SourceCertifyId)
	def get_TargetFaceContrastPictureUrl(self): # String
		return self.get_body_params().get('TargetFaceContrastPictureUrl')

	def set_TargetFaceContrastPictureUrl(self, TargetFaceContrastPictureUrl):  # String
		self.add_body_params('TargetFaceContrastPictureUrl', TargetFaceContrastPictureUrl)
	def get_SourceOssObjectName(self): # String
		return self.get_body_params().get('SourceOssObjectName')

	def set_SourceOssObjectName(self, SourceOssObjectName):  # String
		self.add_body_params('SourceOssObjectName', SourceOssObjectName)
	def get_SourceOssBucketName(self): # String
		return self.get_body_params().get('SourceOssBucketName')

	def set_SourceOssBucketName(self, SourceOssBucketName):  # String
		self.add_body_params('SourceOssBucketName', SourceOssBucketName)
	def get_TargetOssObjectName(self): # String
		return self.get_body_params().get('TargetOssObjectName')

	def set_TargetOssObjectName(self, TargetOssObjectName):  # String
		self.add_body_params('TargetOssObjectName', TargetOssObjectName)
	def get_SceneId(self): # Long
		return self.get_body_params().get('SceneId')

	def set_SceneId(self, SceneId):  # Long
		self.add_body_params('SceneId', SceneId)
	def get_SourceFaceContrastPictureUrl(self): # String
		return self.get_body_params().get('SourceFaceContrastPictureUrl')

	def set_SourceFaceContrastPictureUrl(self, SourceFaceContrastPictureUrl):  # String
		self.add_body_params('SourceFaceContrastPictureUrl', SourceFaceContrastPictureUrl)
	def get_Crop(self): # String
		return self.get_body_params().get('Crop')

	def set_Crop(self, Crop):  # String
		self.add_body_params('Crop', Crop)
