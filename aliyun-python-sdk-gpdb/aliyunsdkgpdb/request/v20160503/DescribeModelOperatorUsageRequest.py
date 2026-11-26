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
from aliyunsdkgpdb.endpoint import endpoint_data

class DescribeModelOperatorUsageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'DescribeModelOperatorUsage','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Keys(self): # Array
		return self.get_query_params().get('Keys')

	def set_Keys(self, Keys):  # Array
		for index1, value1 in enumerate(Keys):
			self.add_query_param('Keys.' + str(index1 + 1), value1)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_GroupBy(self): # String
		return self.get_query_params().get('GroupBy')

	def set_GroupBy(self, GroupBy):  # String
		self.add_query_param('GroupBy', GroupBy)
	def get_ApiKeyIds(self): # Array
		return self.get_query_params().get('ApiKeyIds')

	def set_ApiKeyIds(self, ApiKeyIds):  # Array
		for index1, value1 in enumerate(ApiKeyIds):
			self.add_query_param('ApiKeyIds.' + str(index1 + 1), value1)
	def get_ModelNames(self): # Array
		return self.get_query_params().get('ModelNames')

	def set_ModelNames(self, ModelNames):  # Array
		for index1, value1 in enumerate(ModelNames):
			self.add_query_param('ModelNames.' + str(index1 + 1), value1)
