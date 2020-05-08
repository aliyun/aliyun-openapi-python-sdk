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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class ExportStatisticalDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'ExportStatisticalData','voicebot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BeginTimeLeftRange(self):
		return self.get_query_params().get('BeginTimeLeftRange')

	def set_BeginTimeLeftRange(self,BeginTimeLeftRange):
		self.add_query_param('BeginTimeLeftRange',BeginTimeLeftRange)

	def get_ExportType(self):
		return self.get_query_params().get('ExportType')

	def set_ExportType(self,ExportType):
		self.add_query_param('ExportType',ExportType)

	def get_TimeUnit(self):
		return self.get_query_params().get('TimeUnit')

	def set_TimeUnit(self,TimeUnit):
		self.add_query_param('TimeUnit',TimeUnit)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_BeginTimeRightRange(self):
		return self.get_query_params().get('BeginTimeRightRange')

	def set_BeginTimeRightRange(self,BeginTimeRightRange):
		self.add_query_param('BeginTimeRightRange',BeginTimeRightRange)