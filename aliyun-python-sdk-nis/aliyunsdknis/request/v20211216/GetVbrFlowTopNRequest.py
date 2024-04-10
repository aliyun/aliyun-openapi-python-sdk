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
import json

class GetVbrFlowTopNRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nis', '2021-12-16', 'GetVbrFlowTopN','networkana')
		self.set_method('POST')

	def get_OtherPort(self): # String
		return self.get_query_params().get('OtherPort')

	def set_OtherPort(self, OtherPort):  # String
		self.add_query_param('OtherPort', OtherPort)
	def get_TopN(self): # Integer
		return self.get_query_params().get('TopN')

	def set_TopN(self, TopN):  # Integer
		self.add_query_param('TopN', TopN)
	def get_CloudPort(self): # String
		return self.get_query_params().get('CloudPort')

	def set_CloudPort(self, CloudPort):  # String
		self.add_query_param('CloudPort', CloudPort)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_OtherIp(self): # String
		return self.get_query_params().get('OtherIp')

	def set_OtherIp(self, OtherIp):  # String
		self.add_query_param('OtherIp', OtherIp)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_UseMultiAccount(self): # Boolean
		return self.get_query_params().get('UseMultiAccount')

	def set_UseMultiAccount(self, UseMultiAccount):  # Boolean
		self.add_query_param('UseMultiAccount', UseMultiAccount)
	def get_CloudIp(self): # String
		return self.get_query_params().get('CloudIp')

	def set_CloudIp(self, CloudIp):  # String
		self.add_query_param('CloudIp', CloudIp)
	def get_CenId(self): # String
		return self.get_query_params().get('CenId')

	def set_CenId(self, CenId):  # String
		self.add_query_param('CenId', CenId)
	def get_VirtualBorderRouterId(self): # String
		return self.get_query_params().get('VirtualBorderRouterId')

	def set_VirtualBorderRouterId(self, VirtualBorderRouterId):  # String
		self.add_query_param('VirtualBorderRouterId', VirtualBorderRouterId)
	def get_Direction(self): # String
		return self.get_query_params().get('Direction')

	def set_Direction(self, Direction):  # String
		self.add_query_param('Direction', Direction)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_GroupBy(self): # String
		return self.get_query_params().get('GroupBy')

	def set_GroupBy(self, GroupBy):  # String
		self.add_query_param('GroupBy', GroupBy)
	def get_AccountIds(self): # Array
		return self.get_query_params().get('AccountIds')

	def set_AccountIds(self, AccountIds):  # Array
		self.add_query_param("AccountIds", json.dumps(AccountIds))
	def get_AttachmentId(self): # String
		return self.get_query_params().get('AttachmentId')

	def set_AttachmentId(self, AttachmentId):  # String
		self.add_query_param('AttachmentId', AttachmentId)
