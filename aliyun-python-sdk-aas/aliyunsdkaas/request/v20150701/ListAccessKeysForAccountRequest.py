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
class ListAccessKeysForAccountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Aas', '2015-07-01', 'ListAccessKeysForAccount')

	def get_PK(self):
		return self.get_query_params().get('PK')

	def set_PK(self,PK):
		self.add_query_param('PK',PK)

	def get_AKStatus(self):
		return self.get_query_params().get('AKStatus')

	def set_AKStatus(self,AKStatus):
		self.add_query_param('AKStatus',AKStatus)

	def get_AKType(self):
		return self.get_query_params().get('AKType')

	def set_AKType(self,AKType):
		self.add_query_param('AKType',AKType)