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
class DescribeHanaMetadataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeHanaMetadata','hbr')
		self.set_protocol_type('https')

	def get_EndSnapshotId(self):
		return self.get_query_params().get('EndSnapshotId')

	def set_EndSnapshotId(self,EndSnapshotId):
		self.add_query_param('EndSnapshotId',EndSnapshotId)

	def get_ClientId(self):
		return self.get_query_params().get('ClientId')

	def set_ClientId(self,ClientId):
		self.add_query_param('ClientId',ClientId)

	def get_EndPaths(self):
		return self.get_query_params().get('EndPaths')

	def set_EndPaths(self,EndPaths):
		self.add_query_param('EndPaths',EndPaths)

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_EndTags(self):
		return self.get_query_params().get('EndTags')

	def set_EndTags(self,EndTags):
		self.add_query_param('EndTags',EndTags)

	def get_StartTags(self):
		return self.get_query_params().get('StartTags')

	def set_StartTags(self,StartTags):
		self.add_query_param('StartTags',StartTags)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_StartPaths(self):
		return self.get_query_params().get('StartPaths')

	def set_StartPaths(self,StartPaths):
		self.add_query_param('StartPaths',StartPaths)

	def get_Token(self):
		return self.get_query_params().get('Token')

	def set_Token(self,Token):
		self.add_query_param('Token',Token)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)

	def get_StartSnapshotId(self):
		return self.get_query_params().get('StartSnapshotId')

	def set_StartSnapshotId(self,StartSnapshotId):
		self.add_query_param('StartSnapshotId',StartSnapshotId)