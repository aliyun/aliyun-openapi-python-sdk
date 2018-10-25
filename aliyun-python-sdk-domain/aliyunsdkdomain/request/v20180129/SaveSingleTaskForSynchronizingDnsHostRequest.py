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
class SaveSingleTaskForSynchronizingDnsHostRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveSingleTaskForSynchronizingDnsHost')

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)