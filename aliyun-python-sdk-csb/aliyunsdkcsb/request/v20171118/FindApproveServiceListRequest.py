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
class FindApproveServiceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CSB', '2017-11-18', 'FindApproveServiceList','CSB')
		self.set_protocol_type('https');

	def get_projectName(self):
		return self.get_query_params().get('projectName')

	def set_projectName(self,projectName):
		self.add_query_param('projectName',projectName)

	def get_approveLevel(self):
		return self.get_query_params().get('approveLevel')

	def set_approveLevel(self,approveLevel):
		self.add_query_param('approveLevel',approveLevel)

	def get_showDelService(self):
		return self.get_query_params().get('showDelService')

	def set_showDelService(self,showDelService):
		self.add_query_param('showDelService',showDelService)

	def get_csbId(self):
		return self.get_query_params().get('csbId')

	def set_csbId(self,csbId):
		self.add_query_param('csbId',csbId)

	def get_alias(self):
		return self.get_query_params().get('alias')

	def set_alias(self,alias):
		self.add_query_param('alias',alias)

	def get_serviceName(self):
		return self.get_query_params().get('serviceName')

	def set_serviceName(self,serviceName):
		self.add_query_param('serviceName',serviceName)