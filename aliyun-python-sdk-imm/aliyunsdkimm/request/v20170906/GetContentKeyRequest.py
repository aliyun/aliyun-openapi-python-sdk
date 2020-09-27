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

class GetContentKeyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'GetContentKey','imm')
		self.set_method('POST')

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_VersionId(self):
		return self.get_query_params().get('VersionId')

	def set_VersionId(self,VersionId):
		self.add_query_param('VersionId',VersionId)

	def get_DRMServerId(self):
		return self.get_query_params().get('DRMServerId')

	def set_DRMServerId(self,DRMServerId):
		self.add_query_param('DRMServerId',DRMServerId)

	def get_KeyIds(self):
		return self.get_query_params().get('KeyIds')

	def set_KeyIds(self,KeyIds):
		self.add_query_param('KeyIds',KeyIds)