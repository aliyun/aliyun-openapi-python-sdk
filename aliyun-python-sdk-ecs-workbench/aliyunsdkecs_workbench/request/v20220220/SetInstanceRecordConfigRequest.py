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

class SetInstanceRecordConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecs-workbench', '2022-02-20', 'SetInstanceRecordConfig','ecs-workbench')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Enabled(self): # Boolean
		return self.get_body_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Boolean
		self.add_body_params('Enabled', Enabled)
	def get_RecordStorageTarget(self): # String
		return self.get_body_params().get('RecordStorageTarget')

	def set_RecordStorageTarget(self, RecordStorageTarget):  # String
		self.add_body_params('RecordStorageTarget', RecordStorageTarget)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_ExpirationDays(self): # Integer
		return self.get_body_params().get('ExpirationDays')

	def set_ExpirationDays(self, ExpirationDays):  # Integer
		self.add_body_params('ExpirationDays', ExpirationDays)
