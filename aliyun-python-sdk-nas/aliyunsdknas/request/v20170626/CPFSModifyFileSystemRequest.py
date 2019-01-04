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
class CPFSModifyFileSystemRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'NAS', '2017-06-26', 'CPFSModifyFileSystem','nas')

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_FsId(self):
		return self.get_query_params().get('FsId')

	def set_FsId(self,FsId):
		self.add_query_param('FsId',FsId)

	def get_FsDesc(self):
		return self.get_query_params().get('FsDesc')

	def set_FsDesc(self,FsDesc):
		self.add_query_param('FsDesc',FsDesc)

	def get_Capacity(self):
		return self.get_query_params().get('Capacity')

	def set_Capacity(self,Capacity):
		self.add_query_param('Capacity',Capacity)