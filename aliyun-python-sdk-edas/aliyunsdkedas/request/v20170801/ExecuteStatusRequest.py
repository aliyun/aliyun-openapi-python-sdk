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

class ExecuteStatusRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'ExecuteStatus','Edas')
		self.set_uri_pattern('/pop/sp/api/mse/status/execute')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AccountId(self):
		return self.get_query_params().get('AccountId')

	def set_AccountId(self,AccountId):
		self.add_query_param('AccountId',AccountId)

	def get_NamespaceId(self):
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self,NamespaceId):
		self.add_query_param('NamespaceId',NamespaceId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Ip(self):
		return self.get_query_params().get('Ip')

	def set_Ip(self,Ip):
		self.add_query_param('Ip',Ip)

	def get_TenantId(self):
		return self.get_query_params().get('TenantId')

	def set_TenantId(self,TenantId):
		self.add_query_param('TenantId',TenantId)

	def get_PodName(self):
		return self.get_query_params().get('PodName')

	def set_PodName(self,PodName):
		self.add_query_param('PodName',PodName)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)