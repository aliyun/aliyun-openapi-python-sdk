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
class UpdateOssCallbackSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateOssCallbackSetting','green')

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ScanCallback(self):
		return self.get_query_params().get('ScanCallback')

	def set_ScanCallback(self,ScanCallback):
		self.add_query_param('ScanCallback',ScanCallback)

	def get_ScanCallbackSuggestions(self):
		return self.get_query_params().get('ScanCallbackSuggestions')

	def set_ScanCallbackSuggestions(self,ScanCallbackSuggestions):
		self.add_query_param('ScanCallbackSuggestions',ScanCallbackSuggestions)

	def get_CallbackSeed(self):
		return self.get_query_params().get('CallbackSeed')

	def set_CallbackSeed(self,CallbackSeed):
		self.add_query_param('CallbackSeed',CallbackSeed)

	def get_AuditCallback(self):
		return self.get_query_params().get('AuditCallback')

	def set_AuditCallback(self,AuditCallback):
		self.add_query_param('AuditCallback',AuditCallback)

	def get_CallbackUrl(self):
		return self.get_query_params().get('CallbackUrl')

	def set_CallbackUrl(self,CallbackUrl):
		self.add_query_param('CallbackUrl',CallbackUrl)

	def get_ServiceModules(self):
		return self.get_query_params().get('ServiceModules')

	def set_ServiceModules(self,ServiceModules):
		self.add_query_param('ServiceModules',ServiceModules)