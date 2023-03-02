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

class DescribeEdgeStatInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'lto', '2021-07-07', 'DescribeEdgeStatInfo')
		self.set_method('POST')

	def get_EdgeDn(self): # String
		return self.get_query_params().get('EdgeDn')

	def set_EdgeDn(self, EdgeDn):  # String
		self.add_query_param('EdgeDn', EdgeDn)
	def get_EdgePk(self): # String
		return self.get_query_params().get('EdgePk')

	def set_EdgePk(self, EdgePk):  # String
		self.add_query_param('EdgePk', EdgePk)
