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
from aliyunsdkdas.endpoint import endpoint_data

class CreateAdamBenchTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'CreateAdamBenchTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcEngine(self): # String
		return self.get_query_params().get('SrcEngine')

	def set_SrcEngine(self, SrcEngine):  # String
		self.add_query_param('SrcEngine', SrcEngine)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RequestStartTime(self): # Long
		return self.get_query_params().get('RequestStartTime')

	def set_RequestStartTime(self, RequestStartTime):  # Long
		self.add_query_param('RequestStartTime', RequestStartTime)
	def get_DstSuperPassword(self): # String
		return self.get_query_params().get('DstSuperPassword')

	def set_DstSuperPassword(self, DstSuperPassword):  # String
		self.add_query_param('DstSuperPassword', DstSuperPassword)
	def get_DstSuperAccount(self): # String
		return self.get_query_params().get('DstSuperAccount')

	def set_DstSuperAccount(self, DstSuperAccount):  # String
		self.add_query_param('DstSuperAccount', DstSuperAccount)
	def get_Rate(self): # Integer
		return self.get_query_params().get('Rate')

	def set_Rate(self, Rate):  # Integer
		self.add_query_param('Rate', Rate)
	def get_DstInstanceId(self): # String
		return self.get_query_params().get('DstInstanceId')

	def set_DstInstanceId(self, DstInstanceId):  # String
		self.add_query_param('DstInstanceId', DstInstanceId)
	def get_RequestDuration(self): # Long
		return self.get_query_params().get('RequestDuration')

	def set_RequestDuration(self, RequestDuration):  # Long
		self.add_query_param('RequestDuration', RequestDuration)
	def get_SrcMeanQps(self): # Double
		return self.get_query_params().get('SrcMeanQps')

	def set_SrcMeanQps(self, SrcMeanQps):  # Double
		self.add_query_param('SrcMeanQps', SrcMeanQps)
	def get_SrcMaxQps(self): # Double
		return self.get_query_params().get('SrcMaxQps')

	def set_SrcMaxQps(self, SrcMaxQps):  # Double
		self.add_query_param('SrcMaxQps', SrcMaxQps)
	def get_SrcEngineVersion(self): # String
		return self.get_query_params().get('SrcEngineVersion')

	def set_SrcEngineVersion(self, SrcEngineVersion):  # String
		self.add_query_param('SrcEngineVersion', SrcEngineVersion)
	def get_SrcSqlOssAddr(self): # String
		return self.get_query_params().get('SrcSqlOssAddr')

	def set_SrcSqlOssAddr(self, SrcSqlOssAddr):  # String
		self.add_query_param('SrcSqlOssAddr', SrcSqlOssAddr)
