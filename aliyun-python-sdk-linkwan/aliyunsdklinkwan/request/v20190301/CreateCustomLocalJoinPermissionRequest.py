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
from aliyunsdklinkwan.endpoint import endpoint_data

class CreateCustomLocalJoinPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'CreateCustomLocalJoinPermission','linkwan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClassMode(self):
		return self.get_query_params().get('ClassMode')

	def set_ClassMode(self,ClassMode):
		self.add_query_param('ClassMode',ClassMode)

	def get_FreqBandPlanGroupId(self):
		return self.get_query_params().get('FreqBandPlanGroupId')

	def set_FreqBandPlanGroupId(self,FreqBandPlanGroupId):
		self.add_query_param('FreqBandPlanGroupId',FreqBandPlanGroupId)

	def get_JoinEui(self):
		return self.get_query_params().get('JoinEui')

	def set_JoinEui(self,JoinEui):
		self.add_query_param('JoinEui',JoinEui)

	def get_JoinPermissionName(self):
		return self.get_query_params().get('JoinPermissionName')

	def set_JoinPermissionName(self,JoinPermissionName):
		self.add_query_param('JoinPermissionName',JoinPermissionName)