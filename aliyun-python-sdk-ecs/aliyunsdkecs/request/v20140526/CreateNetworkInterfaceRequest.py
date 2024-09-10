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

class CreateNetworkInterfaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateNetworkInterface','ecs')
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
	def get_Ipv4Prefixs(self): # RepeatList
		return self.get_query_params().get('Ipv4Prefix')

	def set_Ipv4Prefixs(self, Ipv4Prefix):  # RepeatList
		for depth1 in range(len(Ipv4Prefix)):
			self.add_query_param('Ipv4Prefix.' + str(depth1 + 1), Ipv4Prefix[depth1])
	def get_NetworkInterfaceTrafficConfig(self): # Struct
		return self.get_query_params().get('NetworkInterfaceTrafficConfig')

	def set_NetworkInterfaceTrafficConfig(self, NetworkInterfaceTrafficConfig):  # Struct
		if NetworkInterfaceTrafficConfig.get('QueueNumber') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.QueueNumber', NetworkInterfaceTrafficConfig.get('QueueNumber'))
		if NetworkInterfaceTrafficConfig.get('NetworkInterfaceTrafficMode') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.NetworkInterfaceTrafficMode', NetworkInterfaceTrafficConfig.get('NetworkInterfaceTrafficMode'))
		if NetworkInterfaceTrafficConfig.get('QueuePairNumber') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.QueuePairNumber', NetworkInterfaceTrafficConfig.get('QueuePairNumber'))
		if NetworkInterfaceTrafficConfig.get('TxQueueSize') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.TxQueueSize', NetworkInterfaceTrafficConfig.get('TxQueueSize'))
		if NetworkInterfaceTrafficConfig.get('RxQueueSize') is not None:
			self.add_query_param('NetworkInterfaceTrafficConfig.RxQueueSize', NetworkInterfaceTrafficConfig.get('RxQueueSize'))
	def get_SecondaryPrivateIpAddressCount(self): # Integer
		return self.get_query_params().get('SecondaryPrivateIpAddressCount')

	def set_SecondaryPrivateIpAddressCount(self, SecondaryPrivateIpAddressCount):  # Integer
		self.add_query_param('SecondaryPrivateIpAddressCount', SecondaryPrivateIpAddressCount)
	def get_BusinessType(self): # String
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self, BusinessType):  # String
		self.add_query_param('BusinessType', BusinessType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_EnhancedNetwork(self): # Struct
		return self.get_query_params().get('EnhancedNetwork')

	def set_EnhancedNetwork(self, EnhancedNetwork):  # Struct
		if EnhancedNetwork.get('EnableSriov') is not None:
			self.add_query_param('EnhancedNetwork.EnableSriov', EnhancedNetwork.get('EnableSriov'))
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_NetworkInterfaceName(self): # String
		return self.get_query_params().get('NetworkInterfaceName')

	def set_NetworkInterfaceName(self, NetworkInterfaceName):  # String
		self.add_query_param('NetworkInterfaceName', NetworkInterfaceName)
	def get_Visible(self): # Boolean
		return self.get_query_params().get('Visible')

	def set_Visible(self, Visible):  # Boolean
		self.add_query_param('Visible', Visible)
	def get_Ipv6AddressCount(self): # Integer
		return self.get_query_params().get('Ipv6AddressCount')

	def set_Ipv6AddressCount(self, Ipv6AddressCount):  # Integer
		self.add_query_param('Ipv6AddressCount', Ipv6AddressCount)
	def get_RxQueueSize(self): # Integer
		return self.get_query_params().get('RxQueueSize')

	def set_RxQueueSize(self, RxQueueSize):  # Integer
		self.add_query_param('RxQueueSize', RxQueueSize)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_PrivateIpAddresss(self): # RepeatList
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddresss(self, PrivateIpAddress):  # RepeatList
		for depth1 in range(len(PrivateIpAddress)):
			self.add_query_param('PrivateIpAddress.' + str(depth1 + 1), PrivateIpAddress[depth1])
	def get_Ipv6Addresss(self): # RepeatList
		return self.get_query_params().get('Ipv6Address')

	def set_Ipv6Addresss(self, Ipv6Address):  # RepeatList
		for depth1 in range(len(Ipv6Address)):
			self.add_query_param('Ipv6Address.' + str(depth1 + 1), Ipv6Address[depth1])
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Ipv6Prefixs(self): # RepeatList
		return self.get_query_params().get('Ipv6Prefix')

	def set_Ipv6Prefixs(self, Ipv6Prefix):  # RepeatList
		for depth1 in range(len(Ipv6Prefix)):
			self.add_query_param('Ipv6Prefix.' + str(depth1 + 1), Ipv6Prefix[depth1])
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Ipv6PrefixCount(self): # Integer
		return self.get_query_params().get('Ipv6PrefixCount')

	def set_Ipv6PrefixCount(self, Ipv6PrefixCount):  # Integer
		self.add_query_param('Ipv6PrefixCount', Ipv6PrefixCount)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
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
	def get_QueuePairNumber(self): # Integer
		return self.get_query_params().get('QueuePairNumber')

	def set_QueuePairNumber(self, QueuePairNumber):  # Integer
		self.add_query_param('QueuePairNumber', QueuePairNumber)
	def get_SecurityGroupIdss(self): # RepeatList
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIds):  # RepeatList
		for depth1 in range(len(SecurityGroupIds)):
			self.add_query_param('SecurityGroupIds.' + str(depth1 + 1), SecurityGroupIds[depth1])
	def get_NetworkInterfaceTrafficMode(self): # String
		return self.get_query_params().get('NetworkInterfaceTrafficMode')

	def set_NetworkInterfaceTrafficMode(self, NetworkInterfaceTrafficMode):  # String
		self.add_query_param('NetworkInterfaceTrafficMode', NetworkInterfaceTrafficMode)
	def get_Ipv4PrefixCount(self): # Integer
		return self.get_query_params().get('Ipv4PrefixCount')

	def set_Ipv4PrefixCount(self, Ipv4PrefixCount):  # Integer
		self.add_query_param('Ipv4PrefixCount', Ipv4PrefixCount)
	def get_ConnectionTrackingConfiguration(self): # Struct
		return self.get_query_params().get('ConnectionTrackingConfiguration')

	def set_ConnectionTrackingConfiguration(self, ConnectionTrackingConfiguration):  # Struct
		if ConnectionTrackingConfiguration.get('TcpEstablishedTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.TcpEstablishedTimeout', ConnectionTrackingConfiguration.get('TcpEstablishedTimeout'))
		if ConnectionTrackingConfiguration.get('TcpClosedAndTimeWaitTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.TcpClosedAndTimeWaitTimeout', ConnectionTrackingConfiguration.get('TcpClosedAndTimeWaitTimeout'))
		if ConnectionTrackingConfiguration.get('UdpTimeout') is not None:
			self.add_query_param('ConnectionTrackingConfiguration.UdpTimeout', ConnectionTrackingConfiguration.get('UdpTimeout'))
	def get_PrimaryIpAddress(self): # String
		return self.get_query_params().get('PrimaryIpAddress')

	def set_PrimaryIpAddress(self, PrimaryIpAddress):  # String
		self.add_query_param('PrimaryIpAddress', PrimaryIpAddress)
