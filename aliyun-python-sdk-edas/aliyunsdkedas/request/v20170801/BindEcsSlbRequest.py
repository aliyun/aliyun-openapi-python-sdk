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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class BindEcsSlbRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'BindEcsSlb','edas')
		self.set_uri_pattern('/pop/v5/app/slb/bind_slb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VServerGroupId(self):
		return self.get_query_params().get('VServerGroupId')

	def set_VServerGroupId(self,VServerGroupId):
		self.add_query_param('VServerGroupId',VServerGroupId)

	def get_ListenerPort(self):
		return self.get_query_params().get('ListenerPort')

	def set_ListenerPort(self,ListenerPort):
		self.add_query_param('ListenerPort',ListenerPort)

	def get_VForwardingUrlRule(self):
		return self.get_query_params().get('VForwardingUrlRule')

	def set_VForwardingUrlRule(self,VForwardingUrlRule):
		self.add_query_param('VForwardingUrlRule',VForwardingUrlRule)

	def get_SlbId(self):
		return self.get_query_params().get('SlbId')

	def set_SlbId(self,SlbId):
		self.add_query_param('SlbId',SlbId)

	def get_DeployGroupId(self):
		return self.get_query_params().get('DeployGroupId')

	def set_DeployGroupId(self,DeployGroupId):
		self.add_query_param('DeployGroupId',DeployGroupId)

	def get_ListenerHealthCheckUrl(self):
		return self.get_query_params().get('ListenerHealthCheckUrl')

	def set_ListenerHealthCheckUrl(self,ListenerHealthCheckUrl):
		self.add_query_param('ListenerHealthCheckUrl',ListenerHealthCheckUrl)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ListenerProtocol(self):
		return self.get_query_params().get('ListenerProtocol')

	def set_ListenerProtocol(self,ListenerProtocol):
		self.add_query_param('ListenerProtocol',ListenerProtocol)

	def get_VServerGroupName(self):
		return self.get_query_params().get('VServerGroupName')

	def set_VServerGroupName(self,VServerGroupName):
		self.add_query_param('VServerGroupName',VServerGroupName)