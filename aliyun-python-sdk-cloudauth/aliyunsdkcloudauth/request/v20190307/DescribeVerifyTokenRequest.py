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

class DescribeVerifyTokenRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'DescribeVerifyToken','cloudauth')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FaceRetainedImageUrl(self):
		return self.get_query_params().get('FaceRetainedImageUrl')

	def set_FaceRetainedImageUrl(self,FaceRetainedImageUrl):
		self.add_query_param('FaceRetainedImageUrl',FaceRetainedImageUrl)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_CallbackSeed(self):
		return self.get_query_params().get('CallbackSeed')

	def set_CallbackSeed(self,CallbackSeed):
		self.add_query_param('CallbackSeed',CallbackSeed)

	def get_IdCardBackImageUrl(self):
		return self.get_query_params().get('IdCardBackImageUrl')

	def set_IdCardBackImageUrl(self,IdCardBackImageUrl):
		self.add_query_param('IdCardBackImageUrl',IdCardBackImageUrl)

	def get_IdCardNumber(self):
		return self.get_query_params().get('IdCardNumber')

	def set_IdCardNumber(self,IdCardNumber):
		self.add_query_param('IdCardNumber',IdCardNumber)

	def get_IdCardFrontImageUrl(self):
		return self.get_query_params().get('IdCardFrontImageUrl')

	def set_IdCardFrontImageUrl(self,IdCardFrontImageUrl):
		self.add_query_param('IdCardFrontImageUrl',IdCardFrontImageUrl)

	def get_BizType(self):
		return self.get_query_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_query_param('BizType',BizType)

	def get_PassedRedirectUrl(self):
		return self.get_query_params().get('PassedRedirectUrl')

	def set_PassedRedirectUrl(self,PassedRedirectUrl):
		self.add_query_param('PassedRedirectUrl',PassedRedirectUrl)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)

	def get_FailedRedirectUrl(self):
		return self.get_query_params().get('FailedRedirectUrl')

	def set_FailedRedirectUrl(self,FailedRedirectUrl):
		self.add_query_param('FailedRedirectUrl',FailedRedirectUrl)