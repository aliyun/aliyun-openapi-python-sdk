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
from aliyunsdklive.endpoint import endpoint_data

class UpdateLiveAppSnapshotConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateLiveAppSnapshotConfig','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeInterval(self): # Integer
		return self.get_query_params().get('TimeInterval')

	def set_TimeInterval(self, TimeInterval):  # Integer
		self.add_query_param('TimeInterval', TimeInterval)
	def get_OssEndpoint(self): # String
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self, OssEndpoint):  # String
		self.add_query_param('OssEndpoint', OssEndpoint)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_OverwriteOssObject(self): # String
		return self.get_query_params().get('OverwriteOssObject')

	def set_OverwriteOssObject(self, OverwriteOssObject):  # String
		self.add_query_param('OverwriteOssObject', OverwriteOssObject)
	def get_OssBucket(self): # String
		return self.get_query_params().get('OssBucket')

	def set_OssBucket(self, OssBucket):  # String
		self.add_query_param('OssBucket', OssBucket)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_SequenceOssObject(self): # String
		return self.get_query_params().get('SequenceOssObject')

	def set_SequenceOssObject(self, SequenceOssObject):  # String
		self.add_query_param('SequenceOssObject', SequenceOssObject)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_Callback(self): # String
		return self.get_query_params().get('Callback')

	def set_Callback(self, Callback):  # String
		self.add_query_param('Callback', Callback)
