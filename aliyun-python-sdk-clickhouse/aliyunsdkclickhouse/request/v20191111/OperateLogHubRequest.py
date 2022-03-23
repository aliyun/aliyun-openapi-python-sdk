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
from aliyunsdkclickhouse.endpoint import endpoint_data

class OperateLogHubRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'OperateLogHub')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_UseLorne(self): # Boolean
		return self.get_query_params().get('UseLorne')

	def set_UseLorne(self, UseLorne):  # Boolean
		self.add_query_param('UseLorne', UseLorne)
	def get_DeliverName(self): # String
		return self.get_query_params().get('DeliverName')

	def set_DeliverName(self, DeliverName):  # String
		self.add_query_param('DeliverName', DeliverName)
	def get_DeliverTime(self): # String
		return self.get_query_params().get('DeliverTime')

	def set_DeliverTime(self, DeliverTime):  # String
		self.add_query_param('DeliverTime', DeliverTime)
	def get_DomainUrl(self): # String
		return self.get_query_params().get('DomainUrl')

	def set_DomainUrl(self, DomainUrl):  # String
		self.add_query_param('DomainUrl', DomainUrl)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_AccessKey(self): # String
		return self.get_query_params().get('AccessKey')

	def set_AccessKey(self, AccessKey):  # String
		self.add_query_param('AccessKey', AccessKey)
	def get_Create(self): # Boolean
		return self.get_query_params().get('Create')

	def set_Create(self, Create):  # Boolean
		self.add_query_param('Create', Create)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_SchemaName(self): # String
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self, SchemaName):  # String
		self.add_query_param('SchemaName', SchemaName)
	def get_AccessSecret(self): # String
		return self.get_query_params().get('AccessSecret')

	def set_AccessSecret(self, AccessSecret):  # String
		self.add_query_param('AccessSecret', AccessSecret)
	def get_LogStoreName(self): # String
		return self.get_query_params().get('LogStoreName')

	def set_LogStoreName(self, LogStoreName):  # String
		self.add_query_param('LogStoreName', LogStoreName)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LogHubStoress(self): # RepeatList
		return self.get_query_params().get('LogHubStores')

	def set_LogHubStoress(self, LogHubStores):  # RepeatList
		for depth1 in range(len(LogHubStores)):
			if LogHubStores[depth1].get('LogKey') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.LogKey', LogHubStores[depth1].get('LogKey'))
			if LogHubStores[depth1].get('FieldKey') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.FieldKey', LogHubStores[depth1].get('FieldKey'))
			if LogHubStores[depth1].get('Type') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.Type', LogHubStores[depth1].get('Type'))
	def get_FilterDirtyData(self): # Boolean
		return self.get_query_params().get('FilterDirtyData')

	def set_FilterDirtyData(self, FilterDirtyData):  # Boolean
		self.add_query_param('FilterDirtyData', FilterDirtyData)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
