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

class AIGCFaceVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'AIGCFaceVerify','cloudauth')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_query_param('ProductCode', ProductCode)
	def get_OssObjectName(self): # String
		return self.get_query_params().get('OssObjectName')

	def set_OssObjectName(self, OssObjectName):  # String
		self.add_query_param('OssObjectName', OssObjectName)
	def get_FaceContrastPicture(self): # String
		return self.get_body_params().get('FaceContrastPicture')

	def set_FaceContrastPicture(self, FaceContrastPicture):  # String
		self.add_body_params('FaceContrastPicture', FaceContrastPicture)
	def get_OuterOrderNo(self): # String
		return self.get_query_params().get('OuterOrderNo')

	def set_OuterOrderNo(self, OuterOrderNo):  # String
		self.add_query_param('OuterOrderNo', OuterOrderNo)
	def get_FaceContrastPictureUrl(self): # String
		return self.get_query_params().get('FaceContrastPictureUrl')

	def set_FaceContrastPictureUrl(self, FaceContrastPictureUrl):  # String
		self.add_query_param('FaceContrastPictureUrl', FaceContrastPictureUrl)
	def get_SceneId(self): # Long
		return self.get_query_params().get('SceneId')

	def set_SceneId(self, SceneId):  # Long
		self.add_query_param('SceneId', SceneId)
	def get_OssBucketName(self): # String
		return self.get_query_params().get('OssBucketName')

	def set_OssBucketName(self, OssBucketName):  # String
		self.add_query_param('OssBucketName', OssBucketName)
