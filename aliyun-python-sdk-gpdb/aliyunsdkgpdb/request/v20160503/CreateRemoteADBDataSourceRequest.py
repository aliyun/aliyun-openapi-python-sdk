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
from aliyunsdkgpdb.endpoint import endpoint_data

class CreateRemoteADBDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateRemoteADBDataSource','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ManagerUserPassword(self): # String
		return self.get_query_params().get('ManagerUserPassword')

	def set_ManagerUserPassword(self, ManagerUserPassword):  # String
		self.add_query_param('ManagerUserPassword', ManagerUserPassword)
	def get_UserPassword(self): # String
		return self.get_query_params().get('UserPassword')

	def set_UserPassword(self, UserPassword):  # String
		self.add_query_param('UserPassword', UserPassword)
	def get_LocalDBInstanceId(self): # String
		return self.get_query_params().get('LocalDBInstanceId')

	def set_LocalDBInstanceId(self, LocalDBInstanceId):  # String
		self.add_query_param('LocalDBInstanceId', LocalDBInstanceId)
	def get_RemoteDBInstanceId(self): # String
		return self.get_query_params().get('RemoteDBInstanceId')

	def set_RemoteDBInstanceId(self, RemoteDBInstanceId):  # String
		self.add_query_param('RemoteDBInstanceId', RemoteDBInstanceId)
	def get_DataSourceName(self): # String
		return self.get_query_params().get('DataSourceName')

	def set_DataSourceName(self, DataSourceName):  # String
		self.add_query_param('DataSourceName', DataSourceName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ManagerUserName(self): # String
		return self.get_query_params().get('ManagerUserName')

	def set_ManagerUserName(self, ManagerUserName):  # String
		self.add_query_param('ManagerUserName', ManagerUserName)
	def get_RemoteDatabase(self): # String
		return self.get_query_params().get('RemoteDatabase')

	def set_RemoteDatabase(self, RemoteDatabase):  # String
		self.add_query_param('RemoteDatabase', RemoteDatabase)
	def get_LocalDatabase(self): # String
		return self.get_query_params().get('LocalDatabase')

	def set_LocalDatabase(self, LocalDatabase):  # String
		self.add_query_param('LocalDatabase', LocalDatabase)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
