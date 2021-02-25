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

class AddServiceTimeConfigRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'AddServiceTimeConfig','edas')
		self.set_uri_pattern('/pop/sp/api/timeout/add')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Path(self):
		return self.get_query_params().get('Path')

	def set_Path(self,Path):
		self.add_query_param('Path',Path)

	def get_ServiceType(self):
		return self.get_query_params().get('ServiceType')

	def set_ServiceType(self,ServiceType):
		self.add_query_param('ServiceType',ServiceType)

	def get_ConsumerAppId(self):
		return self.get_query_params().get('ConsumerAppId')

	def set_ConsumerAppId(self,ConsumerAppId):
		self.add_query_param('ConsumerAppId',ConsumerAppId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ServiceVersion(self):
		return self.get_query_params().get('ServiceVersion')

	def set_ServiceVersion(self,ServiceVersion):
		self.add_query_param('ServiceVersion',ServiceVersion)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_Source(self):
		return self.get_query_params().get('Source')

	def set_Source(self,Source):
		self.add_query_param('Source',Source)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)

	def get_ServiceGroup(self):
		return self.get_query_params().get('ServiceGroup')

	def set_ServiceGroup(self,ServiceGroup):
		self.add_query_param('ServiceGroup',ServiceGroup)

	def get_ConsumerAppName(self):
		return self.get_query_params().get('ConsumerAppName')

	def set_ConsumerAppName(self,ConsumerAppName):
		self.add_query_param('ConsumerAppName',ConsumerAppName)

	def get_Timeout(self):
		return self.get_query_params().get('Timeout')

	def set_Timeout(self,Timeout):
		self.add_query_param('Timeout',Timeout)