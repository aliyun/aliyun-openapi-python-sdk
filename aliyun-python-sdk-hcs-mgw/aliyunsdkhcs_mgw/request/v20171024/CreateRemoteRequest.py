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

class CreateRemoteRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateRemote')
		self.set_method('POST')

	def get_RemoteName(self):
		return self.get_query_params().get('RemoteName')

	def set_RemoteName(self,RemoteName):
		self.add_query_param('RemoteName',RemoteName)

	def get_MountPoint(self):
		return self.get_query_params().get('MountPoint')

	def set_MountPoint(self,MountPoint):
		self.add_query_param('MountPoint',MountPoint)

	def get_Path(self):
		return self.get_query_params().get('Path')

	def set_Path(self,Path):
		self.add_query_param('Path',Path)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_RemoteHost(self):
		return self.get_query_params().get('RemoteHost')

	def set_RemoteHost(self,RemoteHost):
		self.add_query_param('RemoteHost',RemoteHost)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_MountType(self):
		return self.get_query_params().get('MountType')

	def set_MountType(self,MountType):
		self.add_query_param('MountType',MountType)

	def get_RemoteType(self):
		return self.get_query_params().get('RemoteType')

	def set_RemoteType(self,RemoteType):
		self.add_query_param('RemoteType',RemoteType)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)