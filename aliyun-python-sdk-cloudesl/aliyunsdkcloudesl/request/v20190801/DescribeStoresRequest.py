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
from aliyunsdkcloudesl.endpoint import endpoint_data

class DescribeStoresRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2019-08-01', 'DescribeStores','cloudesl')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StoreName(self):
		return self.get_body_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_body_params('StoreName', StoreName)

	def get_StoreId(self):
		return self.get_body_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_body_params('StoreId', StoreId)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_FromDate(self):
		return self.get_body_params().get('FromDate')

	def set_FromDate(self,FromDate):
		self.add_body_params('FromDate', FromDate)

	def get_CompanyId(self):
		return self.get_body_params().get('CompanyId')

	def set_CompanyId(self,CompanyId):
		self.add_body_params('CompanyId', CompanyId)

	def get_ToDate(self):
		return self.get_body_params().get('ToDate')

	def set_ToDate(self,ToDate):
		self.add_body_params('ToDate', ToDate)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_Brand(self):
		return self.get_body_params().get('Brand')

	def set_Brand(self,Brand):
		self.add_body_params('Brand', Brand)