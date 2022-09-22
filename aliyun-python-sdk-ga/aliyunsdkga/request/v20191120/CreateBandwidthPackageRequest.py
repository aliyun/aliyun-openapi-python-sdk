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
from aliyunsdkga.endpoint import endpoint_data

class CreateBandwidthPackageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateBandwidthPackage','gaplus')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BandwidthType(self): # String
		return self.get_query_params().get('BandwidthType')

	def set_BandwidthType(self, BandwidthType):  # String
		self.add_query_param('BandwidthType', BandwidthType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_AutoUseCoupon(self): # String
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # String
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_AutoRenewDuration(self): # Integer
		return self.get_query_params().get('AutoRenewDuration')

	def set_AutoRenewDuration(self, AutoRenewDuration):  # Integer
		self.add_query_param('AutoRenewDuration', AutoRenewDuration)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_CbnGeographicRegionIdB(self): # String
		return self.get_query_params().get('CbnGeographicRegionIdB')

	def set_CbnGeographicRegionIdB(self, CbnGeographicRegionIdB):  # String
		self.add_query_param('CbnGeographicRegionIdB', CbnGeographicRegionIdB)
	def get_CbnGeographicRegionIdA(self): # String
		return self.get_query_params().get('CbnGeographicRegionIdA')

	def set_CbnGeographicRegionIdA(self, CbnGeographicRegionIdA):  # String
		self.add_query_param('CbnGeographicRegionIdA', CbnGeographicRegionIdA)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_BillingType(self): # String
		return self.get_query_params().get('BillingType')

	def set_BillingType(self, BillingType):  # String
		self.add_query_param('BillingType', BillingType)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
	def get_Ratio(self): # Integer
		return self.get_query_params().get('Ratio')

	def set_Ratio(self, Ratio):  # Integer
		self.add_query_param('Ratio', Ratio)
