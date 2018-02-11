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
class UpdateLiveSnapshotDetectPornConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveSnapshotDetectPornConfig','live')

	def get_OssBucket(self):
		return self.get_query_params().get('OssBucket')

	def set_OssBucket(self,OssBucket):
		self.add_query_param('OssBucket',OssBucket)

	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OssEndpoint(self):
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self,OssEndpoint):
		self.add_query_param('OssEndpoint',OssEndpoint)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_OssObject(self):
		return self.get_query_params().get('OssObject')

	def set_OssObject(self,OssObject):
		self.add_query_param('OssObject',OssObject)

	def get_Scenes(self):
		return self.get_query_params().get('Scenes')

	def set_Scenes(self,Scenes):
		for i in range(len(Scenes)):	
			if Scenes[i] is not None:
				self.add_query_param('Scene.' + str(i + 1) , Scenes[i]);