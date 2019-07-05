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
class UpdateWebsiteInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateWebsiteInstance','green')

	def get_SiteProtocol(self):
		return self.get_query_params().get('SiteProtocol')

	def set_SiteProtocol(self,SiteProtocol):
		self.add_query_param('SiteProtocol',SiteProtocol)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_WebsiteScanInterval(self):
		return self.get_query_params().get('WebsiteScanInterval')

	def set_WebsiteScanInterval(self,WebsiteScanInterval):
		self.add_query_param('WebsiteScanInterval',WebsiteScanInterval)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_IndexPage(self):
		return self.get_query_params().get('IndexPage')

	def set_IndexPage(self,IndexPage):
		self.add_query_param('IndexPage',IndexPage)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_IndexPageScanInterval(self):
		return self.get_query_params().get('IndexPageScanInterval')

	def set_IndexPageScanInterval(self,IndexPageScanInterval):
		self.add_query_param('IndexPageScanInterval',IndexPageScanInterval)