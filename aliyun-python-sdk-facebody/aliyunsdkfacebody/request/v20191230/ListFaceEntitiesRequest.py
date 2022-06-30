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
from aliyunsdkfacebody.endpoint import endpoint_data

class ListFaceEntitiesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'ListFaceEntities','facebody')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EntityIdPrefix(self): # String
		return self.get_body_params().get('EntityIdPrefix')

	def set_EntityIdPrefix(self, EntityIdPrefix):  # String
		self.add_body_params('EntityIdPrefix', EntityIdPrefix)
	def get_Limit(self): # Integer
		return self.get_body_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_body_params('Limit', Limit)
	def get_Order(self): # String
		return self.get_body_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_body_params('Order', Order)
	def get_Offset(self): # Integer
		return self.get_body_params().get('Offset')

	def set_Offset(self, Offset):  # Integer
		self.add_body_params('Offset', Offset)
	def get_Token(self): # String
		return self.get_body_params().get('Token')

	def set_Token(self, Token):  # String
		self.add_body_params('Token', Token)
	def get_Labels(self): # String
		return self.get_body_params().get('Labels')

	def set_Labels(self, Labels):  # String
		self.add_body_params('Labels', Labels)
	def get_DbName(self): # String
		return self.get_body_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_body_params('DbName', DbName)
