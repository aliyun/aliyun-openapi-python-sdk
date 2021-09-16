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
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'CreateAdamBenchTask','das')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SrcEngine(self):
		return self.get_query_params().get('SrcEngine')

	def set_SrcEngine(self,SrcEngine):
		self.add_query_param('SrcEngine',SrcEngine)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RequestStartTime(self):
		return self.get_query_params().get('RequestStartTime')

	def set_RequestStartTime(self,RequestStartTime):
		self.add_query_param('RequestStartTime',RequestStartTime)

	def get_DstSuperPassword(self):
		return self.get_query_params().get('DstSuperPassword')

	def set_DstSuperPassword(self,DstSuperPassword):
		self.add_query_param('DstSuperPassword',DstSuperPassword)

	def get_DstSuperAccount(self):
		return self.get_query_params().get('DstSuperAccount')

	def set_DstSuperAccount(self,DstSuperAccount):
		self.add_query_param('DstSuperAccount',DstSuperAccount)

	def get_Rate(self):
		return self.get_query_params().get('Rate')

	def set_Rate(self,Rate):
		self.add_query_param('Rate',Rate)

	def get_DstInstanceId(self):
		return self.get_query_params().get('DstInstanceId')

	def set_DstInstanceId(self,DstInstanceId):
		self.add_query_param('DstInstanceId',DstInstanceId)

	def get_RequestDuration(self):
		return self.get_query_params().get('RequestDuration')

	def set_RequestDuration(self,RequestDuration):
		self.add_query_param('RequestDuration',RequestDuration)

	def get_SrcMeanQps(self):
		return self.get_query_params().get('SrcMeanQps')

	def set_SrcMeanQps(self,SrcMeanQps):
		self.add_query_param('SrcMeanQps',SrcMeanQps)

	def get_SrcMaxQps(self):
		return self.get_query_params().get('SrcMaxQps')

	def set_SrcMaxQps(self,SrcMaxQps):
		self.add_query_param('SrcMaxQps',SrcMaxQps)

	def get_SrcEngineVersion(self):
		return self.get_query_params().get('SrcEngineVersion')

	def set_SrcEngineVersion(self,SrcEngineVersion):
		self.add_query_param('SrcEngineVersion',SrcEngineVersion)

	def get_SrcSqlOssAddr(self):
		return self.get_query_params().get('SrcSqlOssAddr')

	def set_SrcSqlOssAddr(self,SrcSqlOssAddr):
		self.add_query_param('SrcSqlOssAddr',SrcSqlOssAddr)