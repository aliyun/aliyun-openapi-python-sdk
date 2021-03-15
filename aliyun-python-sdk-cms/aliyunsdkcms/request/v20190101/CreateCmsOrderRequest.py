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

class CreateCmsOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateCmsOrder','cms')
		self.set_method('POST')

	def get_SmsCount(self):
		return self.get_query_params().get('SmsCount')

	def set_SmsCount(self,SmsCount):
		self.add_query_param('SmsCount',SmsCount)

	def get_AutoUseCoupon(self):
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self,AutoUseCoupon):
		self.add_query_param('AutoUseCoupon',AutoUseCoupon)

	def get_LogMonitorStream(self):
		return self.get_query_params().get('LogMonitorStream')

	def set_LogMonitorStream(self,LogMonitorStream):
		self.add_query_param('LogMonitorStream',LogMonitorStream)

	def get_CustomTimeSeries(self):
		return self.get_query_params().get('CustomTimeSeries')

	def set_CustomTimeSeries(self,CustomTimeSeries):
		self.add_query_param('CustomTimeSeries',CustomTimeSeries)

	def get_ApiCount(self):
		return self.get_query_params().get('ApiCount')

	def set_ApiCount(self,ApiCount):
		self.add_query_param('ApiCount',ApiCount)

	def get_PhoneCount(self):
		return self.get_query_params().get('PhoneCount')

	def set_PhoneCount(self,PhoneCount):
		self.add_query_param('PhoneCount',PhoneCount)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_SuggestType(self):
		return self.get_query_params().get('SuggestType')

	def set_SuggestType(self,SuggestType):
		self.add_query_param('SuggestType',SuggestType)

	def get_EventStoreNum(self):
		return self.get_query_params().get('EventStoreNum')

	def set_EventStoreNum(self,EventStoreNum):
		self.add_query_param('EventStoreNum',EventStoreNum)

	def get_SiteTaskNum(self):
		return self.get_query_params().get('SiteTaskNum')

	def set_SiteTaskNum(self,SiteTaskNum):
		self.add_query_param('SiteTaskNum',SiteTaskNum)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_SiteOperatorNum(self):
		return self.get_query_params().get('SiteOperatorNum')

	def set_SiteOperatorNum(self,SiteOperatorNum):
		self.add_query_param('SiteOperatorNum',SiteOperatorNum)

	def get_SiteEcsNum(self):
		return self.get_query_params().get('SiteEcsNum')

	def set_SiteEcsNum(self,SiteEcsNum):
		self.add_query_param('SiteEcsNum',SiteEcsNum)

	def get_EventStoreTime(self):
		return self.get_query_params().get('EventStoreTime')

	def set_EventStoreTime(self,EventStoreTime):
		self.add_query_param('EventStoreTime',EventStoreTime)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)