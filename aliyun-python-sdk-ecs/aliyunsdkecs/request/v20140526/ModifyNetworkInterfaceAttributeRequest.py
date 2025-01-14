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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyNetworkInterfaceAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyNetworkInterfaceAttribute','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueueNumber(self): # Integer
		return self.get_query_params().get('QueueNumber')

	def set_QueueNumber(self, QueueNumber):  # Integer
		self.add_query_param('QueueNumber', QueueNumber)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SecurityGroupIds(self): # RepeatList
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupIds(self, SecurityGroupId):  # RepeatList
		for depth1 in range(len(SecurityGroupId)):
			self.add_query_param('SecurityGroupId.' + str(depth1 + 1), SecurityGroupId[depth1])
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_NetworkInterfaceTrafficConfig(self): # Struct
		return self.get_query_params().get('NetworkInterfaceTrafficConfig')

	def set_NetworkInterfaceTrafficConfig(self, NetworkInterfaceTrafficConfig):  # Struct
		if NetworkInterfaceTrafficConfig.get('NetworkInterfaceTrafficMode') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.NetworkInterfaceTrafficMode', NetworkInterfaceTrafficConfig.get('NetworkInterfaceTrafficMode'))
		if NetworkInterfaceTrafficConfig.get('QueueNumber') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.QueueNumber', NetworkInterfaceTrafficConfig.get('QueueNumber'))
		if NetworkInterfaceTrafficConfig.get('QueuePairNumber') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.QueuePairNumber', NetworkInterfaceTrafficConfig.get('QueuePairNumber'))
		if NetworkInterfaceTrafficConfig.get('RxQueueSize') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.RxQueueSize', NetworkInterfaceTrafficConfig.get('RxQueueSize'))
		if NetworkInterfaceTrafficConfig.get('TxQueueSize') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.TxQueueSize', NetworkInterfaceTrafficConfig.get('TxQueueSize'))
	def get_EnhancedNetwork(self): # Struct
		return self.get_query_params().get('EnhancedNetwork')

	def set_EnhancedNetwork(self, EnhancedNetwork):  # Struct
		if EnhancedNetwork.get('EnableSriov') is not None:
			self.add_query_param('EnhancedNetwork.EnableSriov', EnhancedNetwork.get('EnableSriov'))
		if EnhancedNetwork.get('EnableRss') is not None:
			self.add_query_param('EnhancedNetwork.EnableRss', EnhancedNetwork.get('EnableRss'))
	def get_SourceDestCheck(self): # Boolean
		return self.get_query_params().get('SourceDestCheck')

	def set_SourceDestCheck(self, SourceDestCheck):  # Boolean
		self.add_query_param('SourceDestCheck', SourceDestCheck)
	def get_NetworkInterfaceName(self): # String
		return self.get_query_params().get('NetworkInterfaceName')

	def set_NetworkInterfaceName(self, NetworkInterfaceName):  # String
		self.add_query_param('NetworkInterfaceName', NetworkInterfaceName)
	def get_TxQueueSize(self): # Integer
		return self.get_query_params().get('TxQueueSize')

	def set_TxQueueSize(self, TxQueueSize):  # Integer
		self.add_query_param('TxQueueSize', TxQueueSize)
	def get_DeleteOnRelease(self): # Boolean
		return self.get_query_params().get('DeleteOnRelease')

	def set_DeleteOnRelease(self, DeleteOnRelease):  # Boolean
		self.add_query_param('DeleteOnRelease', DeleteOnRelease)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_RxQueueSize(self): # Integer
		return self.get_query_params().get('RxQueueSize')

	def set_RxQueueSize(self, RxQueueSize):  # Integer
		self.add_query_param('RxQueueSize', RxQueueSize)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ConnectionTrackingConfiguration(self): # Struct
		return self.get_query_params().get('ConnectionTrackingConfiguration')

	def set_ConnectionTrackingConfiguration(self, ConnectionTrackingConfiguration):  # Struct
		if ConnectionTrackingConfiguration.get('TcpEstablishedTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.TcpEstablishedTimeout', ConnectionTrackingConfiguration.get('TcpEstablishedTimeout'))
		if ConnectionTrackingConfiguration.get('TcpClosedAndTimeWaitTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.TcpClosedAndTimeWaitTimeout', ConnectionTrackingConfiguration.get('TcpClosedAndTimeWaitTimeout'))
		if ConnectionTrackingConfiguration.get('UdpTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.UdpTimeout', ConnectionTrackingConfiguration.get('UdpTimeout'))
	def get_NetworkInterfaceId(self): # String
		return self.get_query_params().get('NetworkInterfaceId')

	def set_NetworkInterfaceId(self, NetworkInterfaceId):  # String
		self.add_query_param('NetworkInterfaceId', NetworkInterfaceId)
