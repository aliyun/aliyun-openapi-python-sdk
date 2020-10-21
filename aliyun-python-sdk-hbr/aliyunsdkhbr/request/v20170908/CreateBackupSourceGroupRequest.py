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
from aliyunsdkhbr.endpoint import endpoint_data

class CreateBackupSourceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupSourceGroup','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BackupSources(self):
		return self.get_query_params().get('BackupSource')

	def set_BackupSources(self, BackupSources):
		for depth1 in range(len(BackupSources)):
			if BackupSources[depth1].get('BackupSourceId') is not None:
				self.add_query_param('BackupSource.' + str(depth1 + 1) + '.BackupSourceId', BackupSources[depth1].get('BackupSourceId'))
			if BackupSources[depth1].get('DatabaseName') is not None:
				self.add_query_param('BackupSource.' + str(depth1 + 1) + '.DatabaseName', BackupSources[depth1].get('DatabaseName'))
			if BackupSources[depth1].get('Description') is not None:
				self.add_query_param('BackupSource.' + str(depth1 + 1) + '.Description', BackupSources[depth1].get('Description'))
			if BackupSources[depth1].get('ClusterId') is not None:
				self.add_query_param('BackupSource.' + str(depth1 + 1) + '.ClusterId', BackupSources[depth1].get('ClusterId'))

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ImplicitlyCreateBackupSources(self):
		return self.get_query_params().get('ImplicitlyCreateBackupSources')

	def set_ImplicitlyCreateBackupSources(self,ImplicitlyCreateBackupSources):
		self.add_query_param('ImplicitlyCreateBackupSources',ImplicitlyCreateBackupSources)

	def get_BackupSourceIds(self):
		return self.get_query_params().get('BackupSourceId')

	def set_BackupSourceIds(self, BackupSourceIds):
		for depth1 in range(len(BackupSourceIds)):
			if BackupSourceIds[depth1] is not None:
				self.add_query_param('BackupSourceId.' + str(depth1 + 1) , BackupSourceIds[depth1])

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_BackupSourceGroupId(self):
		return self.get_query_params().get('BackupSourceGroupId')

	def set_BackupSourceGroupId(self,BackupSourceGroupId):
		self.add_query_param('BackupSourceGroupId',BackupSourceGroupId)