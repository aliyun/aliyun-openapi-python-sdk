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
class ModifyJumpserverPasswordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HPC', '2016-12-13', 'ModifyJumpserverPassword','hpc')
		self.set_method('POST')

	def get_TOKEN(self):
		return self.get_query_params().get('TOKEN')

	def set_TOKEN(self,TOKEN):
		self.add_query_param('TOKEN',TOKEN)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_NewPassword(self):
		return self.get_query_params().get('NewPassword')

	def set_NewPassword(self,NewPassword):
		self.add_query_param('NewPassword',NewPassword)