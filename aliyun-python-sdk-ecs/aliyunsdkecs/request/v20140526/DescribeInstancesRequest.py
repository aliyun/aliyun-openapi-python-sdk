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

class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInstances','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InnerIpAddresses(self):
		return self.get_query_params().get('InnerIpAddresses')

	def set_InnerIpAddresses(self,InnerIpAddresses):
		self.add_query_param('InnerIpAddresses',InnerIpAddresses)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PrivateIpAddresses(self):
		return self.get_query_params().get('PrivateIpAddresses')

	def set_PrivateIpAddresses(self,PrivateIpAddresses):
		self.add_query_param('PrivateIpAddresses',PrivateIpAddresses)

	def get_HpcClusterId(self):
		return self.get_query_params().get('HpcClusterId')

	def set_HpcClusterId(self,HpcClusterId):
		self.add_query_param('HpcClusterId',HpcClusterId)

	def get_HttpPutResponseHopLimit(self):
		return self.get_query_params().get('HttpPutResponseHopLimit')

	def set_HttpPutResponseHopLimit(self,HttpPutResponseHopLimit):
		self.add_query_param('HttpPutResponseHopLimit',HttpPutResponseHopLimit)

	def get_Filter2Value(self):
		return self.get_query_params().get('Filter.2.Value')

	def set_Filter2Value(self,Filter2Value):
		self.add_query_param('Filter.2.Value',Filter2Value)

	def get_KeyPairName(self):
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self,KeyPairName):
		self.add_query_param('KeyPairName',KeyPairName)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_LockReason(self):
		return self.get_query_params().get('LockReason')

	def set_LockReason(self,LockReason):
		self.add_query_param('LockReason',LockReason)

	def get_Filter1Key(self):
		return self.get_query_params().get('Filter.1.Key')

	def set_Filter1Key(self,Filter1Key):
		self.add_query_param('Filter.1.Key',Filter1Key)

	def get_DeviceAvailable(self):
		return self.get_query_params().get('DeviceAvailable')

	def set_DeviceAvailable(self,DeviceAvailable):
		self.add_query_param('DeviceAvailable',DeviceAvailable)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_Filter3Value(self):
		return self.get_query_params().get('Filter.3.Value')

	def set_Filter3Value(self,Filter3Value):
		self.add_query_param('Filter.3.Value',Filter3Value)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_Filter1Value(self):
		return self.get_query_params().get('Filter.1.Value')

	def set_Filter1Value(self,Filter1Value):
		self.add_query_param('Filter.1.Value',Filter1Value)

	def get_NeedSaleCycle(self):
		return self.get_query_params().get('NeedSaleCycle')

	def set_NeedSaleCycle(self,NeedSaleCycle):
		self.add_query_param('NeedSaleCycle',NeedSaleCycle)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_AdditionalAttributess(self):
		return self.get_query_params().get('AdditionalAttributess')

	def set_AdditionalAttributess(self, AdditionalAttributess):
		for depth1 in range(len(AdditionalAttributess)):
			if AdditionalAttributess[depth1] is not None:
				self.add_query_param('AdditionalAttributes.' + str(depth1 + 1) , AdditionalAttributess[depth1])

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self,InstanceIds):
		self.add_query_param('InstanceIds',InstanceIds)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_InstanceNetworkType(self):
		return self.get_query_params().get('InstanceNetworkType')

	def set_InstanceNetworkType(self,InstanceNetworkType):
		self.add_query_param('InstanceNetworkType',InstanceNetworkType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_Filter4Value(self):
		return self.get_query_params().get('Filter.4.Value')

	def set_Filter4Value(self,Filter4Value):
		self.add_query_param('Filter.4.Value',Filter4Value)

	def get_IoOptimized(self):
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self,IoOptimized):
		self.add_query_param('IoOptimized',IoOptimized)

	def get_SecurityGroupId(self):
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self,SecurityGroupId):
		self.add_query_param('SecurityGroupId',SecurityGroupId)

	def get_Filter4Key(self):
		return self.get_query_params().get('Filter.4.Key')

	def set_Filter4Key(self,Filter4Key):
		self.add_query_param('Filter.4.Key',Filter4Key)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_RdmaIpAddresses(self):
		return self.get_query_params().get('RdmaIpAddresses')

	def set_RdmaIpAddresses(self,RdmaIpAddresses):
		self.add_query_param('RdmaIpAddresses',RdmaIpAddresses)

	def get_HttpEndpoint(self):
		return self.get_query_params().get('HttpEndpoint')

	def set_HttpEndpoint(self,HttpEndpoint):
		self.add_query_param('HttpEndpoint',HttpEndpoint)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PublicIpAddresses(self):
		return self.get_query_params().get('PublicIpAddresses')

	def set_PublicIpAddresses(self,PublicIpAddresses):
		self.add_query_param('PublicIpAddresses',PublicIpAddresses)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_InstanceTypeFamily(self):
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self,InstanceTypeFamily):
		self.add_query_param('InstanceTypeFamily',InstanceTypeFamily)

	def get_Filter2Key(self):
		return self.get_query_params().get('Filter.2.Key')

	def set_Filter2Key(self,Filter2Key):
		self.add_query_param('Filter.2.Key',Filter2Key)

	def get_EipAddresses(self):
		return self.get_query_params().get('EipAddresses')

	def set_EipAddresses(self,EipAddresses):
		self.add_query_param('EipAddresses',EipAddresses)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_HttpTokens(self):
		return self.get_query_params().get('HttpTokens')

	def set_HttpTokens(self,HttpTokens):
		self.add_query_param('HttpTokens',HttpTokens)

	def get_Filter3Key(self):
		return self.get_query_params().get('Filter.3.Key')

	def set_Filter3Key(self,Filter3Key):
		self.add_query_param('Filter.3.Key',Filter3Key)