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
from aliyunsdkkms.endpoint import endpoint_data

class AdvanceEncryptRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Kms', '2016-01-20', 'AdvanceEncrypt','kms')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PaddingMode(self): # String
		return self.get_query_params().get('PaddingMode')

	def set_PaddingMode(self, PaddingMode):  # String
		self.add_query_param('PaddingMode', PaddingMode)
	def get_Aad(self): # String
		return self.get_query_params().get('Aad')

	def set_Aad(self, Aad):  # String
		self.add_query_param('Aad', Aad)
	def get_KeyId(self): # String
		return self.get_query_params().get('KeyId')

	def set_KeyId(self, KeyId):  # String
		self.add_query_param('KeyId', KeyId)
	def get_Plaintext(self): # String
		return self.get_query_params().get('Plaintext')

	def set_Plaintext(self, Plaintext):  # String
		self.add_query_param('Plaintext', Plaintext)
	def get_Iv(self): # String
		return self.get_query_params().get('Iv')

	def set_Iv(self, Iv):  # String
		self.add_query_param('Iv', Iv)
	def get_Algorithm(self): # String
		return self.get_query_params().get('Algorithm')

	def set_Algorithm(self, Algorithm):  # String
		self.add_query_param('Algorithm', Algorithm)
