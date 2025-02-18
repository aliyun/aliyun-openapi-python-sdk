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
from aliyunsdksgw.endpoint import endpoint_data

class SwitchCSGClientsReverseSyncConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'SwitchCSGClientsReverseSyncConfiguration','hcs_sgw')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ReverseSyncInternalSecond(self): # Integer
		return self.get_query_params().get('ReverseSyncInternalSecond')

	def set_ReverseSyncInternalSecond(self, ReverseSyncInternalSecond):  # Integer
		self.add_query_param('ReverseSyncInternalSecond', ReverseSyncInternalSecond)
	def get_ClientIds(self): # Array
		return self.get_query_params().get('ClientIds')

	def set_ClientIds(self, ClientIds):  # Array
		for index1, value1 in enumerate(ClientIds):
			self.add_query_param('ClientIds.' + str(index1 + 1), value1)
	def get_ClientRegionId(self): # String
		return self.get_query_params().get('ClientRegionId')

	def set_ClientRegionId(self, ClientRegionId):  # String
		self.add_query_param('ClientRegionId', ClientRegionId)
	def get_IsReverseSync(self): # Boolean
		return self.get_query_params().get('IsReverseSync')

	def set_IsReverseSync(self, IsReverseSync):  # Boolean
		self.add_query_param('IsReverseSync', IsReverseSync)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
