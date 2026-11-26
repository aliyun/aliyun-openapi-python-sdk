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

class CreateStreamingJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateStreamingJob','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TryRun(self): # Boolean
		return self.get_query_params().get('TryRun')

	def set_TryRun(self, TryRun):  # Boolean
		self.add_query_param('TryRun', TryRun)
	def get_JobDescription(self): # String
		return self.get_query_params().get('JobDescription')

	def set_JobDescription(self, JobDescription):  # String
		self.add_query_param('JobDescription', JobDescription)
	def get_DestSchema(self): # String
		return self.get_query_params().get('DestSchema')

	def set_DestSchema(self, DestSchema):  # String
		self.add_query_param('DestSchema', DestSchema)
	def get_DestColumns(self): # Array
		return self.get_query_params().get('DestColumns')

	def set_DestColumns(self, DestColumns):  # Array
		self.add_query_param("DestColumns", json.dumps(DestColumns))
	def get_UpdateColumns(self): # Array
		return self.get_query_params().get('UpdateColumns')

	def set_UpdateColumns(self, UpdateColumns):  # Array
		self.add_query_param("UpdateColumns", json.dumps(UpdateColumns))
	def get_Consistency(self): # String
		return self.get_query_params().get('Consistency')

	def set_Consistency(self, Consistency):  # String
		self.add_query_param('Consistency', Consistency)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_DestDatabase(self): # String
		return self.get_query_params().get('DestDatabase')

	def set_DestDatabase(self, DestDatabase):  # String
		self.add_query_param('DestDatabase', DestDatabase)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_JobName(self): # String
		return self.get_query_params().get('JobName')

	def set_JobName(self, JobName):  # String
		self.add_query_param('JobName', JobName)
	def get_SrcColumns(self): # Array
		return self.get_query_params().get('SrcColumns')

	def set_SrcColumns(self, SrcColumns):  # Array
		self.add_query_param("SrcColumns", json.dumps(SrcColumns))
	def get_JobConfig(self): # String
		return self.get_query_params().get('JobConfig')

	def set_JobConfig(self, JobConfig):  # String
		self.add_query_param('JobConfig', JobConfig)
	def get_MatchColumns(self): # Array
		return self.get_query_params().get('MatchColumns')

	def set_MatchColumns(self, MatchColumns):  # Array
		self.add_query_param("MatchColumns", json.dumps(MatchColumns))
	def get_DestTable(self): # String
		return self.get_query_params().get('DestTable')

	def set_DestTable(self, DestTable):  # String
		self.add_query_param('DestTable', DestTable)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_FallbackOffset(self): # String
		return self.get_query_params().get('FallbackOffset')

	def set_FallbackOffset(self, FallbackOffset):  # String
		self.add_query_param('FallbackOffset', FallbackOffset)
	def get_DataSourceId(self): # String
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceId(self, DataSourceId):  # String
		self.add_query_param('DataSourceId', DataSourceId)
	def get_WriteMode(self): # String
		return self.get_query_params().get('WriteMode')

	def set_WriteMode(self, WriteMode):  # String
		self.add_query_param('WriteMode', WriteMode)
	def get_ErrorLimitCount(self): # Long
		return self.get_query_params().get('ErrorLimitCount')

	def set_ErrorLimitCount(self, ErrorLimitCount):  # Long
		self.add_query_param('ErrorLimitCount', ErrorLimitCount)
	def get_Account(self): # String
		return self.get_query_params().get('Account')

	def set_Account(self, Account):  # String
		self.add_query_param('Account', Account)
