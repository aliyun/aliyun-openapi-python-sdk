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
class CreateBackupSourceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreateBackupSourceGroup','hbr')

	def get_BackupSources(self):
		return self.get_query_params().get('BackupSources')

	def set_BackupSources(self,BackupSources):
		for i in range(len(BackupSources)):	
			if BackupSources[i].get('BackupSourceId') is not None:
				self.add_query_param('BackupSource.' + str(i + 1) + '.BackupSourceId' , BackupSources[i].get('BackupSourceId'))
			if BackupSources[i].get('DatabaseName') is not None:
				self.add_query_param('BackupSource.' + str(i + 1) + '.DatabaseName' , BackupSources[i].get('DatabaseName'))
			if BackupSources[i].get('Description') is not None:
				self.add_query_param('BackupSource.' + str(i + 1) + '.Description' , BackupSources[i].get('Description'))
			if BackupSources[i].get('ClusterId') is not None:
				self.add_query_param('BackupSource.' + str(i + 1) + '.ClusterId' , BackupSources[i].get('ClusterId'))


	def get_ImplicitlyCreateBackupSources(self):
		return self.get_query_params().get('ImplicitlyCreateBackupSources')

	def set_ImplicitlyCreateBackupSources(self,ImplicitlyCreateBackupSources):
		self.add_query_param('ImplicitlyCreateBackupSources',ImplicitlyCreateBackupSources)

	def get_BackupSourceIds(self):
		return self.get_query_params().get('BackupSourceIds')

	def set_BackupSourceIds(self,BackupSourceIds):
		for i in range(len(BackupSourceIds)):	
			if BackupSourceIds[i] is not None:
				self.add_query_param('BackupSourceId.' + str(i + 1) , BackupSourceIds[i]);

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_SourceType(self):
		return self.get_query_params().get('SourceType')

	def set_SourceType(self,SourceType):
		self.add_query_param('SourceType',SourceType)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_BackupSourceGroupId(self):
		return self.get_query_params().get('BackupSourceGroupId')

	def set_BackupSourceGroupId(self,BackupSourceGroupId):
		self.add_query_param('BackupSourceGroupId',BackupSourceGroupId)