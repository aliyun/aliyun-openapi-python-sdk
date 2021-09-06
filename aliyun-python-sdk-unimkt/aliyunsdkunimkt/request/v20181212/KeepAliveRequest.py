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
from aliyunsdkunimkt.endpoint import endpoint_data

class KeepAliveRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'KeepAlive')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Tac(self):
		return self.get_body_params().get('Tac')

	def set_Tac(self,Tac):
		self.add_body_params('Tac', Tac)

	def get_NetworkType(self):
		return self.get_body_params().get('NetworkType')

	def set_NetworkType(self,NetworkType):
		self.add_body_params('NetworkType', NetworkType)

	def get_CellId(self):
		return self.get_body_params().get('CellId')

	def set_CellId(self,CellId):
		self.add_body_params('CellId', CellId)

	def get_DeviceSn(self):
		return self.get_body_params().get('DeviceSn')

	def set_DeviceSn(self,DeviceSn):
		self.add_body_params('DeviceSn', DeviceSn)

	def get_ChannelId(self):
		return self.get_body_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_body_params('ChannelId', ChannelId)