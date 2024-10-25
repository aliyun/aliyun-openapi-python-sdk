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
from aliyunsdkvpc.endpoint import endpoint_data

class CreateHighReliablePhysicalConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateHighReliablePhysicalConnection','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PortType(self): # String
		return self.get_query_params().get('PortType')

	def set_PortType(self, PortType):  # String
		self.add_query_param('PortType', PortType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_HighReliableType(self): # String
		return self.get_query_params().get('HighReliableType')

	def set_HighReliableType(self, HighReliableType):  # String
		self.add_query_param('HighReliableType', HighReliableType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
	def get_DryRun(self): # String
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # String
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ApLists(self): # RepeatList
		return self.get_query_params().get('ApList')

	def set_ApLists(self, ApList):  # RepeatList
		for depth1 in range(len(ApList)):
			if ApList[depth1].get('Name') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.Name', ApList[depth1].get('Name'))
			if ApList[depth1].get('Description') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.Description', ApList[depth1].get('Description'))
			if ApList[depth1].get('RegionId') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.RegionId', ApList[depth1].get('RegionId'))
			if ApList[depth1].get('LineOperator') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.LineOperator', ApList[depth1].get('LineOperator'))
			if ApList[depth1].get('AccessPointId') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.AccessPointId', ApList[depth1].get('AccessPointId'))
			if ApList[depth1].get('PortNum') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.PortNum', ApList[depth1].get('PortNum'))
			if ApList[depth1].get('Type') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.Type', ApList[depth1].get('Type'))
			if ApList[depth1].get('Bandwidth') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.Bandwidth', ApList[depth1].get('Bandwidth'))
			if ApList[depth1].get('PeerLocation') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.PeerLocation', ApList[depth1].get('PeerLocation'))
			if ApList[depth1].get('CircuitCode') is not None:
				self.add_query_param('ApList.' + str(depth1 + 1) + '.CircuitCode', ApList[depth1].get('CircuitCode'))
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_DeviceAdvancedCapacitys(self): # RepeatList
		return self.get_query_params().get('DeviceAdvancedCapacity')

	def set_DeviceAdvancedCapacitys(self, DeviceAdvancedCapacity):  # RepeatList
		for depth1 in range(len(DeviceAdvancedCapacity)):
			self.add_query_param('DeviceAdvancedCapacity.' + str(depth1 + 1), DeviceAdvancedCapacity[depth1])
