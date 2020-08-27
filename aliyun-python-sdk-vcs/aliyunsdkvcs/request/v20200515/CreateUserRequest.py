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
from aliyunsdkvcs.endpoint import endpoint_data

class CreateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'CreateUser')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_Gender(self):
		return self.get_body_params().get('Gender')

	def set_Gender(self,Gender):
		self.add_body_params('Gender', Gender)

	def get_PlateNo(self):
		return self.get_body_params().get('PlateNo')

	def set_PlateNo(self,PlateNo):
		self.add_body_params('PlateNo', PlateNo)

	def get_IdNumber(self):
		return self.get_body_params().get('IdNumber')

	def set_IdNumber(self,IdNumber):
		self.add_body_params('IdNumber', IdNumber)

	def get_FaceImageUrl(self):
		return self.get_body_params().get('FaceImageUrl')

	def set_FaceImageUrl(self,FaceImageUrl):
		self.add_body_params('FaceImageUrl', FaceImageUrl)

	def get_Attachment(self):
		return self.get_body_params().get('Attachment')

	def set_Attachment(self,Attachment):
		self.add_body_params('Attachment', Attachment)

	def get_IsvSubId(self):
		return self.get_body_params().get('IsvSubId')

	def set_IsvSubId(self,IsvSubId):
		self.add_body_params('IsvSubId', IsvSubId)

	def get_Address(self):
		return self.get_body_params().get('Address')

	def set_Address(self,Address):
		self.add_body_params('Address', Address)

	def get_UserGroupId(self):
		return self.get_body_params().get('UserGroupId')

	def set_UserGroupId(self,UserGroupId):
		self.add_body_params('UserGroupId', UserGroupId)

	def get_PhoneNo(self):
		return self.get_body_params().get('PhoneNo')

	def set_PhoneNo(self,PhoneNo):
		self.add_body_params('PhoneNo', PhoneNo)

	def get_BizId(self):
		return self.get_body_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_body_params('BizId', BizId)

	def get_Age(self):
		return self.get_body_params().get('Age')

	def set_Age(self,Age):
		self.add_body_params('Age', Age)

	def get_UserName(self):
		return self.get_body_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_body_params('UserName', UserName)