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
from aliyunsdkcloudapi.endpoint import endpoint_data

class CreateInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateInstance','apigateway')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_InstanceSpec(self):
		return self.get_query_params().get('InstanceSpec')

	def set_InstanceSpec(self,InstanceSpec):
		self.add_query_param('InstanceSpec',InstanceSpec)

	def get_HttpsPolicy(self):
		return self.get_query_params().get('HttpsPolicy')

	def set_HttpsPolicy(self,HttpsPolicy):
		self.add_query_param('HttpsPolicy',HttpsPolicy)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)