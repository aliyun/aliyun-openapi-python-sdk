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
from aliyunsdkdomain.endpoint import endpoint_data

class QueryPurchasedDomainsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'QueryPurchasedDomains','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UpdateTimeOrder(self): # Boolean
		return self.get_body_params().get('UpdateTimeOrder')

	def set_UpdateTimeOrder(self, UpdateTimeOrder):  # Boolean
		self.add_body_params('UpdateTimeOrder', UpdateTimeOrder)
	def get_DomainName(self): # String
		return self.get_body_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_body_params('DomainName', DomainName)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_ProductType(self): # Integer
		return self.get_body_params().get('ProductType')

	def set_ProductType(self, ProductType):  # Integer
		self.add_body_params('ProductType', ProductType)
	def get_OperationStatus(self): # Integer
		return self.get_body_params().get('OperationStatus')

	def set_OperationStatus(self, OperationStatus):  # Integer
		self.add_body_params('OperationStatus', OperationStatus)
	def get_StartOperationTime(self): # String
		return self.get_body_params().get('StartOperationTime')

	def set_StartOperationTime(self, StartOperationTime):  # String
		self.add_body_params('StartOperationTime', StartOperationTime)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_EndOperationTime(self): # String
		return self.get_body_params().get('EndOperationTime')

	def set_EndOperationTime(self, EndOperationTime):  # String
		self.add_body_params('EndOperationTime', EndOperationTime)
	def get_OpTimeOrder(self): # Boolean
		return self.get_body_params().get('OpTimeOrder')

	def set_OpTimeOrder(self, OpTimeOrder):  # Boolean
		self.add_body_params('OpTimeOrder', OpTimeOrder)
