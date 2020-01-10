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

class DescribeMigrationJobDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribeMigrationJobDetail','dts')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_MigrationModeDataInitialization(self):
		return self.get_query_params().get('MigrationMode.DataInitialization')

	def set_MigrationModeDataInitialization(self,MigrationModeDataInitialization):
		self.add_query_param('MigrationMode.DataInitialization',MigrationModeDataInitialization)

	def get_MigrationJobId(self):
		return self.get_query_params().get('MigrationJobId')

	def set_MigrationJobId(self,MigrationJobId):
		self.add_query_param('MigrationJobId',MigrationJobId)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MigrationModeStructureInitialization(self):
		return self.get_query_params().get('MigrationMode.StructureInitialization')

	def set_MigrationModeStructureInitialization(self,MigrationModeStructureInitialization):
		self.add_query_param('MigrationMode.StructureInitialization',MigrationModeStructureInitialization)

	def get_AccountId(self):
		return self.get_query_params().get('AccountId')

	def set_AccountId(self,AccountId):
		self.add_query_param('AccountId',AccountId)

	def get_MigrationModeDataSynchronization(self):
		return self.get_query_params().get('MigrationMode.DataSynchronization')

	def set_MigrationModeDataSynchronization(self,MigrationModeDataSynchronization):
		self.add_query_param('MigrationMode.DataSynchronization',MigrationModeDataSynchronization)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)