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
from aliyunsdkelasticsearch.endpoint import endpoint_data

class UpdateApmRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'UpdateApm','elasticsearch')
		self.set_uri_pattern('/openapi/apm/[instanceId]')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_outputES(self):
		return self.get_query_params().get('outputES')

	def set_outputES(self,outputES):
		self.add_query_param('outputES',outputES)

	def get_outputESPassword(self):
		return self.get_query_params().get('outputESPassword')

	def set_outputESPassword(self,outputESPassword):
		self.add_query_param('outputESPassword',outputESPassword)

	def get_instanceId(self):
		return self.get_path_params().get('instanceId')

	def set_instanceId(self,instanceId):
		self.add_path_param('instanceId',instanceId)

	def get_yml(self):
		return self.get_query_params().get('yml')

	def set_yml(self,yml):
		self.add_query_param('yml',yml)

	def get_outputESUserName(self):
		return self.get_query_params().get('outputESUserName')

	def set_outputESUserName(self,outputESUserName):
		self.add_query_param('outputESUserName',outputESUserName)

	def get_token(self):
		return self.get_query_params().get('token')

	def set_token(self,token):
		self.add_query_param('token',token)