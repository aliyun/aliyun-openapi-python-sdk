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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class ListIcpApplicationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'ListIcpApplications')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IntentionBizId(self): # String
		return self.get_query_params().get('IntentionBizId')

	def set_IntentionBizId(self, IntentionBizId):  # String
		self.add_query_param('IntentionBizId', IntentionBizId)
	def get_Type(self): # Integer
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # Integer
		self.add_query_param('Type', Type)
	def get_ApplicationStatus(self): # Integer
		return self.get_query_params().get('ApplicationStatus')

	def set_ApplicationStatus(self, ApplicationStatus):  # Integer
		self.add_query_param('ApplicationStatus', ApplicationStatus)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_CompanyName(self): # String
		return self.get_query_params().get('CompanyName')

	def set_CompanyName(self, CompanyName):  # String
		self.add_query_param('CompanyName', CompanyName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_SortOrder(self): # String
		return self.get_query_params().get('SortOrder')

	def set_SortOrder(self, SortOrder):  # String
		self.add_query_param('SortOrder', SortOrder)
	def get_SortField(self): # String
		return self.get_query_params().get('SortField')

	def set_SortField(self, SortField):  # String
		self.add_query_param('SortField', SortField)
