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

	def get_ActionType(self): # String
		return self.get_query_params().get('ActionType')

	def set_ActionType(self, ActionType):  # String
		self.add_query_param('ActionType', ActionType)
	def get_IsNeedSaveNotifyRule(self): # String
		return self.get_query_params().get('IsNeedSaveNotifyRule')

	def set_IsNeedSaveNotifyRule(self, IsNeedSaveNotifyRule):  # String
		self.add_query_param('IsNeedSaveNotifyRule', IsNeedSaveNotifyRule)
	def get_IsNeedAdjustCreditAccount(self): # String
		return self.get_query_params().get('IsNeedAdjustCreditAccount')

	def set_IsNeedAdjustCreditAccount(self, IsNeedAdjustCreditAccount):  # String
		self.add_query_param('IsNeedAdjustCreditAccount', IsNeedAdjustCreditAccount)
	def get_NewCreateMode(self): # Boolean
		return self.get_query_params().get('NewCreateMode')

	def set_NewCreateMode(self, NewCreateMode):  # Boolean
		self.add_query_param('NewCreateMode', NewCreateMode)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_CurrencyCode(self): # String
		return self.get_query_params().get('CurrencyCode')

	def set_CurrencyCode(self, CurrencyCode):  # String
		self.add_query_param('CurrencyCode', CurrencyCode)
	def get_DailyCycle(self): # String
		return self.get_query_params().get('DailyCycle')

	def set_DailyCycle(self, DailyCycle):  # String
		self.add_query_param('DailyCycle', DailyCycle)
	def get_Operator(self): # String
		return self.get_query_params().get('Operator')

	def set_Operator(self, Operator):  # String
		self.add_query_param('Operator', Operator)
	def get_Uid(self): # String
		return self.get_query_params().get('Uid')

	def set_Uid(self, Uid):  # String
		self.add_query_param('Uid', Uid)
	def get_SiteCode(self): # String
		return self.get_query_params().get('SiteCode')

	def set_SiteCode(self, SiteCode):  # String
		self.add_query_param('SiteCode', SiteCode)
	def get_ClearCycle(self): # String
		return self.get_query_params().get('ClearCycle')

	def set_ClearCycle(self, ClearCycle):  # String
		self.add_query_param('ClearCycle', ClearCycle)
	def get_NeedNotice(self): # Boolean
		return self.get_query_params().get('NeedNotice')

	def set_NeedNotice(self, NeedNotice):  # Boolean
		self.add_query_param('NeedNotice', NeedNotice)
	def get_RequestId(self): # String
		return self.get_query_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_query_param('RequestId', RequestId)
	def get_IsNeedSetCreditAmount(self): # String
		return self.get_query_params().get('IsNeedSetCreditAmount')

	def set_IsNeedSetCreditAmount(self, IsNeedSetCreditAmount):  # String
		self.add_query_param('IsNeedSetCreditAmount', IsNeedSetCreditAmount)
	def get_CreditAmount(self): # String
		return self.get_query_params().get('CreditAmount')

	def set_CreditAmount(self, CreditAmount):  # String
		self.add_query_param('CreditAmount', CreditAmount)
	def get_IsNeedAddSettleLabel(self): # String
		return self.get_query_params().get('IsNeedAddSettleLabel')

	def set_IsNeedAddSettleLabel(self, IsNeedAddSettleLabel):  # String
		self.add_query_param('IsNeedAddSettleLabel', IsNeedAddSettleLabel)
