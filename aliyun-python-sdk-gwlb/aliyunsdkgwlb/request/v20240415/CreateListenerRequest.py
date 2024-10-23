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
from aliyunsdkgwlb.endpoint import endpoint_data

class CreateListenerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Gwlb', '2024-04-15', 'CreateListener','gwlb')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_ServerGroupId(self): # String
		return self.get_body_params().get('ServerGroupId')

	def set_ServerGroupId(self, ServerGroupId):  # String
		self.add_body_params('ServerGroupId', ServerGroupId)
	def get_Tag(self): # Array
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Key') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
			if value1.get('Value') is not None:
				self.add_body_params('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_LoadBalancerId(self): # String
		return self.get_body_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_body_params('LoadBalancerId', LoadBalancerId)
	def get_ListenerDescription(self): # String
		return self.get_body_params().get('ListenerDescription')

	def set_ListenerDescription(self, ListenerDescription):  # String
		self.add_body_params('ListenerDescription', ListenerDescription)
