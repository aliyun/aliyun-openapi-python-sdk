# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateDBInstanceforFirstPayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'CreateDBInstanceforFirstPay')

	def get_uid(self):
		return self.get_query_params().get('uid')

	def set_uid(self,uid):
		self.add_query_param('uid',uid)

	def get_bid(self):
		return self.get_query_params().get('bid')

	def set_bid(self,bid):
		self.add_query_param('bid',bid)

	def get_uidLoginEmail(self):
		return self.get_query_params().get('uidLoginEmail')

	def set_uidLoginEmail(self,uidLoginEmail):
		self.add_query_param('uidLoginEmail',uidLoginEmail)

	def get_bidLoginEmail(self):
		return self.get_query_params().get('bidLoginEmail')

	def set_bidLoginEmail(self,bidLoginEmail):
		self.add_query_param('bidLoginEmail',bidLoginEmail)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)

	def get_EngineVersion(self):
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self,EngineVersion):
		self.add_query_param('EngineVersion',EngineVersion)

	def get_DBInstanceClass(self):
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self,DBInstanceClass):
		self.add_query_param('DBInstanceClass',DBInstanceClass)

	def get_DBInstanceStorage(self):
		return self.get_query_params().get('DBInstanceStorage')

	def set_DBInstanceStorage(self,DBInstanceStorage):
		self.add_query_param('DBInstanceStorage',DBInstanceStorage)

	def get_DBInstanceNetType(self):
		return self.get_query_params().get('DBInstanceNetType')

	def set_DBInstanceNetType(self,DBInstanceNetType):
		self.add_query_param('DBInstanceNetType',DBInstanceNetType)

	def get_CharacterSetName(self):
		return self.get_query_params().get('CharacterSetName')

	def set_CharacterSetName(self,CharacterSetName):
		self.add_query_param('CharacterSetName',CharacterSetName)

	def get_DBInstanceRemarks(self):
		return self.get_query_params().get('DBInstanceRemarks')

	def set_DBInstanceRemarks(self,DBInstanceRemarks):
		self.add_query_param('DBInstanceRemarks',DBInstanceRemarks)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)