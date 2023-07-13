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
from aliyunsdkmse.endpoint import endpoint_data

class AddGatewayAuthConsumerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'AddGatewayAuthConsumer','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_KeyName(self): # String
		return self.get_query_params().get('KeyName')

	def set_KeyName(self, KeyName):  # String
		self.add_query_param('KeyName', KeyName)
	def get_TokenPrefix(self): # String
		return self.get_query_params().get('TokenPrefix')

	def set_TokenPrefix(self, TokenPrefix):  # String
		self.add_query_param('TokenPrefix', TokenPrefix)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_GatewayUniqueId(self): # String
		return self.get_query_params().get('GatewayUniqueId')

	def set_GatewayUniqueId(self, GatewayUniqueId):  # String
		self.add_query_param('GatewayUniqueId', GatewayUniqueId)
	def get_Jwks(self): # String
		return self.get_query_params().get('Jwks')

	def set_Jwks(self, Jwks):  # String
		self.add_query_param('Jwks', Jwks)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_TokenPosition(self): # String
		return self.get_query_params().get('TokenPosition')

	def set_TokenPosition(self, TokenPosition):  # String
		self.add_query_param('TokenPosition', TokenPosition)
	def get_EncodeType(self): # String
		return self.get_query_params().get('EncodeType')

	def set_EncodeType(self, EncodeType):  # String
		self.add_query_param('EncodeType', EncodeType)
	def get_KeyValue(self): # String
		return self.get_query_params().get('KeyValue')

	def set_KeyValue(self, KeyValue):  # String
		self.add_query_param('KeyValue', KeyValue)
	def get_TokenPass(self): # Boolean
		return self.get_query_params().get('TokenPass')

	def set_TokenPass(self, TokenPass):  # Boolean
		self.add_query_param('TokenPass', TokenPass)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_TokenName(self): # String
		return self.get_query_params().get('TokenName')

	def set_TokenName(self, TokenName):  # String
		self.add_query_param('TokenName', TokenName)
