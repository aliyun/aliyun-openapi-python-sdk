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
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateCluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BusinessCode(self): # String
		return self.get_query_params().get('BusinessCode')

	def set_BusinessCode(self, BusinessCode):  # String
		self.add_query_param('BusinessCode', BusinessCode)
	def get_CreateWithLogIntegration(self): # Boolean
		return self.get_query_params().get('CreateWithLogIntegration')

	def set_CreateWithLogIntegration(self, CreateWithLogIntegration):  # Boolean
		self.add_query_param('CreateWithLogIntegration', CreateWithLogIntegration)
	def get_Vswitchidss(self): # RepeatList
		return self.get_query_params().get('Vswitchids')

	def set_Vswitchidss(self, Vswitchids):  # RepeatList
		for depth1 in range(len(Vswitchids)):
			self.add_query_param('Vswitchids.' + str(depth1 + 1), Vswitchids[depth1])
	def get_CloudMonitorFlags(self): # Integer
		return self.get_query_params().get('CloudMonitorFlags')

	def set_CloudMonitorFlags(self, CloudMonitorFlags):  # Integer
		self.add_query_param('CloudMonitorFlags', CloudMonitorFlags)
	def get_ClusterEnvType(self): # String
		return self.get_query_params().get('ClusterEnvType')

	def set_ClusterEnvType(self, ClusterEnvType):  # String
		self.add_query_param('ClusterEnvType', ClusterEnvType)
	def get_CreateWithArmsIntegration(self): # Boolean
		return self.get_query_params().get('CreateWithArmsIntegration')

	def set_CreateWithArmsIntegration(self, CreateWithArmsIntegration):  # Boolean
		self.add_query_param('CreateWithArmsIntegration', CreateWithArmsIntegration)
	def get_KeyPair(self): # String
		return self.get_query_params().get('KeyPair')

	def set_KeyPair(self, KeyPair):  # String
		self.add_query_param('KeyPair', KeyPair)
	def get_ClusterTitle(self): # String
		return self.get_query_params().get('ClusterTitle')

	def set_ClusterTitle(self, ClusterTitle):  # String
		self.add_query_param('ClusterTitle', ClusterTitle)
	def get_PodCIDR(self): # String
		return self.get_query_params().get('PodCIDR')

	def set_PodCIDR(self, PodCIDR):  # String
		self.add_query_param('PodCIDR', PodCIDR)
	def get_ClusterId(self): # Long
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # Long
		self.add_query_param('ClusterId', ClusterId)
	def get_ClusterType(self): # String
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # String
		self.add_query_param('ClusterType', ClusterType)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_SnatEntry(self): # Integer
		return self.get_query_params().get('SnatEntry')

	def set_SnatEntry(self, SnatEntry):  # Integer
		self.add_query_param('SnatEntry', SnatEntry)
	def get_NetPlug(self): # String
		return self.get_query_params().get('NetPlug')

	def set_NetPlug(self, NetPlug):  # String
		self.add_query_param('NetPlug', NetPlug)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_RegionName(self): # String
		return self.get_query_params().get('RegionName')

	def set_RegionName(self, RegionName):  # String
		self.add_query_param('RegionName', RegionName)
	def get_PrivateZone(self): # Boolean
		return self.get_query_params().get('PrivateZone')

	def set_PrivateZone(self, PrivateZone):  # Boolean
		self.add_query_param('PrivateZone', PrivateZone)
	def get_ServiceCIDR(self): # String
		return self.get_query_params().get('ServiceCIDR')

	def set_ServiceCIDR(self, ServiceCIDR):  # String
		self.add_query_param('ServiceCIDR', ServiceCIDR)
	def get_PublicSlb(self): # Integer
		return self.get_query_params().get('PublicSlb')

	def set_PublicSlb(self, PublicSlb):  # Integer
		self.add_query_param('PublicSlb', PublicSlb)
