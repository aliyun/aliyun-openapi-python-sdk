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
from aliyunsdkcloudauth.endpoint import endpoint_data

class DescribeDeviceInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cloudauth', '2019-03-07', 'DescribeDeviceInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserDeviceId(self): # String
		return self.get_query_params().get('UserDeviceId')

	def set_UserDeviceId(self, UserDeviceId):  # String
		self.add_query_param('UserDeviceId', UserDeviceId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_ExpiredStartDay(self): # String
		return self.get_query_params().get('ExpiredStartDay')

	def set_ExpiredStartDay(self, ExpiredStartDay):  # String
		self.add_query_param('ExpiredStartDay', ExpiredStartDay)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_DeviceId(self): # String
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self, DeviceId):  # String
		self.add_query_param('DeviceId', DeviceId)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_ExpiredEndDay(self): # String
		return self.get_query_params().get('ExpiredEndDay')

	def set_ExpiredEndDay(self, ExpiredEndDay):  # String
		self.add_query_param('ExpiredEndDay', ExpiredEndDay)
