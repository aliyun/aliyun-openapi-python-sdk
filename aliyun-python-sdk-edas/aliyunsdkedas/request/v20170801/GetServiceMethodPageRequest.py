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

class GetServiceMethodPageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'GetServiceMethodPage','Edas')
		self.set_uri_pattern('/pop/sp/api/mseForOam/getServiceMethodPage')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_registryType(self):
		return self.get_query_params().get('registryType')

	def set_registryType(self,registryType):
		self.add_query_param('registryType',registryType)

	def get_origin(self):
		return self.get_query_params().get('origin')

	def set_origin(self,origin):
		self.add_query_param('origin',origin)

	def get_ip(self):
		return self.get_query_params().get('ip')

	def set_ip(self,ip):
		self.add_query_param('ip',ip)

	def get_source(self):
		return self.get_query_params().get('source')

	def set_source(self,source):
		self.add_query_param('source',source)

	def get_pageNumber(self):
		return self.get_query_params().get('pageNumber')

	def set_pageNumber(self,pageNumber):
		self.add_query_param('pageNumber',pageNumber)

	def get_path(self):
		return self.get_query_params().get('path')

	def set_path(self,path):
		self.add_query_param('path',path)

	def get_serviceType(self):
		return self.get_query_params().get('serviceType')

	def set_serviceType(self,serviceType):
		self.add_query_param('serviceType',serviceType)

	def get_appId(self):
		return self.get_query_params().get('appId')

	def set_appId(self,appId):
		self.add_query_param('appId',appId)

	def get_namespace(self):
		return self.get_query_params().get('namespace')

	def set_namespace(self,namespace):
		self.add_query_param('namespace',namespace)

	def get_serviceVersion(self):
		return self.get_query_params().get('serviceVersion')

	def set_serviceVersion(self,serviceVersion):
		self.add_query_param('serviceVersion',serviceVersion)

	def get_pageSize(self):
		return self.get_query_params().get('pageSize')

	def set_pageSize(self,pageSize):
		self.add_query_param('pageSize',pageSize)

	def get_name(self):
		return self.get_query_params().get('name')

	def set_name(self,name):
		self.add_query_param('name',name)

	def get_serviceName(self):
		return self.get_query_params().get('serviceName')

	def set_serviceName(self,serviceName):
		self.add_query_param('serviceName',serviceName)

	def get_region(self):
		return self.get_query_params().get('region')

	def set_region(self,region):
		self.add_query_param('region',region)

	def get_serviceId(self):
		return self.get_query_params().get('serviceId')

	def set_serviceId(self,serviceId):
		self.add_query_param('serviceId',serviceId)

	def get_methodController(self):
		return self.get_query_params().get('methodController')

	def set_methodController(self,methodController):
		self.add_query_param('methodController',methodController)

	def get_group(self):
		return self.get_query_params().get('group')

	def set_group(self,group):
		self.add_query_param('group',group)