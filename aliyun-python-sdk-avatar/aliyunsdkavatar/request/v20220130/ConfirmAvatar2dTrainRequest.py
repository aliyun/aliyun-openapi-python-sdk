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

class ConfirmAvatar2dTrainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'avatar', '2022-01-30', 'ConfirmAvatar2dTrain')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Confirm(self): # String
		return self.get_query_params().get('Confirm')

	def set_Confirm(self, Confirm):  # String
		self.add_query_param('Confirm', Confirm)
	def get_Code(self): # String
		return self.get_query_params().get('Code')

	def set_Code(self, Code):  # String
		self.add_query_param('Code', Code)
	def get_TenantId(self): # Long
		return self.get_query_params().get('TenantId')

	def set_TenantId(self, TenantId):  # Long
		self.add_query_param('TenantId', TenantId)
