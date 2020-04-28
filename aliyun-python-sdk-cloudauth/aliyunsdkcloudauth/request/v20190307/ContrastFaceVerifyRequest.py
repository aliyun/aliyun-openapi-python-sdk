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

class ContrastFaceVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'ContrastFaceVerify','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_OssObjectName(self):
		return self.get_body_params().get('OssObjectName')

	def set_OssObjectName(self,OssObjectName):
		self.add_body_params('OssObjectName', OssObjectName)

	def get_FaceContrastPicture(self):
		return self.get_body_params().get('FaceContrastPicture')

	def set_FaceContrastPicture(self,FaceContrastPicture):
		self.add_body_params('FaceContrastPicture', FaceContrastPicture)

	def get_CertName(self):
		return self.get_body_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_body_params('CertName', CertName)

	def get_Ip(self):
		return self.get_body_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_body_params('Ip', Ip)

	def get_Mobile(self):
		return self.get_body_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_body_params('Mobile', Mobile)

	def get_DeviceToken(self):
		return self.get_body_params().get('DeviceToken')

	def set_DeviceToken(self,DeviceToken):
		self.add_body_params('DeviceToken', DeviceToken)

	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)

	def get_CertifyId(self):
		return self.get_body_params().get('CertifyId')

	def set_CertifyId(self,CertifyId):
		self.add_body_params('CertifyId', CertifyId)

	def get_CertNo(self):
		return self.get_body_params().get('CertNo')

	def set_CertNo(self,CertNo):
		self.add_body_params('CertNo', CertNo)

	def get_OuterOrderNo(self):
		return self.get_body_params().get('OuterOrderNo')

	def set_OuterOrderNo(self,OuterOrderNo):
		self.add_body_params('OuterOrderNo', OuterOrderNo)

	def get_CertType(self):
		return self.get_body_params().get('CertType')

	def set_CertType(self,CertType):
		self.add_body_params('CertType', CertType)

	def get_FaceContrastPictureUrl(self):
		return self.get_body_params().get('FaceContrastPictureUrl')

	def set_FaceContrastPictureUrl(self,FaceContrastPictureUrl):
		self.add_body_params('FaceContrastPictureUrl', FaceContrastPictureUrl)

	def get_SceneId(self):
		return self.get_body_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_body_params('SceneId', SceneId)

	def get_OssBucketName(self):
		return self.get_body_params().get('OssBucketName')

	def set_OssBucketName(self,OssBucketName):
		self.add_body_params('OssBucketName', OssBucketName)