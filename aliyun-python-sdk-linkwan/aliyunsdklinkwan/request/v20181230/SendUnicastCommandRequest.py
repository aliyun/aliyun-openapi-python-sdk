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
class SendUnicastCommandRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'SendUnicastCommand','linkwan')

	def get_DevEui(self):
		return self.get_body_params().get('DevEui')

	def set_DevEui(self,DevEui):
		self.add_body_params('DevEui', DevEui)

	def get_MaxRetries(self):
		return self.get_body_params().get('MaxRetries')

	def set_MaxRetries(self,MaxRetries):
		self.add_body_params('MaxRetries', MaxRetries)

	def get_CleanUp(self):
		return self.get_body_params().get('CleanUp')

	def set_CleanUp(self,CleanUp):
		self.add_body_params('CleanUp', CleanUp)

	def get_FPort(self):
		return self.get_body_params().get('FPort')

	def set_FPort(self,FPort):
		self.add_body_params('FPort', FPort)

	def get_Comfirmed(self):
		return self.get_body_params().get('Comfirmed')

	def set_Comfirmed(self,Comfirmed):
		self.add_body_params('Comfirmed', Comfirmed)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)