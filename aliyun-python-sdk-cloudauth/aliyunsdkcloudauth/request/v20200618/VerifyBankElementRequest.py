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

class VerifyBankElementRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2020-06-18', 'VerifyBankElement','cloudauth')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IdName(self):
		return self.get_body_params().get('IdName')

	def set_IdName(self,IdName):
		self.add_body_params('IdName', IdName)

	def get_Mobile(self):
		return self.get_body_params().get('Mobile')

	def set_Mobile(self,Mobile):
		self.add_body_params('Mobile', Mobile)

	def get_BankCardUrl(self):
		return self.get_body_params().get('BankCardUrl')

	def set_BankCardUrl(self,BankCardUrl):
		self.add_body_params('BankCardUrl', BankCardUrl)

	def get_IdNo(self):
		return self.get_body_params().get('IdNo')

	def set_IdNo(self,IdNo):
		self.add_body_params('IdNo', IdNo)

	def get_BankCardNo(self):
		return self.get_body_params().get('BankCardNo')

	def set_BankCardNo(self,BankCardNo):
		self.add_body_params('BankCardNo', BankCardNo)

	def get_Mode(self):
		return self.get_body_params().get('Mode')

	def set_Mode(self,Mode):
		self.add_body_params('Mode', Mode)

	def get_OuterOrderNo(self):
		return self.get_body_params().get('OuterOrderNo')

	def set_OuterOrderNo(self,OuterOrderNo):
		self.add_body_params('OuterOrderNo', OuterOrderNo)

	def get_BankCardFile(self):
		return self.get_body_params().get('BankCardFile')

	def set_BankCardFile(self,BankCardFile):
		self.add_body_params('BankCardFile', BankCardFile)

	def get_SceneId(self):
		return self.get_body_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_body_params('SceneId', SceneId)