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
import json

class DescribePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribePrice','ens')
		self.set_method('POST')

	def get_DataDisks(self): # Array
		return self.get_query_params().get('DataDisks')

	def set_DataDisks(self, DataDisks):  # Array
		self.add_query_param("DataDisks", json.dumps(DataDisks))
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
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_DataDisk1Size(self): # Integer
		return self.get_query_params().get('DataDisk.1.Size')

	def set_DataDisk1Size(self, DataDisk1Size):  # Integer
		self.add_query_param('DataDisk.1.Size', DataDisk1Size)
	def get_Quantity(self): # Integer
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # Integer
		self.add_query_param('Quantity', Quantity)
	def get_SystemDiskSize(self): # Integer
		return self.get_query_params().get('SystemDisk.Size')

	def set_SystemDiskSize(self, SystemDiskSize):  # Integer
		self.add_query_param('SystemDisk.Size', SystemDiskSize)
