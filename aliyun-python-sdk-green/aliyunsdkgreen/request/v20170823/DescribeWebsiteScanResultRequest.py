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
from aliyunsdkgreen.endpoint import endpoint_data

class DescribeWebsiteScanResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'DescribeWebsiteScanResult','green')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SubServiceModule(self):
		return self.get_query_params().get('SubServiceModule')

	def set_SubServiceModule(self,SubServiceModule):
		self.add_query_param('SubServiceModule',SubServiceModule)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_TotalCount(self):
		return self.get_query_params().get('TotalCount')

	def set_TotalCount(self,TotalCount):
		self.add_query_param('TotalCount',TotalCount)

	def get_SiteUrl(self):
		return self.get_query_params().get('SiteUrl')

	def set_SiteUrl(self,SiteUrl):
		self.add_query_param('SiteUrl',SiteUrl)

	def get_HandleStatus(self):
		return self.get_query_params().get('HandleStatus')

	def set_HandleStatus(self,HandleStatus):
		self.add_query_param('HandleStatus',HandleStatus)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_Label(self):
		return self.get_query_params().get('Label')

	def set_Label(self,Label):
		self.add_query_param('Label',Label)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)