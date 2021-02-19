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

class ListDefaultCollectorConfigurationsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListDefaultCollectorConfigurations','elasticsearch')
		self.set_uri_pattern('/openapi/beats/default-configurations')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_resType(self):
		return self.get_query_params().get('resType')

	def set_resType(self,resType):
		self.add_query_param('resType',resType)

	def get_resVersion(self):
		return self.get_query_params().get('resVersion')

	def set_resVersion(self,resVersion):
		self.add_query_param('resVersion',resVersion)

	def get_sourceType(self):
		return self.get_query_params().get('sourceType')

	def set_sourceType(self,sourceType):
		self.add_query_param('sourceType',sourceType)