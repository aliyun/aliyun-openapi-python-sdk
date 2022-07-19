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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class ListShiftPersonnelsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListShiftPersonnels')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ShiftPersonUID(self): # String
		return self.get_body_params().get('ShiftPersonUID')

	def set_ShiftPersonUID(self, ShiftPersonUID):  # String
		self.add_body_params('ShiftPersonUID', ShiftPersonUID)
	def get_UserType(self): # String
		return self.get_body_params().get('UserType')

	def set_UserType(self, UserType):  # String
		self.add_body_params('UserType', UserType)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_body_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_body_params('BeginTime', BeginTime)
	def get_ShiftScheduleIdentifier(self): # String
		return self.get_body_params().get('ShiftScheduleIdentifier')

	def set_ShiftScheduleIdentifier(self, ShiftScheduleIdentifier):  # String
		self.add_body_params('ShiftScheduleIdentifier', ShiftScheduleIdentifier)
