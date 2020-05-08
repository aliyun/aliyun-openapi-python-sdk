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

class CreateInstanceAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'CreateInstanceAccount','drds')

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_DbPrivileges(self):
		return self.get_query_params().get('DbPrivileges')

	def set_DbPrivileges(self,DbPrivileges):
		for i in range(len(DbPrivileges)):	
			if DbPrivileges[i].get('DbName') is not None:
				self.add_query_param('DbPrivilege.' + str(i + 1) + '.DbName' , DbPrivileges[i].get('DbName'))
			if DbPrivileges[i].get('Privilege') is not None:
				self.add_query_param('DbPrivilege.' + str(i + 1) + '.Privilege' , DbPrivileges[i].get('Privilege'))
