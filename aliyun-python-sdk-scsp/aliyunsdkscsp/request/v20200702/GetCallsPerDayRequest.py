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
from aliyunsdkscsp.endpoint import endpoint_data

class GetCallsPerDayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'GetCallsPerDay')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_DataIdStart(self): # String
		return self.get_query_params().get('DataIdStart')

	def set_DataIdStart(self, DataIdStart):  # String
		self.add_query_param('DataIdStart', DataIdStart)
	def get_DataIdEnd(self): # String
		return self.get_query_params().get('DataIdEnd')

	def set_DataIdEnd(self, DataIdEnd):  # String
		self.add_query_param('DataIdEnd', DataIdEnd)
	def get_DataId(self): # String
		return self.get_query_params().get('DataId')

	def set_DataId(self, DataId):  # String
		self.add_query_param('DataId', DataId)
	def get_HourId(self): # String
		return self.get_query_params().get('HourId')

	def set_HourId(self, HourId):  # String
		self.add_query_param('HourId', HourId)
	def get_MinuteId(self): # String
		return self.get_query_params().get('MinuteId')

	def set_MinuteId(self, MinuteId):  # String
		self.add_query_param('MinuteId', MinuteId)
	def get_PhoneNumbers(self): # String
		return self.get_query_params().get('PhoneNumbers')

	def set_PhoneNumbers(self, PhoneNumbers):  # String
		self.add_query_param('PhoneNumbers', PhoneNumbers)
	def get_HavePhoneNumbers(self): # String
		return self.get_query_params().get('HavePhoneNumbers')

	def set_HavePhoneNumbers(self, HavePhoneNumbers):  # String
		self.add_query_param('HavePhoneNumbers', HavePhoneNumbers)
	def get_PageNo(self): # Long
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Long
		self.add_query_param('PageNo', PageNo)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
