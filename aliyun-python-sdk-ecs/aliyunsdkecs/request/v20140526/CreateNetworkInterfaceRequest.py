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


	def get_QueueNumber(self):
		return self.get_query_params().get('QueueNumber')

	def set_QueueNumber(self,QueueNumber):
		self.add_query_param('QueueNumber',QueueNumber)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SecondaryPrivateIpAddressCount(self):
		return self.get_query_params().get('SecondaryPrivateIpAddressCount')

	def set_SecondaryPrivateIpAddressCount(self,SecondaryPrivateIpAddressCount):
		self.add_query_param('SecondaryPrivateIpAddressCount',SecondaryPrivateIpAddressCount)

	def get_BusinessType(self):
		return self.get_query_params().get('BusinessType')

	def set_BusinessType(self,BusinessType):
		self.add_query_param('BusinessType',BusinessType)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))

	def get_NetworkInterfaceName(self):
		return self.get_query_params().get('NetworkInterfaceName')

	def set_NetworkInterfaceName(self,NetworkInterfaceName):
		self.add_query_param('NetworkInterfaceName',NetworkInterfaceName)

	def get_Visible(self):
		return self.get_query_params().get('Visible')

	def set_Visible(self,Visible):
		self.add_query_param('Visible',Visible)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityGroupIdss(self):
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIdss):
		for depth1 in range(len(SecurityGroupIdss)):
			if SecurityGroupIdss[depth1] is not None:
				self.add_query_param('SecurityGroupIds.' + str(depth1 + 1) , SecurityGroupIdss[depth1])

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_PrivateIpAddresss(self):
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddresss(self, PrivateIpAddresss):
		for depth1 in range(len(PrivateIpAddresss)):
			if PrivateIpAddresss[depth1] is not None:
				self.add_query_param('PrivateIpAddress.' + str(depth1 + 1) , PrivateIpAddresss[depth1])

	def get_PrimaryIpAddress(self):
		return self.get_query_params().get('PrimaryIpAddress')

	def set_PrimaryIpAddress(self,PrimaryIpAddress):
		self.add_query_param('PrimaryIpAddress',PrimaryIpAddress)