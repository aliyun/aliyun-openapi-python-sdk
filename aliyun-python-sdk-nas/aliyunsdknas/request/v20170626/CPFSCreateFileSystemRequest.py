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
class CPFSCreateFileSystemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CPFSCreateFileSystem','nas')

	def get_FsSpec(self):
		return self.get_query_params().get('FsSpec')

	def set_FsSpec(self,FsSpec):
		self.add_query_param('FsSpec',FsSpec)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_NetworkType(self):
		return self.get_query_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_query_param('NetworkType',NetworkType)

	def get_FsDesc(self):
		return self.get_query_params().get('FsDesc')

	def set_FsDesc(self,FsDesc):
		self.add_query_param('FsDesc',FsDesc)

	def get_Capacity(self):
		return self.get_query_params().get('Capacity')

	def set_Capacity(self,Capacity):
		self.add_query_param('Capacity',Capacity)