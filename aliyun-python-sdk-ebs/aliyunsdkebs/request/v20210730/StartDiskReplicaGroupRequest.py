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

class StartDiskReplicaGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ebs', '2021-07-30', 'StartDiskReplicaGroup','ebs')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ReplicaGroupId(self): # String
		return self.get_query_params().get('ReplicaGroupId')

	def set_ReplicaGroupId(self, ReplicaGroupId):  # String
		self.add_query_param('ReplicaGroupId', ReplicaGroupId)
	def get_OneShot(self): # Boolean
		return self.get_query_params().get('OneShot')

	def set_OneShot(self, OneShot):  # Boolean
		self.add_query_param('OneShot', OneShot)
