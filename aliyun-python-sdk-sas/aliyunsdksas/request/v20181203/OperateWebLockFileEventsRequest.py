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
from aliyunsdksas.endpoint import endpoint_data

class OperateWebLockFileEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'OperateWebLockFileEvents','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EventIdss(self): # RepeatList
		return self.get_query_params().get('EventIds')

	def set_EventIdss(self, EventIds):  # RepeatList
		for depth1 in range(len(EventIds)):
			self.add_query_param('EventIds.' + str(depth1 + 1), EventIds[depth1])
	def get_OperationCode(self): # String
		return self.get_query_params().get('OperationCode')

	def set_OperationCode(self, OperationCode):  # String
		self.add_query_param('OperationCode', OperationCode)
	def get_DealAll(self): # Integer
		return self.get_query_params().get('DealAll')

	def set_DealAll(self, DealAll):  # Integer
		self.add_query_param('DealAll', DealAll)
