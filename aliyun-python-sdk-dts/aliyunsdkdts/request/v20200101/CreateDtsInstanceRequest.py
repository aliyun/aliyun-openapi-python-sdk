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
from aliyunsdkdts.endpoint import endpoint_data

class CreateDtsInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'CreateDtsInstance','dts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoStart(self):
		return self.get_query_params().get('AutoStart')

	def set_AutoStart(self,AutoStart):
		self.add_query_param('AutoStart',AutoStart)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_InstanceClass(self):
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self,InstanceClass):
		self.add_query_param('InstanceClass',InstanceClass)

	def get_DatabaseCount(self):
		return self.get_query_params().get('DatabaseCount')

	def set_DatabaseCount(self,DatabaseCount):
		self.add_query_param('DatabaseCount',DatabaseCount)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_ComputeUnit(self):
		return self.get_query_params().get('ComputeUnit')

	def set_ComputeUnit(self,ComputeUnit):
		self.add_query_param('ComputeUnit',ComputeUnit)

	def get_DestinationRegion(self):
		return self.get_query_params().get('DestinationRegion')

	def set_DestinationRegion(self,DestinationRegion):
		self.add_query_param('DestinationRegion',DestinationRegion)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DestinationEndpointEngineName(self):
		return self.get_query_params().get('DestinationEndpointEngineName')

	def set_DestinationEndpointEngineName(self,DestinationEndpointEngineName):
		self.add_query_param('DestinationEndpointEngineName',DestinationEndpointEngineName)

	def get_Quantity(self):
		return self.get_query_params().get('Quantity')

	def set_Quantity(self,Quantity):
		self.add_query_param('Quantity',Quantity)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_UsedTime(self):
		return self.get_query_params().get('UsedTime')

	def set_UsedTime(self,UsedTime):
		self.add_query_param('UsedTime',UsedTime)

	def get_SyncArchitecture(self):
		return self.get_query_params().get('SyncArchitecture')

	def set_SyncArchitecture(self,SyncArchitecture):
		self.add_query_param('SyncArchitecture',SyncArchitecture)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_SourceRegion(self):
		return self.get_query_params().get('SourceRegion')

	def set_SourceRegion(self,SourceRegion):
		self.add_query_param('SourceRegion',SourceRegion)

	def get_SourceEndpointEngineName(self):
		return self.get_query_params().get('SourceEndpointEngineName')

	def set_SourceEndpointEngineName(self,SourceEndpointEngineName):
		self.add_query_param('SourceEndpointEngineName',SourceEndpointEngineName)