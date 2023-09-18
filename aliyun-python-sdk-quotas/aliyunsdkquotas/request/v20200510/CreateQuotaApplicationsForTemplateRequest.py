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
from aliyunsdkquotas.endpoint import endpoint_data

class CreateQuotaApplicationsForTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'CreateQuotaApplicationsForTemplate','quotas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Reason(self): # String
		return self.get_body_params().get('Reason')

	def set_Reason(self, Reason):  # String
		self.add_body_params('Reason', Reason)
	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_QuotaActionCode(self): # String
		return self.get_body_params().get('QuotaActionCode')

	def set_QuotaActionCode(self, QuotaActionCode):  # String
		self.add_body_params('QuotaActionCode', QuotaActionCode)
	def get_DesireValue(self): # Double
		return self.get_body_params().get('DesireValue')

	def set_DesireValue(self, DesireValue):  # Double
		self.add_body_params('DesireValue', DesireValue)
	def get_EffectiveTime(self): # String
		return self.get_body_params().get('EffectiveTime')

	def set_EffectiveTime(self, EffectiveTime):  # String
		self.add_body_params('EffectiveTime', EffectiveTime)
	def get_AliyunUidss(self): # RepeatList
		return self.get_body_params().get('AliyunUids')

	def set_AliyunUidss(self, AliyunUids):  # RepeatList
		for depth1 in range(len(AliyunUids)):
			self.add_body_params('AliyunUids.' + str(depth1 + 1), AliyunUids[depth1])
	def get_QuotaCategory(self): # String
		return self.get_body_params().get('QuotaCategory')

	def set_QuotaCategory(self, QuotaCategory):  # String
		self.add_body_params('QuotaCategory', QuotaCategory)
	def get_ExpireTime(self): # String
		return self.get_body_params().get('ExpireTime')

	def set_ExpireTime(self, ExpireTime):  # String
		self.add_body_params('ExpireTime', ExpireTime)
	def get_EnvLanguage(self): # String
		return self.get_body_params().get('EnvLanguage')

	def set_EnvLanguage(self, EnvLanguage):  # String
		self.add_body_params('EnvLanguage', EnvLanguage)
	def get_NoticeType(self): # Integer
		return self.get_body_params().get('NoticeType')

	def set_NoticeType(self, NoticeType):  # Integer
		self.add_body_params('NoticeType', NoticeType)
	def get_Dimensionss(self): # RepeatList
		return self.get_body_params().get('Dimensions')

	def set_Dimensionss(self, Dimensions):  # RepeatList
		for depth1 in range(len(Dimensions)):
			if Dimensions[depth1].get('Key') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Key', Dimensions[depth1].get('Key'))
			if Dimensions[depth1].get('Value') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Value', Dimensions[depth1].get('Value'))
