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
from aliyunsdkfaas.endpoint import endpoint_data

class UpdateCreateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'faas', '2017-08-24', 'UpdateCreateTask')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_FpgaImageObjectName(self):
		return self.get_query_params().get('FpgaImageObjectName')

	def set_FpgaImageObjectName(self,FpgaImageObjectName):
		self.add_query_param('FpgaImageObjectName',FpgaImageObjectName)

	def get_FpgaImageUUID(self):
		return self.get_query_params().get('FpgaImageUUID')

	def set_FpgaImageUUID(self,FpgaImageUUID):
		self.add_query_param('FpgaImageUUID',FpgaImageUUID)

	def get_callerUid(self):
		return self.get_query_params().get('callerUid')

	def set_callerUid(self,callerUid):
		self.add_query_param('callerUid',callerUid)