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
from aliyunsdkhbase.endpoint import endpoint_data

class EnableHBaseueModuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'EnableHBaseueModule','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ModuleTypeName(self):
		return self.get_query_params().get('ModuleTypeName')

	def set_ModuleTypeName(self,ModuleTypeName):
		self.add_query_param('ModuleTypeName',ModuleTypeName)

	def get_HbaseueClusterId(self):
		return self.get_query_params().get('HbaseueClusterId')

	def set_HbaseueClusterId(self,HbaseueClusterId):
		self.add_query_param('HbaseueClusterId',HbaseueClusterId)

	def get_BdsId(self):
		return self.get_query_params().get('BdsId')

	def set_BdsId(self,BdsId):
		self.add_query_param('BdsId',BdsId)

	def get_ModuleClusterName(self):
		return self.get_query_params().get('ModuleClusterName')

	def set_ModuleClusterName(self,ModuleClusterName):
		self.add_query_param('ModuleClusterName',ModuleClusterName)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DiskSize(self):
		return self.get_query_params().get('DiskSize')

	def set_DiskSize(self,DiskSize):
		self.add_query_param('DiskSize',DiskSize)

	def get_MasterInstanceType(self):
		return self.get_query_params().get('MasterInstanceType')

	def set_MasterInstanceType(self,MasterInstanceType):
		self.add_query_param('MasterInstanceType',MasterInstanceType)

	def get_DiskType(self):
		return self.get_query_params().get('DiskType')

	def set_DiskType(self,DiskType):
		self.add_query_param('DiskType',DiskType)

	def get_VswitchId(self):
		return self.get_query_params().get('VswitchId')

	def set_VswitchId(self,VswitchId):
		self.add_query_param('VswitchId',VswitchId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_CoreInstanceType(self):
		return self.get_query_params().get('CoreInstanceType')

	def set_CoreInstanceType(self,CoreInstanceType):
		self.add_query_param('CoreInstanceType',CoreInstanceType)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_NodeCount(self):
		return self.get_query_params().get('NodeCount')

	def set_NodeCount(self,NodeCount):
		self.add_query_param('NodeCount',NodeCount)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)