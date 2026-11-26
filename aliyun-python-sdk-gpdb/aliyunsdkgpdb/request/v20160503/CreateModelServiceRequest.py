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
from aliyunsdkgpdb.endpoint import endpoint_data
import json

class CreateModelServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'CreateModelService','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_ModelName(self): # String
		return self.get_query_params().get('ModelName')

	def set_ModelName(self, ModelName):  # String
		self.add_query_param('ModelName', ModelName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_InferenceEngine(self): # String
		return self.get_query_params().get('InferenceEngine')

	def set_InferenceEngine(self, InferenceEngine):  # String
		self.add_query_param('InferenceEngine', InferenceEngine)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_AiNodes(self): # Array
		return self.get_query_params().get('AiNodes')

	def set_AiNodes(self, AiNodes):  # Array
		self.add_query_param("AiNodes", json.dumps(AiNodes))
	def get_Replicas(self): # Integer
		return self.get_query_params().get('Replicas')

	def set_Replicas(self, Replicas):  # Integer
		self.add_query_param('Replicas', Replicas)
	def get_SecurityIPList(self): # String
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self, SecurityIPList):  # String
		self.add_query_param('SecurityIPList', SecurityIPList)
	def get_ModelParams(self): # Map
		return self.get_query_params().get('ModelParams')

	def set_ModelParams(self, ModelParams):  # Map
		self.add_query_param("ModelParams", json.dumps(ModelParams))
	def get_EnablePublicConnection(self): # Boolean
		return self.get_query_params().get('EnablePublicConnection')

	def set_EnablePublicConnection(self, EnablePublicConnection):  # Boolean
		self.add_query_param('EnablePublicConnection', EnablePublicConnection)
