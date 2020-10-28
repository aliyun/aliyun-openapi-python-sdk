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
from aliyunsdkdrds.endpoint import endpoint_data

class CreateDrdsDBRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'CreateDrdsDB','Drds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Encode(self):
		return self.get_query_params().get('Encode')

	def set_Encode(self,Encode):
		self.add_query_param('Encode',Encode)

	def get_RdsInstances(self):
		return self.get_query_params().get('RdsInstance')

	def set_RdsInstances(self, RdsInstances):
		for depth1 in range(len(RdsInstances)):
			if RdsInstances[depth1] is not None:
				self.add_query_param('RdsInstance.' + str(depth1 + 1) , RdsInstances[depth1])

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_RdsSuperAccounts(self):
		return self.get_query_params().get('RdsSuperAccount')

	def set_RdsSuperAccounts(self, RdsSuperAccounts):
		for depth1 in range(len(RdsSuperAccounts)):
			if RdsSuperAccounts[depth1].get('Password') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.Password', RdsSuperAccounts[depth1].get('Password'))
			if RdsSuperAccounts[depth1].get('AccountName') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.AccountName', RdsSuperAccounts[depth1].get('AccountName'))
			if RdsSuperAccounts[depth1].get('DbInstanceId') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.DbInstanceId', RdsSuperAccounts[depth1].get('DbInstanceId'))

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_DbInstanceIsCreating(self):
		return self.get_query_params().get('DbInstanceIsCreating')

	def set_DbInstanceIsCreating(self,DbInstanceIsCreating):
		self.add_query_param('DbInstanceIsCreating',DbInstanceIsCreating)

	def get_InstDbNames(self):
		return self.get_query_params().get('InstDbName')

	def set_InstDbNames(self, InstDbNames):
		for depth1 in range(len(InstDbNames)):
			if InstDbNames[depth1].get('ShardDbName') is not None:
				for depth2 in range(len(InstDbNames[depth1].get('ShardDbName'))):
					if InstDbNames[depth1].get('ShardDbName')[depth2] is not None:
						self.add_query_param('InstDbName.' + str(depth1 + 1) + '.ShardDbName.' + str(depth2 + 1) , InstDbNames[depth1].get('ShardDbName')[depth2])
			if InstDbNames[depth1].get('DbInstanceId') is not None:
				self.add_query_param('InstDbName.' + str(depth1 + 1) + '.DbInstanceId', InstDbNames[depth1].get('DbInstanceId'))

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_DbInstType(self):
		return self.get_query_params().get('DbInstType')

	def set_DbInstType(self,DbInstType):
		self.add_query_param('DbInstType',DbInstType)