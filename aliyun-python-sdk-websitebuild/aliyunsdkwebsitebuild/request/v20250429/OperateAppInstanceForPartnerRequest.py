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

class OperateAppInstanceForPartnerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'WebsiteBuild', '2025-04-29', 'OperateAppInstanceForPartner')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Extend(self): # String
		return self.get_query_params().get('Extend')

	def set_Extend(self, Extend):  # String
		self.add_query_param('Extend', Extend)
	def get_OperateEvent(self): # String
		return self.get_query_params().get('OperateEvent')

	def set_OperateEvent(self, OperateEvent):  # String
		self.add_query_param('OperateEvent', OperateEvent)
