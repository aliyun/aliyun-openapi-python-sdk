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

class ChangeCheckCustomConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ChangeCheckCustomConfig','sas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CheckId(self): # Long
		return self.get_query_params().get('CheckId')

	def set_CheckId(self, CheckId):  # Long
		self.add_query_param('CheckId', CheckId)
	def get_CustomConfigss(self): # RepeatList
		return self.get_query_params().get('CustomConfigs')

	def set_CustomConfigss(self, CustomConfigs):  # RepeatList
		for depth1 in range(len(CustomConfigs)):
			if CustomConfigs[depth1].get('Name') is not None:
				self.add_query_param('CustomConfigs.' + str(depth1 + 1) + '.Name', CustomConfigs[depth1].get('Name'))
			if CustomConfigs[depth1].get('Value') is not None:
				self.add_query_param('CustomConfigs.' + str(depth1 + 1) + '.Value', CustomConfigs[depth1].get('Value'))
			if CustomConfigs[depth1].get('Operation') is not None:
				self.add_query_param('CustomConfigs.' + str(depth1 + 1) + '.Operation', CustomConfigs[depth1].get('Operation'))
