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

class QueryUnionPromotionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'QueryUnionPromotion')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UnionBizType(self): # String
		return self.get_query_params().get('UnionBizType')

	def set_UnionBizType(self, UnionBizType):  # String
		self.add_query_param('UnionBizType', UnionBizType)
	def get_ProxyChannelId(self): # String
		return self.get_query_params().get('ProxyChannelId')

	def set_ProxyChannelId(self, ProxyChannelId):  # String
		self.add_query_param('ProxyChannelId', ProxyChannelId)
	def get_UserNick(self): # String
		return self.get_query_params().get('UserNick')

	def set_UserNick(self, UserNick):  # String
		self.add_query_param('UserNick', UserNick)
	def get_Sign(self): # String
		return self.get_query_params().get('Sign')

	def set_Sign(self, Sign):  # String
		self.add_query_param('Sign', Sign)
	def get_AlipayOpenId(self): # Long
		return self.get_query_params().get('AlipayOpenId')

	def set_AlipayOpenId(self, AlipayOpenId):  # Long
		self.add_query_param('AlipayOpenId', AlipayOpenId)
	def get_UserId(self): # Long
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # Long
		self.add_query_param('UserId', UserId)
	def get_ChannelId(self): # String
		return self.get_query_params().get('ChannelId')

	def set_ChannelId(self, ChannelId):  # String
		self.add_query_param('ChannelId', ChannelId)
