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

class OperateVulsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'OperateVuls')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Reason(self): # String
		return self.get_query_params().get('Reason')

	def set_Reason(self, Reason):  # String
		self.add_query_param('Reason', Reason)
	def get_Precondition(self): # Integer
		return self.get_query_params().get('Precondition')

	def set_Precondition(self, Precondition):  # Integer
		self.add_query_param('Precondition', Precondition)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_VulNames(self): # RepeatList
		return self.get_query_params().get('VulName')

	def set_VulNames(self, VulName):  # RepeatList
		for depth1 in range(len(VulName)):
			self.add_query_param('VulName.' + str(depth1 + 1), VulName[depth1])
	def get_OperateType(self): # String
		return self.get_query_params().get('OperateType')

	def set_OperateType(self, OperateType):  # String
		self.add_query_param('OperateType', OperateType)
	def get_DesktopIds(self): # RepeatList
		return self.get_query_params().get('DesktopId')

	def set_DesktopIds(self, DesktopId):  # RepeatList
		for depth1 in range(len(DesktopId)):
			self.add_query_param('DesktopId.' + str(depth1 + 1), DesktopId[depth1])
