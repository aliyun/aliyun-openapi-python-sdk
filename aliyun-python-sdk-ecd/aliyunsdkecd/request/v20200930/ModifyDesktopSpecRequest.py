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

class ModifyDesktopSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ecd', '2020-09-30', 'ModifyDesktopSpec')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_UserDiskPerformanceLevel(self): # String
		return self.get_query_params().get('UserDiskPerformanceLevel')

	def set_UserDiskPerformanceLevel(self, UserDiskPerformanceLevel):  # String
		self.add_query_param('UserDiskPerformanceLevel', UserDiskPerformanceLevel)
	def get_PromotionId(self): # String
		return self.get_query_params().get('PromotionId')

	def set_PromotionId(self, PromotionId):  # String
		self.add_query_param('PromotionId', PromotionId)
	def get_UserDiskSizeGib(self): # Integer
		return self.get_query_params().get('UserDiskSizeGib')

	def set_UserDiskSizeGib(self, UserDiskSizeGib):  # Integer
		self.add_query_param('UserDiskSizeGib', UserDiskSizeGib)
	def get_DesktopId(self): # String
		return self.get_query_params().get('DesktopId')

	def set_DesktopId(self, DesktopId):  # String
		self.add_query_param('DesktopId', DesktopId)
	def get_DesktopType(self): # String
		return self.get_query_params().get('DesktopType')

	def set_DesktopType(self, DesktopType):  # String
		self.add_query_param('DesktopType', DesktopType)
	def get_RootDiskSizeGib(self): # Integer
		return self.get_query_params().get('RootDiskSizeGib')

	def set_RootDiskSizeGib(self, RootDiskSizeGib):  # Integer
		self.add_query_param('RootDiskSizeGib', RootDiskSizeGib)
