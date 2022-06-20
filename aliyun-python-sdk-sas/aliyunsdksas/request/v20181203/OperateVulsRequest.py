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
from aliyunsdksas.endpoint import endpoint_data

class OperateVulsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'OperateVuls')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_VulNamess(self): # RepeatList
		return self.get_query_params().get('VulNames')

	def set_VulNamess(self, VulNames):  # RepeatList
		for depth1 in range(len(VulNames)):
			self.add_query_param('VulNames.' + str(depth1 + 1), VulNames[depth1])
	def get_OperateType(self): # String
		return self.get_query_params().get('OperateType')

	def set_OperateType(self, OperateType):  # String
		self.add_query_param('OperateType', OperateType)
	def get_Uuidss(self): # RepeatList
		return self.get_query_params().get('Uuids')

	def set_Uuidss(self, Uuids):  # RepeatList
		for depth1 in range(len(Uuids)):
			self.add_query_param('Uuids.' + str(depth1 + 1), Uuids[depth1])
