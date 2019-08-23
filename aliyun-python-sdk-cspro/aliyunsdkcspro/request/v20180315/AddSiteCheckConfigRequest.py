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
from aliyunsdkcspro.endpoint import endpoint_data

class AddSiteCheckConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cspro', '2018-03-15', 'AddSiteCheckConfig','cspro')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SetBaseLine(self):
		return self.get_body_params().get('SetBaseLine')

	def set_SetBaseLine(self,SetBaseLine):
		self.add_body_params('SetBaseLine', SetBaseLine)

	def get_SiteCheckFrequency(self):
		return self.get_body_params().get('SiteCheckFrequency')

	def set_SiteCheckFrequency(self,SiteCheckFrequency):
		self.add_body_params('SiteCheckFrequency', SiteCheckFrequency)

	def get_SiteProtocol(self):
		return self.get_body_params().get('SiteProtocol')

	def set_SiteProtocol(self,SiteProtocol):
		self.add_body_params('SiteProtocol', SiteProtocol)

	def get_IndexUrl(self):
		return self.get_body_params().get('IndexUrl')

	def set_IndexUrl(self,IndexUrl):
		self.add_body_params('IndexUrl', IndexUrl)

	def get_IndexCheckFrequency(self):
		return self.get_body_params().get('IndexCheckFrequency')

	def set_IndexCheckFrequency(self,IndexCheckFrequency):
		self.add_body_params('IndexCheckFrequency', IndexCheckFrequency)

	def get_SiteDomain(self):
		return self.get_body_params().get('SiteDomain')

	def set_SiteDomain(self,SiteDomain):
		self.add_body_params('SiteDomain', SiteDomain)