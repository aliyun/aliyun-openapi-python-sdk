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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class UpdateControlPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'UpdateControlPolicy','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NewPolicyName(self): # String
		return self.get_query_params().get('NewPolicyName')

	def set_NewPolicyName(self, NewPolicyName):  # String
		self.add_query_param('NewPolicyName', NewPolicyName)
	def get_PolicyId(self): # String
		return self.get_query_params().get('PolicyId')

	def set_PolicyId(self, PolicyId):  # String
		self.add_query_param('PolicyId', PolicyId)
	def get_NewPolicyDocument(self): # String
		return self.get_query_params().get('NewPolicyDocument')

	def set_NewPolicyDocument(self, NewPolicyDocument):  # String
		self.add_query_param('NewPolicyDocument', NewPolicyDocument)
	def get_NewDescription(self): # String
		return self.get_query_params().get('NewDescription')

	def set_NewDescription(self, NewDescription):  # String
		self.add_query_param('NewDescription', NewDescription)
