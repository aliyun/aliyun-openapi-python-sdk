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
from aliyunsdkwebplus.endpoint import endpoint_data

class DescribeApplicationsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'DescribeApplications','webx')
		self.set_uri_pattern('/pop/v1/wam/application')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppName(self):
		return self.get_query_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_query_param('AppName',AppName)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CategorySearch(self):
		return self.get_query_params().get('CategorySearch')

	def set_CategorySearch(self,CategorySearch):
		self.add_query_param('CategorySearch',CategorySearch)

	def get_StackSearch(self):
		return self.get_query_params().get('StackSearch')

	def set_StackSearch(self,StackSearch):
		self.add_query_param('StackSearch',StackSearch)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_AppSearch(self):
		return self.get_query_params().get('AppSearch')

	def set_AppSearch(self,AppSearch):
		self.add_query_param('AppSearch',AppSearch)

	def get_EnvSearch(self):
		return self.get_query_params().get('EnvSearch')

	def set_EnvSearch(self,EnvSearch):
		self.add_query_param('EnvSearch',EnvSearch)