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
import json

class ExecuteStatementRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'ExecuteStatement','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SecretArn(self): # String
		return self.get_query_params().get('SecretArn')

	def set_SecretArn(self, SecretArn):  # String
		self.add_query_param('SecretArn', SecretArn)
	def get_RagWorkspaceCollection(self): # Struct
		return self.get_query_params().get('RagWorkspaceCollection')

	def set_RagWorkspaceCollection(self, RagWorkspaceCollection):  # Struct
		self.add_query_param("RagWorkspaceCollection", json.dumps(RagWorkspaceCollection))
	def get_Sql(self): # String
		return self.get_body_params().get('Sql')

	def set_Sql(self, Sql):  # String
		self.add_body_params('Sql', Sql)
	def get_Sqls(self): # Array
		return self.get_body_params().get('Sqls')

	def set_Sqls(self, Sqls):  # Array
		self.add_body_params("Sqls", json.dumps(Sqls))
	def get_Database(self): # String
		return self.get_query_params().get('Database')

	def set_Database(self, Database):  # String
		self.add_query_param('Database', Database)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_StatementName(self): # String
		return self.get_query_params().get('StatementName')

	def set_StatementName(self, StatementName):  # String
		self.add_query_param('StatementName', StatementName)
	def get_RunType(self): # String
		return self.get_query_params().get('RunType')

	def set_RunType(self, RunType):  # String
		self.add_query_param('RunType', RunType)
	def get_Parameters(self): # Array
		return self.get_body_params().get('Parameters')

	def set_Parameters(self, Parameters):  # Array
		self.add_body_params("Parameters", json.dumps(Parameters))
	def get_WorkspaceId(self): # String
		return self.get_query_params().get('WorkspaceId')

	def set_WorkspaceId(self, WorkspaceId):  # String
		self.add_query_param('WorkspaceId', WorkspaceId)
