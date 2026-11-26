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

class RerankRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'Rerank','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TopK(self): # Integer
		return self.get_body_params().get('TopK')

	def set_TopK(self, TopK):  # Integer
		self.add_body_params('TopK', TopK)
	def get_Documents(self): # Array
		return self.get_body_params().get('Documents')

	def set_Documents(self, Documents):  # Array
		self.add_body_params("Documents", json.dumps(Documents))
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_Model(self): # String
		return self.get_body_params().get('Model')

	def set_Model(self, Model):  # String
		self.add_body_params('Model', Model)
	def get_ReturnDocuments(self): # Boolean
		return self.get_body_params().get('ReturnDocuments')

	def set_ReturnDocuments(self, ReturnDocuments):  # Boolean
		self.add_body_params('ReturnDocuments', ReturnDocuments)
	def get_Instruct(self): # String
		return self.get_body_params().get('Instruct')

	def set_Instruct(self, Instruct):  # String
		self.add_body_params('Instruct', Instruct)
	def get_Query(self): # String
		return self.get_body_params().get('Query')

	def set_Query(self, Query):  # String
		self.add_body_params('Query', Query)
	def get_MaxChunksPerDoc(self): # Integer
		return self.get_body_params().get('MaxChunksPerDoc')

	def set_MaxChunksPerDoc(self, MaxChunksPerDoc):  # Integer
		self.add_body_params('MaxChunksPerDoc', MaxChunksPerDoc)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
