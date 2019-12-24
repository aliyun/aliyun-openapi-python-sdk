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

class PopUpQueryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-07', 'PopUpQuery')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OptionType(self):
		return self.get_body_params().get('OptionType')

	def set_OptionType(self,OptionType):
		self.add_body_params('OptionType', OptionType)

	def get_Extra(self):
		return self.get_body_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_body_params('Extra', Extra)

	def get_UrlId(self):
		return self.get_body_params().get('UrlId')

	def set_UrlId(self,UrlId):
		self.add_body_params('UrlId', UrlId)

	def get_AlipayOpenId(self):
		return self.get_body_params().get('AlipayOpenId')

	def set_AlipayOpenId(self,AlipayOpenId):
		self.add_body_params('AlipayOpenId', AlipayOpenId)

	def get_ChannelId(self):
		return self.get_body_params().get('ChannelId')

	def set_ChannelId(self,ChannelId):
		self.add_body_params('ChannelId', ChannelId)

	def get_OuterCode(self):
		return self.get_body_params().get('OuterCode')

	def set_OuterCode(self,OuterCode):
		self.add_body_params('OuterCode', OuterCode)