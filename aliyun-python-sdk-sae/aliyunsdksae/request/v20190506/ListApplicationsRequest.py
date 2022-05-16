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
from aliyunsdksae.endpoint import endpoint_data

class ListApplicationsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'sae', '2019-05-06', 'ListApplications','serverless')
		self.set_uri_pattern('/pop/v1/sam/app/listApplications')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_FieldValue(self): # String
		return self.get_query_params().get('FieldValue')

	def set_FieldValue(self, FieldValue):  # String
		self.add_query_param('FieldValue', FieldValue)
	def get_Reverse(self): # Boolean
		return self.get_query_params().get('Reverse')

	def set_Reverse(self, Reverse):  # Boolean
		self.add_query_param('Reverse', Reverse)
	def get_FieldType(self): # String
		return self.get_query_params().get('FieldType')

	def set_FieldType(self, FieldType):  # String
		self.add_query_param('FieldType', FieldType)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
