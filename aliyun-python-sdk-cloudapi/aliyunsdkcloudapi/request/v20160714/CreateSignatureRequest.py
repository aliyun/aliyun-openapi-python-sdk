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
class CreateSignatureRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'CreateSignature','apigateway')

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_SignatureName(self):
		return self.get_query_params().get('SignatureName')

	def set_SignatureName(self,SignatureName):
		self.add_query_param('SignatureName',SignatureName)

	def get_SignatureKey(self):
		return self.get_query_params().get('SignatureKey')

	def set_SignatureKey(self,SignatureKey):
		self.add_query_param('SignatureKey',SignatureKey)

	def get_SignatureSecret(self):
		return self.get_query_params().get('SignatureSecret')

	def set_SignatureSecret(self,SignatureSecret):
		self.add_query_param('SignatureSecret',SignatureSecret)