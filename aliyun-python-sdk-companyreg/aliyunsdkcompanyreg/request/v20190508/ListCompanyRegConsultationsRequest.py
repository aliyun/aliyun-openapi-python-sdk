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

class ListCompanyRegConsultationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'ListCompanyRegConsultations')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EndGmtCreate(self): # Long
		return self.get_query_params().get('EndGmtCreate')

	def set_EndGmtCreate(self, EndGmtCreate):  # Long
		self.add_query_param('EndGmtCreate', EndGmtCreate)
	def get_City(self): # String
		return self.get_query_params().get('City')

	def set_City(self, City):  # String
		self.add_query_param('City', City)
	def get_PageNum(self): # Integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # Integer
		self.add_query_param('PageNum', PageNum)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_BizId(self): # String
		return self.get_query_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_query_param('BizId', BizId)
	def get_StartGmtCreate(self): # Long
		return self.get_query_params().get('StartGmtCreate')

	def set_StartGmtCreate(self, StartGmtCreate):  # Long
		self.add_query_param('StartGmtCreate', StartGmtCreate)
