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

class CreateInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'SWAS-OPEN', '2020-06-01', 'CreateInstances','SWAS-OPEN')
		self.set_method('POST')

	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_AutoRenewPeriod(self): # Integer
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self, AutoRenewPeriod):  # Integer
		self.add_query_param('AutoRenewPeriod', AutoRenewPeriod)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_DataDiskSize(self): # Long
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self, DataDiskSize):  # Long
		self.add_query_param('DataDiskSize', DataDiskSize)
	def get_PlanId(self): # String
		return self.get_query_params().get('PlanId')

	def set_PlanId(self, PlanId):  # String
		self.add_query_param('PlanId', PlanId)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
