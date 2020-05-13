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
from aliyunsdkretailcloud.endpoint import endpoint_data

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateCluster','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BusinessCode(self):
		return self.get_query_params().get('BusinessCode')

	def set_BusinessCode(self,BusinessCode):
		self.add_query_param('BusinessCode',BusinessCode)

	def get_CreateWithLogIntegration(self):
		return self.get_query_params().get('CreateWithLogIntegration')

	def set_CreateWithLogIntegration(self,CreateWithLogIntegration):
		self.add_query_param('CreateWithLogIntegration',CreateWithLogIntegration)

	def get_Vswitchidss(self):
		return self.get_query_params().get('Vswitchidss')

	def set_Vswitchidss(self, Vswitchidss):
		for depth1 in range(len(Vswitchidss)):
			if Vswitchidss[depth1] is not None:
				self.add_query_param('Vswitchids.' + str(depth1 + 1) , Vswitchidss[depth1])

	def get_CloudMonitorFlags(self):
		return self.get_query_params().get('CloudMonitorFlags')

	def set_CloudMonitorFlags(self,CloudMonitorFlags):
		self.add_query_param('CloudMonitorFlags',CloudMonitorFlags)

	def get_ClusterEnvType(self):
		return self.get_query_params().get('ClusterEnvType')

	def set_ClusterEnvType(self,ClusterEnvType):
		self.add_query_param('ClusterEnvType',ClusterEnvType)

	def get_CreateWithArmsIntegration(self):
		return self.get_query_params().get('CreateWithArmsIntegration')

	def set_CreateWithArmsIntegration(self,CreateWithArmsIntegration):
		self.add_query_param('CreateWithArmsIntegration',CreateWithArmsIntegration)

	def get_KeyPair(self):
		return self.get_query_params().get('KeyPair')

	def set_KeyPair(self,KeyPair):
		self.add_query_param('KeyPair',KeyPair)

	def get_ClusterTitle(self):
		return self.get_query_params().get('ClusterTitle')

	def set_ClusterTitle(self,ClusterTitle):
		self.add_query_param('ClusterTitle',ClusterTitle)

	def get_PodCIDR(self):
		return self.get_query_params().get('PodCIDR')

	def set_PodCIDR(self,PodCIDR):
		self.add_query_param('PodCIDR',PodCIDR)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_SnatEntry(self):
		return self.get_query_params().get('SnatEntry')

	def set_SnatEntry(self,SnatEntry):
		self.add_query_param('SnatEntry',SnatEntry)

	def get_NetPlug(self):
		return self.get_query_params().get('NetPlug')

	def set_NetPlug(self,NetPlug):
		self.add_query_param('NetPlug',NetPlug)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_RegionName(self):
		return self.get_query_params().get('RegionName')

	def set_RegionName(self,RegionName):
		self.add_query_param('RegionName',RegionName)

	def get_PrivateZone(self):
		return self.get_query_params().get('PrivateZone')

	def set_PrivateZone(self,PrivateZone):
		self.add_query_param('PrivateZone',PrivateZone)

	def get_ServiceCIDR(self):
		return self.get_query_params().get('ServiceCIDR')

	def set_ServiceCIDR(self,ServiceCIDR):
		self.add_query_param('ServiceCIDR',ServiceCIDR)

	def get_PublicSlb(self):
		return self.get_query_params().get('PublicSlb')

	def set_PublicSlb(self,PublicSlb):
		self.add_query_param('PublicSlb',PublicSlb)