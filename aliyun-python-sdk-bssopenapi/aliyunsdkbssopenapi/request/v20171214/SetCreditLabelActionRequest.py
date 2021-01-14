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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class SetCreditLabelActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'SetCreditLabelAction')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ActionType(self):
		return self.get_query_params().get('ActionType')

	def set_ActionType(self,ActionType):
		self.add_query_param('ActionType',ActionType)

	def get_IsNeedSaveNotifyRule(self):
		return self.get_query_params().get('IsNeedSaveNotifyRule')

	def set_IsNeedSaveNotifyRule(self,IsNeedSaveNotifyRule):
		self.add_query_param('IsNeedSaveNotifyRule',IsNeedSaveNotifyRule)

	def get_IsNeedAdjustCreditAccount(self):
		return self.get_query_params().get('IsNeedAdjustCreditAccount')

	def set_IsNeedAdjustCreditAccount(self,IsNeedAdjustCreditAccount):
		self.add_query_param('IsNeedAdjustCreditAccount',IsNeedAdjustCreditAccount)

	def get_NewCreateMode(self):
		return self.get_query_params().get('NewCreateMode')

	def set_NewCreateMode(self,NewCreateMode):
		self.add_query_param('NewCreateMode',NewCreateMode)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_CurrencyCode(self):
		return self.get_query_params().get('CurrencyCode')

	def set_CurrencyCode(self,CurrencyCode):
		self.add_query_param('CurrencyCode',CurrencyCode)

	def get_DailyCycle(self):
		return self.get_query_params().get('DailyCycle')

	def set_DailyCycle(self,DailyCycle):
		self.add_query_param('DailyCycle',DailyCycle)

	def get_Operator(self):
		return self.get_query_params().get('Operator')

	def set_Operator(self,Operator):
		self.add_query_param('Operator',Operator)

	def get_Uid(self):
		return self.get_query_params().get('Uid')

	def set_Uid(self,Uid):
		self.add_query_param('Uid',Uid)

	def get_SiteCode(self):
		return self.get_query_params().get('SiteCode')

	def set_SiteCode(self,SiteCode):
		self.add_query_param('SiteCode',SiteCode)

	def get_ClearCycle(self):
		return self.get_query_params().get('ClearCycle')

	def set_ClearCycle(self,ClearCycle):
		self.add_query_param('ClearCycle',ClearCycle)

	def get_NeedNotice(self):
		return self.get_query_params().get('NeedNotice')

	def set_NeedNotice(self,NeedNotice):
		self.add_query_param('NeedNotice',NeedNotice)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_IsNeedSetCreditAmount(self):
		return self.get_query_params().get('IsNeedSetCreditAmount')

	def set_IsNeedSetCreditAmount(self,IsNeedSetCreditAmount):
		self.add_query_param('IsNeedSetCreditAmount',IsNeedSetCreditAmount)

	def get_CreditAmount(self):
		return self.get_query_params().get('CreditAmount')

	def set_CreditAmount(self,CreditAmount):
		self.add_query_param('CreditAmount',CreditAmount)

	def get_IsNeedAddSettleLabel(self):
		return self.get_query_params().get('IsNeedAddSettleLabel')

	def set_IsNeedAddSettleLabel(self,IsNeedAddSettleLabel):
		self.add_query_param('IsNeedAddSettleLabel',IsNeedAddSettleLabel)