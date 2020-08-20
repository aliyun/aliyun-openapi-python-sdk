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

class CreateStatisticsTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'CreateStatisticsTask','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_DepartmentIds(self):
		return self.get_query_params().get('DepartmentIds')

	def set_DepartmentIds(self, DepartmentIds):
		for depth1 in range(len(DepartmentIds)):
			if DepartmentIds[depth1] is not None:
				self.add_query_param('DepartmentId.' + str(depth1 + 1) , DepartmentIds[depth1])

	def get_DateTo(self):
		return self.get_query_params().get('DateTo')

	def set_DateTo(self,DateTo):
		self.add_query_param('DateTo',DateTo)

	def get_DateFrom(self):
		return self.get_query_params().get('DateFrom')

	def set_DateFrom(self,DateFrom):
		self.add_query_param('DateFrom',DateFrom)