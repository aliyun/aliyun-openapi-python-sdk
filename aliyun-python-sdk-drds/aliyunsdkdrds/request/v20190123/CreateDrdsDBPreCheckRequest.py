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

class CreateDrdsDBPreCheckRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'CreateDrdsDBPreCheck','drds')

	def get_Encode(self):
		return self.get_query_params().get('Encode')

	def set_Encode(self,Encode):
		self.add_query_param('Encode',Encode)

	def get_InstDbNames(self):
		return self.get_query_params().get('InstDbNames')

	def set_InstDbNames(self,InstDbNames):
		for i in range(len(InstDbNames)):	
			for j in range(len(InstDbNames[i].get('ShardDbNames'))):
				if InstDbNames[i].get('ShardDbNames')[j] is not None:
					self.add_query_param('InstDbName.' + str(i + 1) + '.ShardDbName.'+str(j + 1), InstDbNames[i].get('ShardDbNames')[j])
			if InstDbNames[i].get('DbInstanceId') is not None:
				self.add_query_param('InstDbName.' + str(i + 1) + '.DbInstanceId' , InstDbNames[i].get('DbInstanceId'))


	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_RdsSuperAccounts(self):
		return self.get_query_params().get('RdsSuperAccounts')

	def set_RdsSuperAccounts(self,RdsSuperAccounts):
		for i in range(len(RdsSuperAccounts)):	
			if RdsSuperAccounts[i].get('Password') is not None:
				self.add_query_param('RdsSuperAccount.' + str(i + 1) + '.Password' , RdsSuperAccounts[i].get('Password'))
			if RdsSuperAccounts[i].get('AccountName') is not None:
				self.add_query_param('RdsSuperAccount.' + str(i + 1) + '.AccountName' , RdsSuperAccounts[i].get('AccountName'))
			if RdsSuperAccounts[i].get('DbInstanceId') is not None:
				self.add_query_param('RdsSuperAccount.' + str(i + 1) + '.DbInstanceId' , RdsSuperAccounts[i].get('DbInstanceId'))


	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_RdsInstances(self):
		return self.get_query_params().get('RdsInstances')

	def set_RdsInstances(self,RdsInstances):
		for i in range(len(RdsInstances)):	
			if RdsInstances[i] is not None:
				self.add_query_param('RdsInstance.' + str(i + 1) , RdsInstances[i]);

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_DbInstType(self):
		return self.get_query_params().get('DbInstType')

	def set_DbInstType(self,DbInstType):
		self.add_query_param('DbInstType',DbInstType)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_DbInstanceIsCreating(self):
		return self.get_query_params().get('DbInstanceIsCreating')

	def set_DbInstanceIsCreating(self,DbInstanceIsCreating):
		self.add_query_param('DbInstanceIsCreating',DbInstanceIsCreating)