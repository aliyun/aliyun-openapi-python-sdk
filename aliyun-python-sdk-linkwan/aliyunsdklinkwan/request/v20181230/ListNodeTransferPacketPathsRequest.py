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
class ListNodeTransferPacketPathsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'ListNodeTransferPacketPaths','linkwan')
		self.set_protocol_type('https');

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_DevEui(self):
		return self.get_body_params().get('DevEui')

	def set_DevEui(self,DevEui):
		self.add_body_params('DevEui', DevEui)

	def get_Base64EncodedMacPayload(self):
		return self.get_body_params().get('Base64EncodedMacPayload')

	def set_Base64EncodedMacPayload(self,Base64EncodedMacPayload):
		self.add_body_params('Base64EncodedMacPayload', Base64EncodedMacPayload)

	def get_LogMillis(self):
		return self.get_body_params().get('LogMillis')

	def set_LogMillis(self,LogMillis):
		self.add_body_params('LogMillis', LogMillis)