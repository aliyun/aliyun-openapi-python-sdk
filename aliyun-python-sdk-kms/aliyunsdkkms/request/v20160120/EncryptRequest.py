# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class EncryptRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Kms', '2016-01-20', 'Encrypt','kms')

	def get_KeyId(self):
		return self.get_query_params().get('KeyId')

	def set_KeyId(self,KeyId):
		self.add_query_param('KeyId',KeyId)

	def get_Plaintext(self):
		return self.get_query_params().get('Plaintext')

	def set_Plaintext(self,Plaintext):
		self.add_query_param('Plaintext',Plaintext)

	def get_STSToken(self):
		return self.get_query_params().get('STSToken')

	def set_STSToken(self,STSToken):
		self.add_query_param('STSToken',STSToken)

	def get_EncryptionContext(self):
		return self.get_query_params().get('EncryptionContext')

	def set_EncryptionContext(self,EncryptionContext):
		self.add_query_param('EncryptionContext',EncryptionContext)