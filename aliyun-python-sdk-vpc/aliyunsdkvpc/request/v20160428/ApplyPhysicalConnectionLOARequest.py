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

class ApplyPhysicalConnectionLOARequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ApplyPhysicalConnectionLOA','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_LineType(self): # String
		return self.get_query_params().get('LineType')

	def set_LineType(self, LineType):  # String
		self.add_query_param('LineType', LineType)
	def get_Si(self): # String
		return self.get_query_params().get('Si')

	def set_Si(self, Si):  # String
		self.add_query_param('Si', Si)
	def get_PeerLocation(self): # String
		return self.get_query_params().get('PeerLocation')

	def set_PeerLocation(self, PeerLocation):  # String
		self.add_query_param('PeerLocation', PeerLocation)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_Bandwidth(self): # Integer
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self, Bandwidth):  # Integer
		self.add_query_param('Bandwidth', Bandwidth)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_ConstructionTime(self): # String
		return self.get_query_params().get('ConstructionTime')

	def set_ConstructionTime(self, ConstructionTime):  # String
		self.add_query_param('ConstructionTime', ConstructionTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_CompanyName(self): # String
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self, CompanyName):  # String
		self.add_query_param('CompanyName', CompanyName)
	def get_PMInfos(self): # RepeatList
		return self.get_query_params().get('PMInfo')

	def set_PMInfos(self, PMInfo):  # RepeatList
		for depth1 in range(len(PMInfo)):
			if PMInfo[depth1].get('PMCertificateNo') is not None:
				self.add_query_param('PMInfo.' + str(depth1 + 1) + '.PMCertificateNo', PMInfo[depth1].get('PMCertificateNo'))
			if PMInfo[depth1].get('PMName') is not None:
				self.add_query_param('PMInfo.' + str(depth1 + 1) + '.PMName', PMInfo[depth1].get('PMName'))
			if PMInfo[depth1].get('PMCertificateType') is not None:
				self.add_query_param('PMInfo.' + str(depth1 + 1) + '.PMCertificateType', PMInfo[depth1].get('PMCertificateType'))
			if PMInfo[depth1].get('PMGender') is not None:
				self.add_query_param('PMInfo.' + str(depth1 + 1) + '.PMGender', PMInfo[depth1].get('PMGender'))
			if PMInfo[depth1].get('PMContactInfo') is not None:
				self.add_query_param('PMInfo.' + str(depth1 + 1) + '.PMContactInfo', PMInfo[depth1].get('PMContactInfo'))
