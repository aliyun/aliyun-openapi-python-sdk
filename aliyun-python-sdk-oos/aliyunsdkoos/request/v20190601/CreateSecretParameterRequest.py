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
from aliyunsdkoos.endpoint import endpoint_data
import json

class CreateSecretParameterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'CreateSecretParameter','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Constraints(self): # String
		return self.get_query_params().get('Constraints')

	def set_Constraints(self, Constraints):  # String
		self.add_query_param('Constraints', Constraints)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DKMSInstanceId(self): # String
		return self.get_query_params().get('DKMSInstanceId')

	def set_DKMSInstanceId(self, DKMSInstanceId):  # String
		self.add_query_param('DKMSInstanceId', DKMSInstanceId)
	def get_Value(self): # String
		return self.get_query_params().get('Value')

	def set_Value(self, Value):  # String
		self.add_query_param('Value', Value)
	def get_KeyId(self): # String
		return self.get_query_params().get('KeyId')

	def set_KeyId(self, KeyId):  # String
		self.add_query_param('KeyId', KeyId)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
