# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateSignatureRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cas', '2018-08-13', 'CreateSignature','cas_esign_fdd')

	def get_Quantity(self):
		return self.get_query_params().get('Quantity')

	def set_Quantity(self,Quantity):
		self.add_query_param('Quantity',Quantity)

	def get_HandSignImg(self):
		return self.get_query_params().get('HandSignImg')

	def set_HandSignImg(self,HandSignImg):
		self.add_query_param('HandSignImg',HandSignImg)

	def get_DocId(self):
		return self.get_query_params().get('DocId')

	def set_DocId(self,DocId):
		self.add_query_param('DocId',DocId)

	def get_CustomApi(self):
		return self.get_query_params().get('CustomApi')

	def set_CustomApi(self,CustomApi):
		self.add_query_param('CustomApi',CustomApi)

	def get_PositionPage(self):
		return self.get_query_params().get('PositionPage')

	def set_PositionPage(self,PositionPage):
		self.add_query_param('PositionPage',PositionPage)

	def get_DocTitle(self):
		return self.get_query_params().get('DocTitle')

	def set_DocTitle(self,DocTitle):
		self.add_query_param('DocTitle',DocTitle)

	def get_PositionX(self):
		return self.get_query_params().get('PositionX')

	def set_PositionX(self,PositionX):
		self.add_query_param('PositionX',PositionX)

	def get_PositionY(self):
		return self.get_query_params().get('PositionY')

	def set_PositionY(self,PositionY):
		self.add_query_param('PositionY',PositionY)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PeopleId(self):
		return self.get_query_params().get('PeopleId')

	def set_PeopleId(self,PeopleId):
		self.add_query_param('PeopleId',PeopleId)

	def get_PositionType(self):
		return self.get_query_params().get('PositionType')

	def set_PositionType(self,PositionType):
		self.add_query_param('PositionType',PositionType)

	def get_SignKeyword(self):
		return self.get_query_params().get('SignKeyword')

	def set_SignKeyword(self,SignKeyword):
		self.add_query_param('SignKeyword',SignKeyword)

	def get_NotifyUrl(self):
		return self.get_query_params().get('NotifyUrl')

	def set_NotifyUrl(self,NotifyUrl):
		self.add_query_param('NotifyUrl',NotifyUrl)

	def get_Validity(self):
		return self.get_query_params().get('Validity')

	def set_Validity(self,Validity):
		self.add_query_param('Validity',Validity)

	def get_ReturnUrl(self):
		return self.get_query_params().get('ReturnUrl')

	def set_ReturnUrl(self,ReturnUrl):
		self.add_query_param('ReturnUrl',ReturnUrl)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_KeywordStrategy(self):
		return self.get_query_params().get('KeywordStrategy')

	def set_KeywordStrategy(self,KeywordStrategy):
		self.add_query_param('KeywordStrategy',KeywordStrategy)