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

class VerifyMaterialRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'VerifyMaterial','cloudauth')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FaceImageUrl(self): # String
		return self.get_query_params().get('FaceImageUrl')

	def set_FaceImageUrl(self, FaceImageUrl):  # String
		self.add_query_param('FaceImageUrl', FaceImageUrl)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_IdCardBackImageUrl(self): # String
		return self.get_query_params().get('IdCardBackImageUrl')

	def set_IdCardBackImageUrl(self, IdCardBackImageUrl):  # String
		self.add_query_param('IdCardBackImageUrl', IdCardBackImageUrl)
	def get_IdCardNumber(self): # String
		return self.get_query_params().get('IdCardNumber')

	def set_IdCardNumber(self, IdCardNumber):  # String
		self.add_query_param('IdCardNumber', IdCardNumber)
	def get_IdCardFrontImageUrl(self): # String
		return self.get_query_params().get('IdCardFrontImageUrl')

	def set_IdCardFrontImageUrl(self, IdCardFrontImageUrl):  # String
		self.add_query_param('IdCardFrontImageUrl', IdCardFrontImageUrl)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
