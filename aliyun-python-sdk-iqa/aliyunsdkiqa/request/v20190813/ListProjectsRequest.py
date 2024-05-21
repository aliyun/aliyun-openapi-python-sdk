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

class ListProjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'iqa', '2019-08-13', 'ListProjects','iqa')

	def get_FilterParam(self):
		return self.get_query_params().get('FilterParam')

	def set_FilterParam(self,FilterParam):
		self.add_query_param('FilterParam',FilterParam)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ProjectType(self):
		return self.get_query_params().get('ProjectType')

	def set_ProjectType(self,ProjectType):
		self.add_query_param('ProjectType',ProjectType)