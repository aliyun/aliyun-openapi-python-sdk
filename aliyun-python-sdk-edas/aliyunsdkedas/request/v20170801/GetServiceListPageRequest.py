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

class GetServiceListPageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'GetServiceListPage','Edas')
		self.set_uri_pattern('/pop/sp/api/mseForOam/getServiceListPage')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_serviceType(self):
		return self.get_query_params().get('serviceType')

	def set_serviceType(self,serviceType):
		self.add_query_param('serviceType',serviceType)

	def get_side(self):
		return self.get_query_params().get('side')

	def set_side(self,side):
		self.add_query_param('side',side)

	def get_size(self):
		return self.get_query_params().get('size')

	def set_size(self,size):
		self.add_query_param('size',size)

	def get_origin(self):
		return self.get_query_params().get('origin')

	def set_origin(self,origin):
		self.add_query_param('origin',origin)

	def get_searchType(self):
		return self.get_query_params().get('searchType')

	def set_searchType(self,searchType):
		self.add_query_param('searchType',searchType)

	def get_namespace(self):
		return self.get_query_params().get('namespace')

	def set_namespace(self,namespace):
		self.add_query_param('namespace',namespace)

	def get_page(self):
		return self.get_query_params().get('page')

	def set_page(self,page):
		self.add_query_param('page',page)

	def get_region(self):
		return self.get_query_params().get('region')

	def set_region(self,region):
		self.add_query_param('region',region)

	def get_searchValue(self):
		return self.get_query_params().get('searchValue')

	def set_searchValue(self,searchValue):
		self.add_query_param('searchValue',searchValue)