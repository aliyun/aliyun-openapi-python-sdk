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
from aliyunsdkbaas.endpoint import endpoint_data

class CreateOwnAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateOwnAccount')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Identity(self):
		return self.get_body_params().get('Identity')

	def set_Identity(self,Identity):
		self.add_body_params('Identity', Identity)

	def get_Bizid(self):
		return self.get_body_params().get('Bizid')

	def set_Bizid(self,Bizid):
		self.add_body_params('Bizid', Bizid)

	def get_PublicKey(self):
		return self.get_body_params().get('PublicKey')

	def set_PublicKey(self,PublicKey):
		self.add_body_params('PublicKey', PublicKey)

	def get_RecoveryKey(self):
		return self.get_body_params().get('RecoveryKey')

	def set_RecoveryKey(self,RecoveryKey):
		self.add_body_params('RecoveryKey', RecoveryKey)