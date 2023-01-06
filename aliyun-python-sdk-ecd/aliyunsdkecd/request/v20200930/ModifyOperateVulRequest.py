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
from aliyunsdkecd.endpoint import endpoint_data

class ModifyOperateVulRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyOperateVul')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Reason(self): # String
		return self.get_query_params().get('Reason')

	def set_Reason(self, Reason):  # String
		self.add_query_param('Reason', Reason)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_VulInfos(self): # RepeatList
		return self.get_query_params().get('VulInfo')

	def set_VulInfos(self, VulInfo):  # RepeatList
		for depth1 in range(len(VulInfo)):
			if VulInfo[depth1].get('Name') is not None:
				self.add_query_param('VulInfo.' + str(depth1 + 1) + '.Name', VulInfo[depth1].get('Name'))
			if VulInfo[depth1].get('DesktopId') is not None:
				self.add_query_param('VulInfo.' + str(depth1 + 1) + '.DesktopId', VulInfo[depth1].get('DesktopId'))
			if VulInfo[depth1].get('Tag') is not None:
				self.add_query_param('VulInfo.' + str(depth1 + 1) + '.Tag', VulInfo[depth1].get('Tag'))
	def get_OperateType(self): # String
		return self.get_query_params().get('OperateType')

	def set_OperateType(self, OperateType):  # String
		self.add_query_param('OperateType', OperateType)
