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
from aliyunsdkarms.endpoint import endpoint_data

class ImportCustomAlertRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'ImportCustomAlertRules','arms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsAutoStart(self):
		return self.get_query_params().get('IsAutoStart')

	def set_IsAutoStart(self,IsAutoStart):
		self.add_query_param('IsAutoStart',IsAutoStart)

	def get_ContactGroupIds(self):
		return self.get_query_params().get('ContactGroupIds')

	def set_ContactGroupIds(self,ContactGroupIds):
		self.add_query_param('ContactGroupIds',ContactGroupIds)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_TemplageAlertConfig(self):
		return self.get_query_params().get('TemplageAlertConfig')

	def set_TemplageAlertConfig(self,TemplageAlertConfig):
		self.add_query_param('TemplageAlertConfig',TemplageAlertConfig)