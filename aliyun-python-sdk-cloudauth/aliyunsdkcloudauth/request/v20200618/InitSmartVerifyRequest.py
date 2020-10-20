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

class InitSmartVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2020-06-18', 'InitSmartVerify','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserId(self):
		return self.get_body_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_body_params('UserId', UserId)

	def get_CertifyId(self):
		return self.get_body_params().get('CertifyId')

	def set_CertifyId(self,CertifyId):
		self.add_body_params('CertifyId', CertifyId)

	def get_FacePictureBase64(self):
		return self.get_body_params().get('FacePictureBase64')

	def set_FacePictureBase64(self,FacePictureBase64):
		self.add_body_params('FacePictureBase64', FacePictureBase64)

	def get_Mode(self):
		return self.get_body_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_body_params('Mode', Mode)

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

	def get_MetaInfo(self):
		return self.get_body_params().get('MetaInfo')

	def set_MetaInfo(self,MetaInfo):
		self.add_body_params('MetaInfo', MetaInfo)

	def get_Ocr(self):
		return self.get_body_params().get('Ocr')

	def set_Ocr(self,Ocr):
		self.add_body_params('Ocr', Ocr)

	def get_OssObjectName(self):
		return self.get_body_params().get('OssObjectName')

	def set_OssObjectName(self,OssObjectName):
		self.add_body_params('OssObjectName', OssObjectName)

	def get_FacePictureUrl(self):
		return self.get_body_params().get('FacePictureUrl')

	def set_FacePictureUrl(self,FacePictureUrl):
		self.add_body_params('FacePictureUrl', FacePictureUrl)

	def get_Ip(self):
		return self.get_body_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_body_params('Ip', Ip)

	def get_CertName(self):
		return self.get_body_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_body_params('CertName', CertName)

	def get_Mobile(self):
		return self.get_body_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_body_params('Mobile', Mobile)

	def get_SceneId(self):
		return self.get_body_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_body_params('SceneId', SceneId)

	def get_CallbackToken(self):
		return self.get_body_params().get('CallbackToken')

	def set_CallbackToken(self,CallbackToken):
		self.add_body_params('CallbackToken', CallbackToken)

	def get_OssBucketName(self):
		return self.get_body_params().get('OssBucketName')

	def set_OssBucketName(self,OssBucketName):
		self.add_body_params('OssBucketName', OssBucketName)

	def get_CallbackUrl(self):
		return self.get_body_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_body_params('CallbackUrl', CallbackUrl)