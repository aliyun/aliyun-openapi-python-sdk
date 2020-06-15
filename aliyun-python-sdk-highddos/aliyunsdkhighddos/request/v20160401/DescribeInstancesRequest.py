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

class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HighDDos', '2016-04-01', 'DescribeInstances')
		self.set_method('POST')

	def get_ContainDomain(self):
		return self.get_query_params().get('ContainDomain')

	def set_ContainDomain(self,ContainDomain):
		self.add_query_param('ContainDomain',ContainDomain)

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_ContainDetail(self):
		return self.get_query_params().get('ContainDetail')

	def set_ContainDetail(self,ContainDetail):
		self.add_query_param('ContainDetail',ContainDetail)