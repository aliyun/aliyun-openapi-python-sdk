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

class AddProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'AddProfile','vcs')
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

	def get_FaceUrl(self):
		return self.get_body_params().get('FaceUrl')

	def set_FaceUrl(self,FaceUrl):
		self.add_body_params('FaceUrl', FaceUrl)

	def get_LiveAddress(self):
		return self.get_body_params().get('LiveAddress')

	def set_LiveAddress(self,LiveAddress):
		self.add_body_params('LiveAddress', LiveAddress)

	def get_IsvSubId(self):
		return self.get_body_params().get('IsvSubId')

	def set_IsvSubId(self,IsvSubId):
		self.add_body_params('IsvSubId', IsvSubId)

	def get_SceneType(self):
		return self.get_body_params().get('SceneType')

	def set_SceneType(self,SceneType):
		self.add_body_params('SceneType', SceneType)

	def get_PhoneNo(self):
		return self.get_body_params().get('PhoneNo')

	def set_PhoneNo(self,PhoneNo):
		self.add_body_params('PhoneNo', PhoneNo)

	def get_CatalogId(self):
		return self.get_body_params().get('CatalogId')

	def set_CatalogId(self,CatalogId):
		self.add_body_params('CatalogId', CatalogId)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_BizId(self):
		return self.get_body_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_body_params('BizId', BizId)