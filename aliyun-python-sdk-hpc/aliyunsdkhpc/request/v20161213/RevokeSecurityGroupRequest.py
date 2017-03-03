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
class RevokeSecurityGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HPC', '2016-12-13', 'RevokeSecurityGroup','hpc')
		self.set_method('POST')

	def get_TOKEN(self):
		return self.get_query_params().get('TOKEN')

	def set_TOKEN(self,TOKEN):
		self.add_query_param('TOKEN',TOKEN)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_NicType(self):
		return self.get_query_params().get('NicType')

	def set_NicType(self,NicType):
		self.add_query_param('NicType',NicType)