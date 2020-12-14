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

class SearchObjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'SearchObject')
		self.set_method('POST')

	def get_ShotTimeEnd(self):
		return self.get_body_params().get('ShotTimeEnd')

	def set_ShotTimeEnd(self,ShotTimeEnd):
		self.add_body_params('ShotTimeEnd', ShotTimeEnd)

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_Feature(self):
		return self.get_body_params().get('Feature')

	def set_Feature(self,Feature):
		self.add_body_params('Feature', Feature)

	def get_Vendor(self):
		return self.get_body_params().get('Vendor')

	def set_Vendor(self,Vendor):
		self.add_body_params('Vendor', Vendor)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_ImageContent(self):
		return self.get_body_params().get('ImageContent')

	def set_ImageContent(self,ImageContent):
		self.add_body_params('ImageContent', ImageContent)

	def get_ObjectType(self):
		return self.get_body_params().get('ObjectType')

	def set_ObjectType(self,ObjectType):
		self.add_body_params('ObjectType', ObjectType)

	def get_DeviceList(self):
		return self.get_body_params().get('DeviceList')

	def set_DeviceList(self,DeviceList):
		self.add_body_params('DeviceList', DeviceList)

	def get_ImageUrl(self):
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_body_params('ImageUrl', ImageUrl)

	def get_Attributes(self):
		return self.get_body_params().get('Attributes')

	def set_Attributes(self,Attributes):
		self.add_body_params('Attributes', Attributes)

	def get_ShotTimeStart(self):
		return self.get_body_params().get('ShotTimeStart')

	def set_ShotTimeStart(self,ShotTimeStart):
		self.add_body_params('ShotTimeStart', ShotTimeStart)