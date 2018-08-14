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
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'Encrypt','ccc')

	def get_PublicKey(self):
		return self.get_query_params().get('PublicKey')

	def set_PublicKey(self,PublicKey):
		self.add_query_param('PublicKey',PublicKey)

	def get_PlainTexts(self):
		return self.get_query_params().get('PlainTexts')

	def set_PlainTexts(self,PlainTexts):
		for i in range(len(PlainTexts)):	
			if PlainTexts[i] is not None:
				self.add_query_param('PlainText.' + str(i + 1) , PlainTexts[i]);