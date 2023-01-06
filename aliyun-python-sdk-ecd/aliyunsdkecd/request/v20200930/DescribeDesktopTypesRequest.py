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

class DescribeDesktopTypesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'DescribeDesktopTypes')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppliedScope(self): # String
		return self.get_query_params().get('AppliedScope')

	def set_AppliedScope(self, AppliedScope):  # String
		self.add_query_param('AppliedScope', AppliedScope)
	def get_MemorySize(self): # Integer
		return self.get_query_params().get('MemorySize')

	def set_MemorySize(self, MemorySize):  # Integer
		self.add_query_param('MemorySize', MemorySize)
	def get_GpuCount(self): # Float
		return self.get_query_params().get('GpuCount')

	def set_GpuCount(self, GpuCount):  # Float
		self.add_query_param('GpuCount', GpuCount)
	def get_InstanceTypeFamily(self): # String
		return self.get_query_params().get('InstanceTypeFamily')

	def set_InstanceTypeFamily(self, InstanceTypeFamily):  # String
		self.add_query_param('InstanceTypeFamily', InstanceTypeFamily)
	def get_DesktopTypeId(self): # String
		return self.get_query_params().get('DesktopTypeId')

	def set_DesktopTypeId(self, DesktopTypeId):  # String
		self.add_query_param('DesktopTypeId', DesktopTypeId)
	def get_DesktopIdForModify(self): # String
		return self.get_query_params().get('DesktopIdForModify')

	def set_DesktopIdForModify(self, DesktopIdForModify):  # String
		self.add_query_param('DesktopIdForModify', DesktopIdForModify)
	def get_CpuCount(self): # Integer
		return self.get_query_params().get('CpuCount')

	def set_CpuCount(self, CpuCount):  # Integer
		self.add_query_param('CpuCount', CpuCount)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
