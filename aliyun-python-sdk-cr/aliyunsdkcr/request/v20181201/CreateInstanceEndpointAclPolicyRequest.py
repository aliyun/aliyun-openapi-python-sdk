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

class CreateInstanceEndpointAclPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cr', '2018-12-01', 'CreateInstanceEndpointAclPolicy','acr')
		self.set_method('POST')

	def get_Entry(self):
		return self.get_query_params().get('Entry')

	def set_Entry(self,Entry):
		self.add_query_param('Entry',Entry)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_EndpointType(self):
		return self.get_query_params().get('EndpointType')

	def set_EndpointType(self,EndpointType):
		self.add_query_param('EndpointType',EndpointType)

	def get_ModuleName(self):
		return self.get_query_params().get('ModuleName')

	def set_ModuleName(self,ModuleName):
		self.add_query_param('ModuleName',ModuleName)

	def get_Comment(self):
		return self.get_query_params().get('Comment')

	def set_Comment(self,Comment):
		self.add_query_param('Comment',Comment)