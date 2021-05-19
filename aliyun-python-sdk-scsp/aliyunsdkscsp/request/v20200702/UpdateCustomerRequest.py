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
from aliyunsdkscsp.endpoint import endpoint_data

class UpdateCustomerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'UpdateCustomer')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Industry(self): # String
		return self.get_query_params().get('Industry')

	def set_Industry(self, Industry):  # String
		self.add_query_param('Industry', Industry)
	def get_OuterIdType(self): # Integer
		return self.get_query_params().get('OuterIdType')

	def set_OuterIdType(self, OuterIdType):  # Integer
		self.add_query_param('OuterIdType', OuterIdType)
	def get_Dingding(self): # String
		return self.get_query_params().get('Dingding')

	def set_Dingding(self, Dingding):  # String
		self.add_query_param('Dingding', Dingding)
	def get_BizType(self): # String
		return self.get_query_params().get('BizType')

	def set_BizType(self, BizType):  # String
		self.add_query_param('BizType', BizType)
	def get_TypeCode(self): # String
		return self.get_query_params().get('TypeCode')

	def set_TypeCode(self, TypeCode):  # String
		self.add_query_param('TypeCode', TypeCode)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Contacter(self): # String
		return self.get_query_params().get('Contacter')

	def set_Contacter(self, Contacter):  # String
		self.add_query_param('Contacter', Contacter)
	def get_ProdLineId(self): # Long
		return self.get_query_params().get('ProdLineId')

	def set_ProdLineId(self, ProdLineId):  # Long
		self.add_query_param('ProdLineId', ProdLineId)
	def get_Phone(self): # String
		return self.get_query_params().get('Phone')

	def set_Phone(self, Phone):  # String
		self.add_query_param('Phone', Phone)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_CustomerId(self): # Long
		return self.get_query_params().get('CustomerId')

	def set_CustomerId(self, CustomerId):  # Long
		self.add_query_param('CustomerId', CustomerId)
	def get_ManagerName(self): # String
		return self.get_query_params().get('ManagerName')

	def set_ManagerName(self, ManagerName):  # String
		self.add_query_param('ManagerName', ManagerName)
	def get_OuterId(self): # String
		return self.get_query_params().get('OuterId')

	def set_OuterId(self, OuterId):  # String
		self.add_query_param('OuterId', OuterId)
	def get_Position(self): # String
		return self.get_query_params().get('Position')

	def set_Position(self, Position):  # String
		self.add_query_param('Position', Position)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
