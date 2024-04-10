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

class GetInternetTupleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nis', '2021-12-16', 'GetInternetTuple','networkana')
		self.set_method('POST')

	def get_OtherPort(self): # String
		return self.get_query_params().get('OtherPort')

	def set_OtherPort(self, OtherPort):  # String
		self.add_query_param('OtherPort', OtherPort)
	def get_CloudIsp(self): # String
		return self.get_query_params().get('CloudIsp')

	def set_CloudIsp(self, CloudIsp):  # String
		self.add_query_param('CloudIsp', CloudIsp)
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
	def get_InstanceList(self): # Array
		return self.get_query_params().get('InstanceList')

	def set_InstanceList(self, InstanceList):  # Array
		self.add_query_param("InstanceList", json.dumps(InstanceList))
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
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_TupleType(self): # Integer
		return self.get_query_params().get('TupleType')

	def set_TupleType(self, TupleType):  # Integer
		self.add_query_param('TupleType', TupleType)
	def get_CloudIp(self): # String
		return self.get_query_params().get('CloudIp')

	def set_CloudIp(self, CloudIp):  # String
		self.add_query_param('CloudIp', CloudIp)
	def get_CloudIpList(self): # Array
		return self.get_query_params().get('CloudIpList')

	def set_CloudIpList(self, CloudIpList):  # Array
		self.add_query_param("CloudIpList", json.dumps(CloudIpList))
	def get_OtherIsp(self): # String
		return self.get_query_params().get('OtherIsp')

	def set_OtherIsp(self, OtherIsp):  # String
		self.add_query_param('OtherIsp', OtherIsp)
	def get_OtherCountry(self): # String
		return self.get_query_params().get('OtherCountry')

	def set_OtherCountry(self, OtherCountry):  # String
		self.add_query_param('OtherCountry', OtherCountry)
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
	def get_OtherCity(self): # String
		return self.get_query_params().get('OtherCity')

	def set_OtherCity(self, OtherCity):  # String
		self.add_query_param('OtherCity', OtherCity)
	def get_AccountIdss(self): # RepeatList
		return self.get_query_params().get('AccountIds')

	def set_AccountIdss(self, AccountIds):  # RepeatList
		for depth1 in range(len(AccountIds)):
			self.add_query_param('AccountIds.' + str(depth1 + 1), AccountIds[depth1])
