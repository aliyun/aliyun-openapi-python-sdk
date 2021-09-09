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

class GetSpringCloudTestMethodRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'GetSpringCloudTestMethod','Edas')
		self.set_uri_pattern('/pop/sp/api/mse/test/springcloud/method')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_appId(self):
		return self.get_query_params().get('appId')

	def set_appId(self,appId):
		self.add_query_param('appId',appId)

	def get_namespace(self):
		return self.get_query_params().get('namespace')

	def set_namespace(self,namespace):
		self.add_query_param('namespace',namespace)

	def get_httpMethod(self):
		return self.get_query_params().get('httpMethod')

	def set_httpMethod(self,httpMethod):
		self.add_query_param('httpMethod',httpMethod)

	def get_methodSignature(self):
		return self.get_query_params().get('methodSignature')

	def set_methodSignature(self,methodSignature):
		self.add_query_param('methodSignature',methodSignature)

	def get_serviceName(self):
		return self.get_query_params().get('serviceName')

	def set_serviceName(self,serviceName):
		self.add_query_param('serviceName',serviceName)

	def get_region(self):
		return self.get_query_params().get('region')

	def set_region(self,region):
		self.add_query_param('region',region)

	def get_requiredPath(self):
		return self.get_query_params().get('requiredPath')

	def set_requiredPath(self,requiredPath):
		self.add_query_param('requiredPath',requiredPath)

	def get_methodController(self):
		return self.get_query_params().get('methodController')

	def set_methodController(self,methodController):
		self.add_query_param('methodController',methodController)