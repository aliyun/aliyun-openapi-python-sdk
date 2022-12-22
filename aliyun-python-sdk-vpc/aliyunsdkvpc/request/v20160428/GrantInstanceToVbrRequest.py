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
from aliyunsdkvpc.endpoint import endpoint_data

class GrantInstanceToVbrRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'GrantInstanceToVbr','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_VbrOwnerUid(self): # Long
		return self.get_query_params().get('VbrOwnerUid')

	def set_VbrOwnerUid(self, VbrOwnerUid):  # Long
		self.add_query_param('VbrOwnerUid', VbrOwnerUid)
	def get_VbrRegionNo(self): # String
		return self.get_query_params().get('VbrRegionNo')

	def set_VbrRegionNo(self, VbrRegionNo):  # String
		self.add_query_param('VbrRegionNo', VbrRegionNo)
	def get_VbrInstanceIds(self): # Array
		return self.get_query_params().get('VbrInstanceIds')

	def set_VbrInstanceIds(self, VbrInstanceIds):  # Array
		for index1, value1 in enumerate(VbrInstanceIds):
			self.add_query_param('VbrInstanceIds.' + str(index1 + 1), value1)
	def get_GrantType(self): # String
		return self.get_query_params().get('GrantType')

	def set_GrantType(self, GrantType):  # String
		self.add_query_param('GrantType', GrantType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
