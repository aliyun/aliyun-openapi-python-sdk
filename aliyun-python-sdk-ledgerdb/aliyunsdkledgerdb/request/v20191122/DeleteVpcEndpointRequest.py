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

class DeleteVpcEndpointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ledgerdb', '2019-11-22', 'DeleteVpcEndpoint','ledgerdb')
		self.set_method('POST')

	def get_LedgerId(self):
		return self.get_query_params().get('LedgerId')

	def set_LedgerId(self,LedgerId):
		self.add_query_param('LedgerId',LedgerId)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_VpcEndpointId(self):
		return self.get_query_params().get('VpcEndpointId')

	def set_VpcEndpointId(self,VpcEndpointId):
		self.add_query_param('VpcEndpointId',VpcEndpointId)