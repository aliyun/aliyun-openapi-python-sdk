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

class UpdateAutomateResponseConfigStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'UpdateAutomateResponseConfigStatus','cloud-siem')
		self.set_method('POST')

	def get_Ids(self): # String
		return self.get_body_params().get('Ids')

	def set_Ids(self, Ids):  # String
		self.add_body_params('Ids', Ids)
	def get_InUse(self): # Boolean
		return self.get_body_params().get('InUse')

	def set_InUse(self, InUse):  # Boolean
		self.add_body_params('InUse', InUse)
