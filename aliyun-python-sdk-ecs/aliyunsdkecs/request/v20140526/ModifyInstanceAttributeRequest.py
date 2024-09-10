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

class ModifyInstanceAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyInstanceAttribute','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Recyclable(self): # Boolean
		return self.get_query_params().get('Recyclable')

	def set_Recyclable(self, Recyclable):  # Boolean
		self.add_query_param('Recyclable', Recyclable)
	def get_NetworkInterfaceQueueNumber(self): # Integer
		return self.get_query_params().get('NetworkInterfaceQueueNumber')

	def set_NetworkInterfaceQueueNumber(self, NetworkInterfaceQueueNumber):  # Integer
		self.add_query_param('NetworkInterfaceQueueNumber', NetworkInterfaceQueueNumber)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_PrivateDnsNameOptions(self): # Struct
		return self.get_query_params().get('PrivateDnsNameOptions')

	def set_PrivateDnsNameOptions(self, PrivateDnsNameOptions):  # Struct
		if PrivateDnsNameOptions.get('HostnameType') is not None:
			self.add_query_param('PrivateDnsNameOptions.HostnameType', PrivateDnsNameOptions.get('HostnameType'))
		if PrivateDnsNameOptions.get('EnableInstanceIdDnsARecord') is not None:
			self.add_query_param('PrivateDnsNameOptions.EnableInstanceIdDnsARecord', PrivateDnsNameOptions.get('EnableInstanceIdDnsARecord'))
		if PrivateDnsNameOptions.get('EnableInstanceIdDnsAAAARecord') is not None:
			self.add_query_param('PrivateDnsNameOptions.EnableInstanceIdDnsAAAARecord', PrivateDnsNameOptions.get('EnableInstanceIdDnsAAAARecord'))
		if PrivateDnsNameOptions.get('EnableIpDnsARecord') is not None:
			self.add_query_param('PrivateDnsNameOptions.EnableIpDnsARecord', PrivateDnsNameOptions.get('EnableIpDnsARecord'))
		if PrivateDnsNameOptions.get('EnableIpDnsPtrRecord') is not None:
			self.add_query_param('PrivateDnsNameOptions.EnableIpDnsPtrRecord', PrivateDnsNameOptions.get('EnableIpDnsPtrRecord'))
	def get_CpuOptionsTopologyType(self): # String
		return self.get_query_params().get('CpuOptions.TopologyType')

	def set_CpuOptionsTopologyType(self, CpuOptionsTopologyType):  # String
		self.add_query_param('CpuOptions.TopologyType', CpuOptionsTopologyType)
	def get_EnableJumboFrame(self): # Boolean
		return self.get_query_params().get('EnableJumboFrame')

	def set_EnableJumboFrame(self, EnableJumboFrame):  # Boolean
		self.add_query_param('EnableJumboFrame', EnableJumboFrame)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_CreditSpecification(self): # String
		return self.get_query_params().get('CreditSpecification')

	def set_CreditSpecification(self, CreditSpecification):  # String
		self.add_query_param('CreditSpecification', CreditSpecification)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SecurityGroupIdss(self): # RepeatList
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIdss(self, SecurityGroupIds):  # RepeatList
		for depth1 in range(len(SecurityGroupIds)):
			self.add_query_param('SecurityGroupIds.' + str(depth1 + 1), SecurityGroupIds[depth1])
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_RemoteConnectionOptions(self): # Struct
		return self.get_query_params().get('RemoteConnectionOptions')

	def set_RemoteConnectionOptions(self, RemoteConnectionOptions):  # Struct
		if RemoteConnectionOptions.get('Password') is not None:
			self.add_query_param('RemoteConnectionOptions.Password', RemoteConnectionOptions.get('Password'))
		if RemoteConnectionOptions.get('Type') is not None:
			self.add_query_param('RemoteConnectionOptions.Type', RemoteConnectionOptions.get('Type'))
