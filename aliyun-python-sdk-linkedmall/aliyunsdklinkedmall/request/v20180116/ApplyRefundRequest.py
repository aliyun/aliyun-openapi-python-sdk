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
from aliyunsdklinkedmall.endpoint import endpoint_data

class ApplyRefundRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'ApplyRefund','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BizUid(self):
		return self.get_query_params().get('BizUid')

	def set_BizUid(self,BizUid):
		self.add_query_param('BizUid',BizUid)

	def get_BizClaimType(self):
		return self.get_query_params().get('BizClaimType')

	def set_BizClaimType(self,BizClaimType):
		self.add_query_param('BizClaimType',BizClaimType)

	def get_ApplyReasonTextId(self):
		return self.get_query_params().get('ApplyReasonTextId')

	def set_ApplyReasonTextId(self,ApplyReasonTextId):
		self.add_query_param('ApplyReasonTextId',ApplyReasonTextId)

	def get_AccountType(self):
		return self.get_query_params().get('AccountType')

	def set_AccountType(self,AccountType):
		self.add_query_param('AccountType',AccountType)

	def get_UseAnonymousTbAccount(self):
		return self.get_query_params().get('UseAnonymousTbAccount')

	def set_UseAnonymousTbAccount(self,UseAnonymousTbAccount):
		self.add_query_param('UseAnonymousTbAccount',UseAnonymousTbAccount)

	def get_LeavePictureLists(self):
		return self.get_body_params().get('LeavePictureLists')

	def set_LeavePictureLists(self,LeavePictureLists):
		for i in range(len(LeavePictureLists)):	
			if LeavePictureLists[i].get('Picture') is not None:
				self.add_body_params('LeavePictureList.' + str(i + 1) + '.Picture' , LeavePictureLists[i].get('Picture'))
			if LeavePictureLists[i].get('Desc') is not None:
				self.add_body_params('LeavePictureList.' + str(i + 1) + '.Desc' , LeavePictureLists[i].get('Desc'))


	def get_ApplyRefundCount(self):
		return self.get_query_params().get('ApplyRefundCount')

	def set_ApplyRefundCount(self,ApplyRefundCount):
		self.add_query_param('ApplyRefundCount',ApplyRefundCount)

	def get_GoodsStatus(self):
		return self.get_query_params().get('GoodsStatus')

	def set_GoodsStatus(self,GoodsStatus):
		self.add_query_param('GoodsStatus',GoodsStatus)

	def get_SubLmOrderId(self):
		return self.get_query_params().get('SubLmOrderId')

	def set_SubLmOrderId(self,SubLmOrderId):
		self.add_query_param('SubLmOrderId',SubLmOrderId)

	def get_ThirdPartyUserId(self):
		return self.get_query_params().get('ThirdPartyUserId')

	def set_ThirdPartyUserId(self,ThirdPartyUserId):
		self.add_query_param('ThirdPartyUserId',ThirdPartyUserId)

	def get_ApplyRefundFee(self):
		return self.get_query_params().get('ApplyRefundFee')

	def set_ApplyRefundFee(self,ApplyRefundFee):
		self.add_query_param('ApplyRefundFee',ApplyRefundFee)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_LeaveMessage(self):
		return self.get_body_params().get('LeaveMessage')

	def set_LeaveMessage(self,LeaveMessage):
		self.add_body_params('LeaveMessage', LeaveMessage)