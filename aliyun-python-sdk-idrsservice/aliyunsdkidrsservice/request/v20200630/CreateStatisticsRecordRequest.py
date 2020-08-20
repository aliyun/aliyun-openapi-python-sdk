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
from aliyunsdkidrsservice.endpoint import endpoint_data

class CreateStatisticsRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'CreateStatisticsRecord','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BeginAt(self):
		return self.get_query_params().get('BeginAt')

	def set_BeginAt(self,BeginAt):
		self.add_query_param('BeginAt',BeginAt)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_EndAt(self):
		return self.get_query_params().get('EndAt')

	def set_EndAt(self,EndAt):
		self.add_query_param('EndAt',EndAt)

	def get_DeviceId(self):
		return self.get_query_params().get('DeviceId')

	def set_DeviceId(self,DeviceId):
		self.add_query_param('DeviceId',DeviceId)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)