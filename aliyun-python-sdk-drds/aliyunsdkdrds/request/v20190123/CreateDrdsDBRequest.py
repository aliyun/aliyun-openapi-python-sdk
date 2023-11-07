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
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'CreateDrdsDB','drds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Encode(self): # String
		return self.get_query_params().get('Encode')

	def set_Encode(self, Encode):  # String
		self.add_query_param('Encode', Encode)
	def get_RdsInstances(self): # RepeatList
		return self.get_query_params().get('RdsInstance')

	def set_RdsInstances(self, RdsInstance):  # RepeatList
		for depth1 in range(len(RdsInstance)):
			self.add_query_param('RdsInstance.' + str(depth1 + 1), RdsInstance[depth1])
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_RdsSuperAccounts(self): # RepeatList
		return self.get_query_params().get('RdsSuperAccount')

	def set_RdsSuperAccounts(self, RdsSuperAccount):  # RepeatList
		for depth1 in range(len(RdsSuperAccount)):
			if RdsSuperAccount[depth1].get('Password') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.Password', RdsSuperAccount[depth1].get('Password'))
			if RdsSuperAccount[depth1].get('AccountName') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.AccountName', RdsSuperAccount[depth1].get('AccountName'))
			if RdsSuperAccount[depth1].get('DbInstanceId') is not None:
				self.add_query_param('RdsSuperAccount.' + str(depth1 + 1) + '.DbInstanceId', RdsSuperAccount[depth1].get('DbInstanceId'))
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_DrdsInstanceId(self): # String
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self, DrdsInstanceId):  # String
		self.add_query_param('DrdsInstanceId', DrdsInstanceId)
	def get_DbInstanceIsCreating(self): # Boolean
		return self.get_query_params().get('DbInstanceIsCreating')

	def set_DbInstanceIsCreating(self, DbInstanceIsCreating):  # Boolean
		self.add_query_param('DbInstanceIsCreating', DbInstanceIsCreating)
	def get_InstDbNames(self): # RepeatList
		return self.get_query_params().get('InstDbName')

	def set_InstDbNames(self, InstDbName):  # RepeatList
		for depth1 in range(len(InstDbName)):
			if InstDbName[depth1].get('ShardDbName') is not None:
				for depth2 in range(len(InstDbName[depth1].get('ShardDbName'))):
					self.add_query_param('InstDbName.' + str(depth1 + 1) + '.ShardDbName.' + str(depth2 + 1), InstDbName[depth1].get('ShardDbName')[depth2])
			if InstDbName[depth1].get('DbInstanceId') is not None:
				self.add_query_param('InstDbName.' + str(depth1 + 1) + '.DbInstanceId', InstDbName[depth1].get('DbInstanceId'))
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
	def get_DbInstType(self): # String
		return self.get_query_params().get('DbInstType')

	def set_DbInstType(self, DbInstType):  # String
		self.add_query_param('DbInstType', DbInstType)
