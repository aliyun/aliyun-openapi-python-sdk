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

class QueryInstanceNcdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'QueryInstanceNcd','eflo')
		self.set_method('POST')

	def get_InstanceId2(self): # String
		return self.get_body_params().get('InstanceId2')

	def set_InstanceId2(self, InstanceId2):  # String
		self.add_body_params('InstanceId2', InstanceId2)
	def get_InstanceId1(self): # String
		return self.get_body_params().get('InstanceId1')

	def set_InstanceId1(self, InstanceId1):  # String
		self.add_body_params('InstanceId1', InstanceId1)
	def get_InstanceType(self): # String
		return self.get_body_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_body_params('InstanceType', InstanceType)
