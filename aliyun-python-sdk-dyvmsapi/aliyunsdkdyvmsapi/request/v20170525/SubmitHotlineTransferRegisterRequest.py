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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class SubmitHotlineTransferRegisterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'SubmitHotlineTransferRegister','dyvms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OperatorIdentityCard(self):
		return self.get_query_params().get('OperatorIdentityCard')

	def set_OperatorIdentityCard(self,OperatorIdentityCard):
		self.add_query_param('OperatorIdentityCard',OperatorIdentityCard)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_OperatorMail(self):
		return self.get_query_params().get('OperatorMail')

	def set_OperatorMail(self,OperatorMail):
		self.add_query_param('OperatorMail',OperatorMail)

	def get_HotlineNumber(self):
		return self.get_query_params().get('HotlineNumber')

	def set_HotlineNumber(self,HotlineNumber):
		self.add_query_param('HotlineNumber',HotlineNumber)

	def get_TransferPhoneNumberInfoss(self):
		return self.get_query_params().get('TransferPhoneNumberInfos')

	def set_TransferPhoneNumberInfoss(self, TransferPhoneNumberInfoss):
		for depth1 in range(len(TransferPhoneNumberInfoss)):
			if TransferPhoneNumberInfoss[depth1].get('PhoneNumber') is not None:
				self.add_query_param('TransferPhoneNumberInfos.' + str(depth1 + 1) + '.PhoneNumber', TransferPhoneNumberInfoss[depth1].get('PhoneNumber'))
			if TransferPhoneNumberInfoss[depth1].get('PhoneNumberOwnerName') is not None:
				self.add_query_param('TransferPhoneNumberInfos.' + str(depth1 + 1) + '.PhoneNumberOwnerName', TransferPhoneNumberInfoss[depth1].get('PhoneNumberOwnerName'))
			if TransferPhoneNumberInfoss[depth1].get('IdentityCard') is not None:
				self.add_query_param('TransferPhoneNumberInfos.' + str(depth1 + 1) + '.IdentityCard', TransferPhoneNumberInfoss[depth1].get('IdentityCard'))

	def get_OperatorMobileVerifyCode(self):
		return self.get_query_params().get('OperatorMobileVerifyCode')

	def set_OperatorMobileVerifyCode(self,OperatorMobileVerifyCode):
		self.add_query_param('OperatorMobileVerifyCode',OperatorMobileVerifyCode)

	def get_Agreement(self):
		return self.get_query_params().get('Agreement')

	def set_Agreement(self,Agreement):
		self.add_query_param('Agreement',Agreement)

	def get_QualificationId(self):
		return self.get_query_params().get('QualificationId')

	def set_QualificationId(self,QualificationId):
		self.add_query_param('QualificationId',QualificationId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_OperatorMobile(self):
		return self.get_query_params().get('OperatorMobile')

	def set_OperatorMobile(self,OperatorMobile):
		self.add_query_param('OperatorMobile',OperatorMobile)

	def get_OperatorMailVerifyCode(self):
		return self.get_query_params().get('OperatorMailVerifyCode')

	def set_OperatorMailVerifyCode(self,OperatorMailVerifyCode):
		self.add_query_param('OperatorMailVerifyCode',OperatorMailVerifyCode)

	def get_OperatorName(self):
		return self.get_query_params().get('OperatorName')

	def set_OperatorName(self,OperatorName):
		self.add_query_param('OperatorName',OperatorName)