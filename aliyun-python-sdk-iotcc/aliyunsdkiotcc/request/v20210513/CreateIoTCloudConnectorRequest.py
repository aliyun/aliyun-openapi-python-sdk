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

class CreateIoTCloudConnectorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'CreateIoTCloudConnector','cciot')
		self.set_method('POST')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ISP(self):
		return self.get_query_params().get('ISP')

	def set_ISP(self,ISP):
		self.add_query_param('ISP',ISP)

	def get_IoTCloudConnectorDescription(self):
		return self.get_query_params().get('IoTCloudConnectorDescription')

	def set_IoTCloudConnectorDescription(self,IoTCloudConnectorDescription):
		self.add_query_param('IoTCloudConnectorDescription',IoTCloudConnectorDescription)

	def get_WildcardDomainEnabled(self):
		return self.get_query_params().get('WildcardDomainEnabled')

	def set_WildcardDomainEnabled(self,WildcardDomainEnabled):
		self.add_query_param('WildcardDomainEnabled',WildcardDomainEnabled)

	def get_APN(self):
		return self.get_query_params().get('APN')

	def set_APN(self,APN):
		self.add_query_param('APN',APN)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_IoTCloudConnectorName(self):
		return self.get_query_params().get('IoTCloudConnectorName')

	def set_IoTCloudConnectorName(self,IoTCloudConnectorName):
		self.add_query_param('IoTCloudConnectorName',IoTCloudConnectorName)