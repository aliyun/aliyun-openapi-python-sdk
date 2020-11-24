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
from aliyunsdkft.endpoint import endpoint_data

class RoaDynamicHostHttpApiRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Ft', '2015-02-02', 'RoaDynamicHostHttpApi')
		self.set_uri_pattern('/web/getData/dynamic')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_proxy_original_security_transport(self):
		return self.get_query_params().get('proxy_original_security_transport')

	def set_proxy_original_security_transport(self,proxy_original_security_transport):
		self.add_query_param('proxy_original_security_transport',proxy_original_security_transport)

	def get_proxy_original_source_ip(self):
		return self.get_query_params().get('proxy_original_source_ip')

	def set_proxy_original_source_ip(self,proxy_original_source_ip):
		self.add_query_param('proxy_original_source_ip',proxy_original_source_ip)

	def get_xacsstatuscode(self):
		return self.get_headers().get('x-acs-status-code')

	def set_xacsstatuscode(self,xacsstatuscode):
		self.add_header('x-acs-status-code',xacsstatuscode)