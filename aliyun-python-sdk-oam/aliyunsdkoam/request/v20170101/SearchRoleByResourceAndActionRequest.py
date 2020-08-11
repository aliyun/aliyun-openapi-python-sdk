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

class SearchRoleByResourceAndActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Oam', '2017-01-01', 'SearchRoleByResourceAndAction')
		self.set_method('POST')

	def get_ResourceActions(self):
		return self.get_query_params().get('ResourceActions')

	def set_ResourceActions(self, ResourceActions):
		for depth1 in range(len(ResourceActions)):
			if ResourceActions[depth1].get('Resource') is not None:
				self.add_query_param('ResourceAction.' + str(depth1 + 1) + '.Resource', ResourceActions[depth1].get('Resource'))
			if ResourceActions[depth1].get('ActionField') is not None:
				self.add_query_param('ResourceAction.' + str(depth1 + 1) + '.ActionField', ResourceActions[depth1].get('ActionField'))