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

class LivenessDetectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2020-11-12', 'LivenessDetect','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MediaCategory(self):
		return self.get_body_params().get('MediaCategory')

	def set_MediaCategory(self,MediaCategory):
		self.add_body_params('MediaCategory', MediaCategory)

	def get_MediaUrl(self):
		return self.get_body_params().get('MediaUrl')

	def set_MediaUrl(self,MediaUrl):
		self.add_body_params('MediaUrl', MediaUrl)

	def get_BizType(self):
		return self.get_body_params().get('BizType')

	def set_BizType(self,BizType):
		self.add_body_params('BizType', BizType)

	def get_BizId(self):
		return self.get_body_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_body_params('BizId', BizId)

	def get_MediaFile(self):
		return self.get_body_params().get('MediaFile')

	def set_MediaFile(self,MediaFile):
		self.add_body_params('MediaFile', MediaFile)