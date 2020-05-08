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
class CreateTrademarkOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Trademark', '2018-07-24', 'CreateTrademarkOrder','trademark')

	def get_TmName(self):
		return self.get_query_params().get('TmName')

	def set_TmName(self,TmName):
		self.add_query_param('TmName',TmName)

	def get_RealUserName(self):
		return self.get_query_params().get('RealUserName')

	def set_RealUserName(self,RealUserName):
		self.add_query_param('RealUserName',RealUserName)

	def get_OrderData(self):
		return self.get_query_params().get('OrderData')

	def set_OrderData(self,OrderData):
		self.add_query_param('OrderData',OrderData)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_PartnerCode(self):
		return self.get_query_params().get('PartnerCode')

	def set_PartnerCode(self,PartnerCode):
		self.add_query_param('PartnerCode',PartnerCode)

	def get_PhoneNum(self):
		return self.get_query_params().get('PhoneNum')

	def set_PhoneNum(self,PhoneNum):
		self.add_query_param('PhoneNum',PhoneNum)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_MaterialId(self):
		return self.get_query_params().get('MaterialId')

	def set_MaterialId(self,MaterialId):
		self.add_query_param('MaterialId',MaterialId)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_TmComment(self):
		return self.get_query_params().get('TmComment')

	def set_TmComment(self,TmComment):
		self.add_query_param('TmComment',TmComment)

	def get_RegisterName(self):
		return self.get_query_params().get('RegisterName')

	def set_RegisterName(self,RegisterName):
		self.add_query_param('RegisterName',RegisterName)

	def get_TmNameType(self):
		return self.get_query_params().get('TmNameType')

	def set_TmNameType(self,TmNameType):
		self.add_query_param('TmNameType',TmNameType)

	def get_TmIcon(self):
		return self.get_query_params().get('TmIcon')

	def set_TmIcon(self,TmIcon):
		self.add_query_param('TmIcon',TmIcon)

	def get_Uid(self):
		return self.get_query_params().get('Uid')

	def set_Uid(self,Uid):
		self.add_query_param('Uid',Uid)

	def get_IsBlackIcon(self):
		return self.get_query_params().get('IsBlackIcon')

	def set_IsBlackIcon(self,IsBlackIcon):
		self.add_query_param('IsBlackIcon',IsBlackIcon)

	def get_RenewInfoId(self):
		return self.get_query_params().get('RenewInfoId')

	def set_RenewInfoId(self,RenewInfoId):
		self.add_query_param('RenewInfoId',RenewInfoId)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_RootCode(self):
		return self.get_query_params().get('RootCode')

	def set_RootCode(self,RootCode):
		self.add_query_param('RootCode',RootCode)

	def get_LoaOssKey(self):
		return self.get_query_params().get('LoaOssKey')

	def set_LoaOssKey(self,LoaOssKey):
		self.add_query_param('LoaOssKey',LoaOssKey)

	def get_RegisterNumber(self):
		return self.get_query_params().get('RegisterNumber')

	def set_RegisterNumber(self,RegisterNumber):
		self.add_query_param('RegisterNumber',RegisterNumber)