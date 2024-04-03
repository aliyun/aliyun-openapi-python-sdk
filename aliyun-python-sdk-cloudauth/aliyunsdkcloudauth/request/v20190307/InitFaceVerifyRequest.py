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

class InitFaceVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'InitFaceVerify','cloudauth')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Birthday(self): # String
		return self.get_query_params().get('Birthday')

	def set_Birthday(self, Birthday):  # String
		self.add_query_param('Birthday', Birthday)
	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_FaceContrastPicture(self): # String
		return self.get_body_params().get('FaceContrastPicture')

	def set_FaceContrastPicture(self, FaceContrastPicture):  # String
		self.add_body_params('FaceContrastPicture', FaceContrastPicture)
	def get_ReadImg(self): # String
		return self.get_query_params().get('ReadImg')

	def set_ReadImg(self, ReadImg):  # String
		self.add_query_param('ReadImg', ReadImg)
	def get_RarelyCharacters(self): # String
		return self.get_query_params().get('RarelyCharacters')

	def set_RarelyCharacters(self, RarelyCharacters):  # String
		self.add_query_param('RarelyCharacters', RarelyCharacters)
	def get_VoluntaryCustomizedContent(self): # String
		return self.get_query_params().get('VoluntaryCustomizedContent')

	def set_VoluntaryCustomizedContent(self, VoluntaryCustomizedContent):  # String
		self.add_query_param('VoluntaryCustomizedContent', VoluntaryCustomizedContent)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_CertifyId(self): # String
		return self.get_query_params().get('CertifyId')

	def set_CertifyId(self, CertifyId):  # String
		self.add_query_param('CertifyId', CertifyId)
	def get_EncryptType(self): # String
		return self.get_query_params().get('EncryptType')

	def set_EncryptType(self, EncryptType):  # String
		self.add_query_param('EncryptType', EncryptType)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_CertNo(self): # String
		return self.get_query_params().get('CertNo')

	def set_CertNo(self, CertNo):  # String
		self.add_query_param('CertNo', CertNo)
	def get_OuterOrderNo(self): # String
		return self.get_query_params().get('OuterOrderNo')

	def set_OuterOrderNo(self, OuterOrderNo):  # String
		self.add_query_param('OuterOrderNo', OuterOrderNo)
	def get_CertType(self): # String
		return self.get_query_params().get('CertType')

	def set_CertType(self, CertType):  # String
		self.add_query_param('CertType', CertType)
	def get_FaceContrastPictureUrl(self): # String
		return self.get_query_params().get('FaceContrastPictureUrl')

	def set_FaceContrastPictureUrl(self, FaceContrastPictureUrl):  # String
		self.add_query_param('FaceContrastPictureUrl', FaceContrastPictureUrl)
	def get_Model(self): # String
		return self.get_body_params().get('Model')

	def set_Model(self, Model):  # String
		self.add_body_params('Model', Model)
	def get_SuitableType(self): # String
		return self.get_query_params().get('SuitableType')

	def set_SuitableType(self, SuitableType):  # String
		self.add_query_param('SuitableType', SuitableType)
	def get_CertifyUrlStyle(self): # String
		return self.get_query_params().get('CertifyUrlStyle')

	def set_CertifyUrlStyle(self, CertifyUrlStyle):  # String
		self.add_query_param('CertifyUrlStyle', CertifyUrlStyle)
	def get_MetaInfo(self): # String
		return self.get_query_params().get('MetaInfo')

	def set_MetaInfo(self, MetaInfo):  # String
		self.add_query_param('MetaInfo', MetaInfo)
	def get_OssObjectName(self): # String
		return self.get_query_params().get('OssObjectName')

	def set_OssObjectName(self, OssObjectName):  # String
		self.add_query_param('OssObjectName', OssObjectName)
	def get_ValidityDate(self): # String
		return self.get_query_params().get('ValidityDate')

	def set_ValidityDate(self, ValidityDate):  # String
		self.add_query_param('ValidityDate', ValidityDate)
	def get_CertName(self): # String
		return self.get_query_params().get('CertName')

	def set_CertName(self, CertName):  # String
		self.add_query_param('CertName', CertName)
	def get_Ip(self): # String
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # String
		self.add_query_param('Ip', Ip)
	def get_Mobile(self): # String
		return self.get_query_params().get('Mobile')

	def set_Mobile(self, Mobile):  # String
		self.add_query_param('Mobile', Mobile)
	def get_FaceGuardOutput(self): # String
		return self.get_query_params().get('FaceGuardOutput')

	def set_FaceGuardOutput(self, FaceGuardOutput):  # String
		self.add_query_param('FaceGuardOutput', FaceGuardOutput)
	def get_AuthId(self): # String
		return self.get_body_params().get('AuthId')

	def set_AuthId(self, AuthId):  # String
		self.add_body_params('AuthId', AuthId)
	def get_ProcedurePriority(self): # String
		return self.get_query_params().get('ProcedurePriority')

	def set_ProcedurePriority(self, ProcedurePriority):  # String
		self.add_query_param('ProcedurePriority', ProcedurePriority)
	def get_SceneId(self): # Long
		return self.get_query_params().get('SceneId')

	def set_SceneId(self, SceneId):  # Long
		self.add_query_param('SceneId', SceneId)
	def get_OssBucketName(self): # String
		return self.get_query_params().get('OssBucketName')

	def set_OssBucketName(self, OssBucketName):  # String
		self.add_query_param('OssBucketName', OssBucketName)
	def get_CallbackToken(self): # String
		return self.get_query_params().get('CallbackToken')

	def set_CallbackToken(self, CallbackToken):  # String
		self.add_query_param('CallbackToken', CallbackToken)
	def get_ReturnUrl(self): # String
		return self.get_query_params().get('ReturnUrl')

	def set_ReturnUrl(self, ReturnUrl):  # String
		self.add_query_param('ReturnUrl', ReturnUrl)
	def get_CallbackUrl(self): # String
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self, CallbackUrl):  # String
		self.add_query_param('CallbackUrl', CallbackUrl)
	def get_Crop(self): # String
		return self.get_body_params().get('Crop')

	def set_Crop(self, Crop):  # String
		self.add_body_params('Crop', Crop)
	def get_CertifyUrlType(self): # String
		return self.get_query_params().get('CertifyUrlType')

	def set_CertifyUrlType(self, CertifyUrlType):  # String
		self.add_query_param('CertifyUrlType', CertifyUrlType)
