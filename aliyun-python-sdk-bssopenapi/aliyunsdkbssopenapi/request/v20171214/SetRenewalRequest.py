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

class SetRenewalRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'SetRenewal','bssopenapi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_query_param('ProductCode',ProductCode)

	def get_SubscriptionType(self):
		return self.get_query_params().get('SubscriptionType')

	def set_SubscriptionType(self,SubscriptionType):
		self.add_query_param('SubscriptionType',SubscriptionType)

	def get_RenewalPeriod(self):
		return self.get_query_params().get('RenewalPeriod')

	def set_RenewalPeriod(self,RenewalPeriod):
		self.add_query_param('RenewalPeriod',RenewalPeriod)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ProductType(self):
		return self.get_query_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_query_param('ProductType',ProductType)

	def get_InstanceIDs(self):
		return self.get_query_params().get('InstanceIDs')

	def set_InstanceIDs(self,InstanceIDs):
		self.add_query_param('InstanceIDs',InstanceIDs)

	def get_RenewalStatus(self):
		return self.get_query_params().get('RenewalStatus')

	def set_RenewalStatus(self,RenewalStatus):
		self.add_query_param('RenewalStatus',RenewalStatus)

	def get_RenewalPeriodUnit(self):
		return self.get_query_params().get('RenewalPeriodUnit')

	def set_RenewalPeriodUnit(self,RenewalPeriodUnit):
		self.add_query_param('RenewalPeriodUnit',RenewalPeriodUnit)