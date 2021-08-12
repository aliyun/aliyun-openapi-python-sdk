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

class QueryRingDetailListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'QueryRingDetailList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FromPhoneNumList(self): # String
		return self.get_body_params().get('FromPhoneNumList')

	def set_FromPhoneNumList(self, FromPhoneNumList):  # String
		self.add_body_params('FromPhoneNumList', FromPhoneNumList)
	def get_CallOutStatus(self): # String
		return self.get_body_params().get('CallOutStatus')

	def set_CallOutStatus(self, CallOutStatus):  # String
		self.add_body_params('CallOutStatus', CallOutStatus)
	def get_StartDate(self): # Long
		return self.get_body_params().get('StartDate')

	def set_StartDate(self, StartDate):  # Long
		self.add_body_params('StartDate', StartDate)
	def get_EndDate(self): # Long
		return self.get_body_params().get('EndDate')

	def set_EndDate(self, EndDate):  # Long
		self.add_body_params('EndDate', EndDate)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_PageNo(self): # Integer
		return self.get_body_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_body_params('PageNo', PageNo)
	def get_Extra(self): # String
		return self.get_body_params().get('Extra')

	def set_Extra(self, Extra):  # String
		self.add_body_params('Extra', Extra)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_ToPhoneNumList(self): # String
		return self.get_body_params().get('ToPhoneNumList')

	def set_ToPhoneNumList(self, ToPhoneNumList):  # String
		self.add_body_params('ToPhoneNumList', ToPhoneNumList)
