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

class ElementSmartVerifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2020-06-18', 'ElementSmartVerify','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CertFile(self):
		return self.get_body_params().get('CertFile')

	def set_CertFile(self,CertFile):
		self.add_body_params('CertFile', CertFile)

	def get_CertName(self):
		return self.get_body_params().get('CertName')

	def set_CertName(self,CertName):
		self.add_body_params('CertName', CertName)

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

	def get_CertUrl(self):
		return self.get_body_params().get('CertUrl')

	def set_CertUrl(self,CertUrl):
		self.add_body_params('CertUrl', CertUrl)

	def get_CertType(self):
		return self.get_body_params().get('CertType')

	def set_CertType(self,CertType):
		self.add_body_params('CertType', CertType)

	def get_SceneId(self):
		return self.get_body_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_body_params('SceneId', SceneId)