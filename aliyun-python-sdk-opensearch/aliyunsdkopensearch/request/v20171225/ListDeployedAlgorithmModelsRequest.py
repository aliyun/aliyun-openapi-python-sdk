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
from aliyunsdkopensearch.endpoint import endpoint_data

class ListDeployedAlgorithmModelsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenSearch', '2017-12-25', 'ListDeployedAlgorithmModels','opensearch')
		self.set_uri_pattern('/v4/openapi/app-groups/[appGroupIdentity]/deployed-algorithm-models')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_algorithmType(self):
		return self.get_query_params().get('algorithmType')

	def set_algorithmType(self,algorithmType):
		self.add_query_param('algorithmType',algorithmType)

	def get_inServiceOnly(self):
		return self.get_query_params().get('inServiceOnly')

	def set_inServiceOnly(self,inServiceOnly):
		self.add_query_param('inServiceOnly',inServiceOnly)

	def get_appGroupIdentity(self):
		return self.get_path_params().get('appGroupIdentity')

	def set_appGroupIdentity(self,appGroupIdentity):
		self.add_path_param('appGroupIdentity',appGroupIdentity)