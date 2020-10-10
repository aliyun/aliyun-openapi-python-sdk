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
		RpcRequest.__init__(self, 'clickhouse', '2019-11-11', 'OperateLogHub','clickhouse')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_DeliverName(self):
		return self.get_query_params().get('DeliverName')

	def set_DeliverName(self,DeliverName):
		self.add_query_param('DeliverName',DeliverName)

	def get_DeliverTime(self):
		return self.get_query_params().get('DeliverTime')

	def set_DeliverTime(self,DeliverTime):
		self.add_query_param('DeliverTime',DeliverTime)

	def get_DomainUrl(self):
		return self.get_query_params().get('DomainUrl')

	def set_DomainUrl(self,DomainUrl):
		self.add_query_param('DomainUrl',DomainUrl)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_AccessKey(self):
		return self.get_query_params().get('AccessKey')

	def set_AccessKey(self,AccessKey):
		self.add_query_param('AccessKey',AccessKey)

	def get_Create(self):
		return self.get_query_params().get('Create')

	def set_Create(self,Create):
		self.add_query_param('Create',Create)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_ProjectName(self):
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_query_param('ProjectName',ProjectName)

	def get_SchemaName(self):
		return self.get_query_params().get('SchemaName')

	def set_SchemaName(self,SchemaName):
		self.add_query_param('SchemaName',SchemaName)

	def get_AccessSecret(self):
		return self.get_query_params().get('AccessSecret')

	def set_AccessSecret(self,AccessSecret):
		self.add_query_param('AccessSecret',AccessSecret)

	def get_LogStoreName(self):
		return self.get_query_params().get('LogStoreName')

	def set_LogStoreName(self,LogStoreName):
		self.add_query_param('LogStoreName',LogStoreName)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DBClusterId(self):
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self,DBClusterId):
		self.add_query_param('DBClusterId',DBClusterId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_FilterDirty(self):
		return self.get_query_params().get('FilterDirty')

	def set_FilterDirty(self,FilterDirty):
		self.add_query_param('FilterDirty',FilterDirty)

	def get_LogHubStoress(self):
		return self.get_query_params().get('LogHubStores')

	def set_LogHubStoress(self, LogHubStoress):
		for depth1 in range(len(LogHubStoress)):
			if LogHubStoress[depth1].get('LogKey') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.LogKey', LogHubStoress[depth1].get('LogKey'))
			if LogHubStoress[depth1].get('FieldKey') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.FieldKey', LogHubStoress[depth1].get('FieldKey'))
			if LogHubStoress[depth1].get('Type') is not None:
				self.add_query_param('LogHubStores.' + str(depth1 + 1) + '.Type', LogHubStoress[depth1].get('Type'))

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)