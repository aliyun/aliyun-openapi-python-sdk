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
from aliyunsdksas.endpoint import endpoint_data

class CreateSasOrderRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateSasOrder','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SasWebguardBoolean(self):
		return self.get_query_params().get('SasWebguardBoolean')

	def set_SasWebguardBoolean(self,SasWebguardBoolean):
		self.add_query_param('SasWebguardBoolean',SasWebguardBoolean)

	def get_AutoUseCoupon(self):
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self,AutoUseCoupon):
		self.add_query_param('AutoUseCoupon',AutoUseCoupon)

	def get_Spec(self):
		return self.get_query_params().get('Spec')

	def set_Spec(self,Spec):
		self.add_query_param('Spec',Spec)

	def get_InstanceCount(self):
		return self.get_query_params().get('InstanceCount')

	def set_InstanceCount(self,InstanceCount):
		self.add_query_param('InstanceCount',InstanceCount)

	def get_SasWebguardOrderNum(self):
		return self.get_query_params().get('SasWebguardOrderNum')

	def set_SasWebguardOrderNum(self,SasWebguardOrderNum):
		self.add_query_param('SasWebguardOrderNum',SasWebguardOrderNum)

	def get_ContainerImageScan(self):
		return self.get_query_params().get('ContainerImageScan')

	def set_ContainerImageScan(self,ContainerImageScan):
		self.add_query_param('ContainerImageScan',ContainerImageScan)

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

	def get_SasAntiRansomware(self):
		return self.get_query_params().get('SasAntiRansomware')

	def set_SasAntiRansomware(self,SasAntiRansomware):
		self.add_query_param('SasAntiRansomware',SasAntiRansomware)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_SasSc(self):
		return self.get_query_params().get('SasSc')

	def set_SasSc(self,SasSc):
		self.add_query_param('SasSc',SasSc)

	def get_Vcore(self):
		return self.get_query_params().get('Vcore')

	def set_Vcore(self,Vcore):
		self.add_query_param('Vcore',Vcore)

	def get_SasSlsStorage(self):
		return self.get_query_params().get('SasSlsStorage')

	def set_SasSlsStorage(self,SasSlsStorage):
		self.add_query_param('SasSlsStorage',SasSlsStorage)

	def get_SasProductService(self):
		return self.get_query_params().get('SasProductService')

	def set_SasProductService(self,SasProductService):
		self.add_query_param('SasProductService',SasProductService)