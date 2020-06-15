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

class SyncCrowdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudmarketing', '2018-09-10', 'SyncCrowd')
		self.set_method('POST')

	def get_OuterAccountNo(self):
		return self.get_query_params().get('OuterAccountNo')

	def set_OuterAccountNo(self,OuterAccountNo):
		self.add_query_param('OuterAccountNo',OuterAccountNo)

	def get_CrowdId(self):
		return self.get_query_params().get('CrowdId')

	def set_CrowdId(self,CrowdId):
		self.add_query_param('CrowdId',CrowdId)

	def get_ChannelBrandss(self):
		return self.get_query_params().get('ChannelBrandss')

	def set_ChannelBrandss(self, ChannelBrandss):
		for depth1 in range(len(ChannelBrandss)):
			if ChannelBrandss[depth1].get('OuterBrandId') is not None:
				self.add_query_param('ChannelBrands.' + str(depth1 + 1) + '.OuterBrandId', ChannelBrandss[depth1].get('OuterBrandId'))
			if ChannelBrandss[depth1].get('OuterBrandName') is not None:
				self.add_query_param('ChannelBrands.' + str(depth1 + 1) + '.OuterBrandName', ChannelBrandss[depth1].get('OuterBrandName'))

	def get_ChannelType(self):
		return self.get_query_params().get('ChannelType')

	def set_ChannelType(self,ChannelType):
		self.add_query_param('ChannelType',ChannelType)