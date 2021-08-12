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

class GetOuterCallCenterDataListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'GetOuterCallCenterDataList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueryEndTime(self): # String
		return self.get_body_params().get('QueryEndTime')

	def set_QueryEndTime(self, QueryEndTime):  # String
		self.add_body_params('QueryEndTime', QueryEndTime)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_ToPhoneNum(self): # String
		return self.get_body_params().get('ToPhoneNum')

	def set_ToPhoneNum(self, ToPhoneNum):  # String
		self.add_body_params('ToPhoneNum', ToPhoneNum)
	def get_QueryStartTime(self): # String
		return self.get_body_params().get('QueryStartTime')

	def set_QueryStartTime(self, QueryStartTime):  # String
		self.add_body_params('QueryStartTime', QueryStartTime)
	def get_BizId(self): # String
		return self.get_body_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_body_params('BizId', BizId)
	def get_SessionId(self): # String
		return self.get_body_params().get('SessionId')

	def set_SessionId(self, SessionId):  # String
		self.add_body_params('SessionId', SessionId)
	def get_FromPhoneNum(self): # String
		return self.get_body_params().get('FromPhoneNum')

	def set_FromPhoneNum(self, FromPhoneNum):  # String
		self.add_body_params('FromPhoneNum', FromPhoneNum)
