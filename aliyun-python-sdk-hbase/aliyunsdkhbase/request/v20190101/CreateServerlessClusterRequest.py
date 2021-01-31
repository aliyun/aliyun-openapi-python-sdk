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

class CreateServerlessClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'CreateServerlessCluster','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientType(self):
		return self.get_query_params().get('ClientType')

	def set_ClientType(self,ClientType):
		self.add_query_param('ClientType',ClientType)

	def get_ClusterName(self):
		return self.get_query_params().get('ClusterName')

	def set_ClusterName(self,ClusterName):
		self.add_query_param('ClusterName',ClusterName)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_DiskType(self):
		return self.get_query_params().get('DiskType')

	def set_DiskType(self,DiskType):
		self.add_query_param('DiskType',DiskType)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PeriodUnit(self):
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self,PeriodUnit):
		self.add_query_param('PeriodUnit',PeriodUnit)

	def get_ServerlessCapability(self):
		return self.get_query_params().get('ServerlessCapability')

	def set_ServerlessCapability(self,ServerlessCapability):
		self.add_query_param('ServerlessCapability',ServerlessCapability)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_ServerlessStorage(self):
		return self.get_query_params().get('ServerlessStorage')

	def set_ServerlessStorage(self,ServerlessStorage):
		self.add_query_param('ServerlessStorage',ServerlessStorage)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_ServerlessSpec(self):
		return self.get_query_params().get('ServerlessSpec')

	def set_ServerlessSpec(self,ServerlessSpec):
		self.add_query_param('ServerlessSpec',ServerlessSpec)