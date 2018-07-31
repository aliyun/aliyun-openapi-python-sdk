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
class MoPenQueryCanvasRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'MoPen', '2018-02-11', 'MoPenQueryCanvas')
		self.set_protocol_type('https');
		self.set_method('POST')

	def get_DeviceName(self):
		return self.get_body_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_body_params('DeviceName', DeviceName)

	def get_SessionId(self):
		return self.get_body_params().get('SessionId')

	def set_SessionId(self,SessionId):
		self.add_body_params('SessionId', SessionId)

	def get_PageId(self):
		return self.get_body_params().get('PageId')

	def set_PageId(self,PageId):
		self.add_body_params('PageId', PageId)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)