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

class AddTagMiddleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Oam', '2017-01-01', 'AddTagMiddle')
		self.set_method('POST')

	def get_MutexTagMiddles(self):
		return self.get_query_params().get('MutexTagMiddles')

	def set_MutexTagMiddles(self, MutexTagMiddles):
		for depth1 in range(len(MutexTagMiddles)):
			if MutexTagMiddles[depth1].get('TagId') is not None:
				self.add_query_param('MutexTagMiddle.' + str(depth1 + 1) + '.TagId', MutexTagMiddles[depth1].get('TagId'))
			if MutexTagMiddles[depth1].get('RoleCellId') is not None:
				self.add_query_param('MutexTagMiddle.' + str(depth1 + 1) + '.RoleCellId', MutexTagMiddles[depth1].get('RoleCellId'))
			if MutexTagMiddles[depth1].get('Type') is not None:
				self.add_query_param('MutexTagMiddle.' + str(depth1 + 1) + '.Type', MutexTagMiddles[depth1].get('Type'))

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)