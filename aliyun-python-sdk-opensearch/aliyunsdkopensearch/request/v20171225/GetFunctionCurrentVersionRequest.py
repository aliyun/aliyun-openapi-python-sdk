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

class GetFunctionCurrentVersionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenSearch', '2017-12-25', 'GetFunctionCurrentVersion')
		self.set_uri_pattern('/v4/openapi/functions/[functionName]/current-version')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_modelType(self): # String
		return self.get_query_params().get('modelType')

	def set_modelType(self, modelType):  # String
		self.add_query_param('modelType', modelType)
	def get_functionName(self): # String
		return self.get_path_params().get('functionName')

	def set_functionName(self, functionName):  # String
		self.add_path_param('functionName', functionName)
	def get_domain(self): # String
		return self.get_query_params().get('domain')

	def set_domain(self, domain):  # String
		self.add_query_param('domain', domain)
	def get_functionType(self): # String
		return self.get_query_params().get('functionType')

	def set_functionType(self, functionType):  # String
		self.add_query_param('functionType', functionType)
	def get_category(self): # String
		return self.get_query_params().get('category')

	def set_category(self, category):  # String
		self.add_query_param('category', category)
