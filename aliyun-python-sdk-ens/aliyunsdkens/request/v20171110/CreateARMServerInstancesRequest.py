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

class CreateARMServerInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateARMServerInstances','ens')
		self.set_method('POST')

	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_Resolution(self): # String
		return self.get_query_params().get('Resolution')

	def set_Resolution(self, Resolution):  # String
		self.add_query_param('Resolution', Resolution)
	def get_Frequency(self): # Integer
		return self.get_query_params().get('Frequency')

	def set_Frequency(self, Frequency):  # Integer
		self.add_query_param('Frequency', Frequency)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ServerType(self): # String
		return self.get_query_params().get('ServerType')

	def set_ServerType(self, ServerType):  # String
		self.add_query_param('ServerType', ServerType)
	def get_AutoUseCoupon(self): # Boolean
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # Boolean
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_EnvironmentVar(self): # String
		return self.get_query_params().get('EnvironmentVar')

	def set_EnvironmentVar(self, EnvironmentVar):  # String
		self.add_query_param('EnvironmentVar', EnvironmentVar)
	def get_NameSpace(self): # String
		return self.get_query_params().get('NameSpace')

	def set_NameSpace(self, NameSpace):  # String
		self.add_query_param('NameSpace', NameSpace)
	def get_ServerName(self): # String
		return self.get_query_params().get('ServerName')

	def set_ServerName(self, ServerName):  # String
		self.add_query_param('ServerName', ServerName)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
