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

from aliyunsdkcore.request import RoaRequest
class GetUserSourceRepoRefListRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'cr', '2016-06-07', 'GetUserSourceRepoRefList','cr')
		self.set_uri_pattern('/users/sourceAccount/[SourceAccountId]/repos/[SourceRepoNamespace]/[SourceRepoName]/refs')
		self.set_method('GET')

	def get_SourceAccountId(self):
		return self.get_path_params().get('SourceAccountId')

	def set_SourceAccountId(self,SourceAccountId):
		self.add_path_param('SourceAccountId',SourceAccountId)

	def get_SourceRepoName(self):
		return self.get_path_params().get('SourceRepoName')

	def set_SourceRepoName(self,SourceRepoName):
		self.add_path_param('SourceRepoName',SourceRepoName)

	def get_SourceRepoNamespace(self):
		return self.get_path_params().get('SourceRepoNamespace')

	def set_SourceRepoNamespace(self,SourceRepoNamespace):
		self.add_path_param('SourceRepoNamespace',SourceRepoNamespace)