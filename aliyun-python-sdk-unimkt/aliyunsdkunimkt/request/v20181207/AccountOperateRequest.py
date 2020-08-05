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
from aliyunsdkunimkt.endpoint import endpoint_data

class AccountOperateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-07', 'AccountOperate','uniMkt')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AccountManagerNumber(self):
		return self.get_body_params().get('AccountManagerNumber')

	def set_AccountManagerNumber(self,AccountManagerNumber):
		self.add_body_params('AccountManagerNumber', AccountManagerNumber)

	def get_FromUserId(self):
		return self.get_body_params().get('FromUserId')

	def set_FromUserId(self,FromUserId):
		self.add_body_params('FromUserId', FromUserId)

	def get_ToAccountNo(self):
		return self.get_body_params().get('ToAccountNo')

	def set_ToAccountNo(self,ToAccountNo):
		self.add_body_params('ToAccountNo', ToAccountNo)

	def get_CataloguePrice(self):
		return self.get_body_params().get('CataloguePrice')

	def set_CataloguePrice(self,CataloguePrice):
		self.add_body_params('CataloguePrice', CataloguePrice)

	def get_BpId(self):
		return self.get_body_params().get('BpId')

	def set_BpId(self,BpId):
		self.add_body_params('BpId', BpId)

	def get_OperateName(self):
		return self.get_body_params().get('OperateName')

	def set_OperateName(self,OperateName):
		self.add_body_params('OperateName', OperateName)

	def get_Balance(self):
		return self.get_body_params().get('Balance')

	def set_Balance(self,Balance):
		self.add_body_params('Balance', Balance)

	def get_ActualAmount(self):
		return self.get_body_params().get('ActualAmount')

	def set_ActualAmount(self,ActualAmount):
		self.add_body_params('ActualAmount', ActualAmount)

	def get_ProxyUserNick(self):
		return self.get_body_params().get('ProxyUserNick')

	def set_ProxyUserNick(self,ProxyUserNick):
		self.add_body_params('ProxyUserNick', ProxyUserNick)

	def get_FromAccountNo(self):
		return self.get_body_params().get('FromAccountNo')

	def set_FromAccountNo(self,FromAccountNo):
		self.add_body_params('FromAccountNo', FromAccountNo)

	def get_PriceVersion(self):
		return self.get_body_params().get('PriceVersion')

	def set_PriceVersion(self,PriceVersion):
		self.add_body_params('PriceVersion', PriceVersion)

	def get_CreateTime(self):
		return self.get_body_params().get('CreateTime')

	def set_CreateTime(self,CreateTime):
		self.add_body_params('CreateTime', CreateTime)

	def get_Amount(self):
		return self.get_body_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_body_params('Amount', Amount)

	def get_AccountManagerName(self):
		return self.get_body_params().get('AccountManagerName')

	def set_AccountManagerName(self,AccountManagerName):
		self.add_body_params('AccountManagerName', AccountManagerName)

	def get_ToUserId(self):
		return self.get_body_params().get('ToUserId')

	def set_ToUserId(self,ToUserId):
		self.add_body_params('ToUserId', ToUserId)

	def get_MarketCount(self):
		return self.get_body_params().get('MarketCount')

	def set_MarketCount(self,MarketCount):
		self.add_body_params('MarketCount', MarketCount)

	def get_ProxyUserId(self):
		return self.get_body_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_body_params('ProxyUserId', ProxyUserId)

	def get_DiscountRate(self):
		return self.get_body_params().get('DiscountRate')

	def set_DiscountRate(self,DiscountRate):
		self.add_body_params('DiscountRate', DiscountRate)

	def get_AccuActualAmount(self):
		return self.get_body_params().get('AccuActualAmount')

	def set_AccuActualAmount(self,AccuActualAmount):
		self.add_body_params('AccuActualAmount', AccuActualAmount)

	def get_FlowId(self):
		return self.get_body_params().get('FlowId')

	def set_FlowId(self,FlowId):
		self.add_body_params('FlowId', FlowId)

	def get_PreDebit(self):
		return self.get_body_params().get('PreDebit')

	def set_PreDebit(self,PreDebit):
		self.add_body_params('PreDebit', PreDebit)

	def get_AccuAmount(self):
		return self.get_body_params().get('AccuAmount')

	def set_AccuAmount(self,AccuAmount):
		self.add_body_params('AccuAmount', AccuAmount)