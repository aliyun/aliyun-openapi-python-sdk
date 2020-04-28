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


	def get_TargetFaceContrastPictureUrl(self):
		return self.get_body_params().get('TargetFaceContrastPictureUrl')

	def set_TargetFaceContrastPictureUrl(self,TargetFaceContrastPictureUrl):
		self.add_body_params('TargetFaceContrastPictureUrl', TargetFaceContrastPictureUrl)

	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_TargetCertifyId(self):
		return self.get_body_params().get('TargetCertifyId')

	def set_TargetCertifyId(self,TargetCertifyId):
		self.add_body_params('TargetCertifyId', TargetCertifyId)

	def get_SourceOssObjectName(self):
		return self.get_body_params().get('SourceOssObjectName')

	def set_SourceOssObjectName(self,SourceOssObjectName):
		self.add_body_params('SourceOssObjectName', SourceOssObjectName)

	def get_TargetFaceContrastPicture(self):
		return self.get_body_params().get('TargetFaceContrastPicture')

	def set_TargetFaceContrastPicture(self,TargetFaceContrastPicture):
		self.add_body_params('TargetFaceContrastPicture', TargetFaceContrastPicture)

	def get_TargetOssBucketName(self):
		return self.get_body_params().get('TargetOssBucketName')

	def set_TargetOssBucketName(self,TargetOssBucketName):
		self.add_body_params('TargetOssBucketName', TargetOssBucketName)

	def get_SourceOssBucketName(self):
		return self.get_body_params().get('SourceOssBucketName')

	def set_SourceOssBucketName(self,SourceOssBucketName):
		self.add_body_params('SourceOssBucketName', SourceOssBucketName)

	def get_OuterOrderNo(self):
		return self.get_body_params().get('OuterOrderNo')

	def set_OuterOrderNo(self,OuterOrderNo):
		self.add_body_params('OuterOrderNo', OuterOrderNo)

	def get_TargetOssObjectName(self):
		return self.get_body_params().get('TargetOssObjectName')

	def set_TargetOssObjectName(self,TargetOssObjectName):
		self.add_body_params('TargetOssObjectName', TargetOssObjectName)

	def get_SourceFaceContrastPicture(self):
		return self.get_body_params().get('SourceFaceContrastPicture')

	def set_SourceFaceContrastPicture(self,SourceFaceContrastPicture):
		self.add_body_params('SourceFaceContrastPicture', SourceFaceContrastPicture)

	def get_SceneId(self):
		return self.get_body_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_body_params('SceneId', SceneId)

	def get_SourceFaceContrastPictureUrl(self):
		return self.get_body_params().get('SourceFaceContrastPictureUrl')

	def set_SourceFaceContrastPictureUrl(self,SourceFaceContrastPictureUrl):
		self.add_body_params('SourceFaceContrastPictureUrl', SourceFaceContrastPictureUrl)

	def get_SourceCertifyId(self):
		return self.get_body_params().get('SourceCertifyId')

	def set_SourceCertifyId(self,SourceCertifyId):
		self.add_body_params('SourceCertifyId', SourceCertifyId)