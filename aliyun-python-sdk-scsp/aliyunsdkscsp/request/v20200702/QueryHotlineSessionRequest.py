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

class QueryHotlineSessionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'QueryHotlineSession')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_ServicerId(self): # String
		return self.get_query_params().get('ServicerId')

	def set_ServicerId(self, ServicerId):  # String
		self.add_query_param('ServicerId', ServicerId)
	def get_Params(self): # String
		return self.get_query_params().get('Params')

	def set_Params(self, Params):  # String
		self.add_query_param('Params', Params)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_Acid(self): # String
		return self.get_query_params().get('Acid')

	def set_Acid(self, Acid):  # String
		self.add_query_param('Acid', Acid)
	def get_CallingNumber(self): # String
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumber(self, CallingNumber):  # String
		self.add_query_param('CallingNumber', CallingNumber)
	def get_QueryEndTime(self): # Long
		return self.get_query_params().get('QueryEndTime')

	def set_QueryEndTime(self, QueryEndTime):  # Long
		self.add_query_param('QueryEndTime', QueryEndTime)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_CalledNumber(self): # String
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self, CalledNumber):  # String
		self.add_query_param('CalledNumber', CalledNumber)
	def get_RequestId(self): # String
		return self.get_query_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_query_param('RequestId', RequestId)
	def get_PageNo(self): # Integer
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_query_param('PageNo', PageNo)
	def get_QueryStartTime(self): # Long
		return self.get_query_params().get('QueryStartTime')

	def set_QueryStartTime(self, QueryStartTime):  # Long
		self.add_query_param('QueryStartTime', QueryStartTime)
	def get_ServicerName(self): # String
		return self.get_query_params().get('ServicerName')

	def set_ServicerName(self, ServicerName):  # String
		self.add_query_param('ServicerName', ServicerName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_CallResult(self): # String
		return self.get_query_params().get('CallResult')

	def set_CallResult(self, CallResult):  # String
		self.add_query_param('CallResult', CallResult)
	def get_CallType(self): # Integer
		return self.get_query_params().get('CallType')

	def set_CallType(self, CallType):  # Integer
		self.add_query_param('CallType', CallType)
	def get_MemberName(self): # String
		return self.get_query_params().get('MemberName')

	def set_MemberName(self, MemberName):  # String
		self.add_query_param('MemberName', MemberName)
	def get_MemberId(self): # String
		return self.get_query_params().get('MemberId')

	def set_MemberId(self, MemberId):  # String
		self.add_query_param('MemberId', MemberId)
