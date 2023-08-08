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
from aliyunsdklive.endpoint import endpoint_data

class DescribeLiveDomainTranscodeParamsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'DescribeLiveDomainTranscodeParams','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_pushdomain(self): # String
		return self.get_query_params().get('pushdomain')

	def set_pushdomain(self, pushdomain):  # String
		self.add_query_param('pushdomain', pushdomain)
	def get_app(self): # String
		return self.get_query_params().get('app')

	def set_app(self, app):  # String
		self.add_query_param('app', app)
	def get_template_name(self): # String
		return self.get_query_params().get('template_name')

	def set_template_name(self, template_name):  # String
		self.add_query_param('template_name', template_name)
