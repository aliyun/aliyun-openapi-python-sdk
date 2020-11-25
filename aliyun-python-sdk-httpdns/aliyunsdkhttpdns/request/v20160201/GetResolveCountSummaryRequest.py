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

class GetResolveCountSummaryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Httpdns', '2016-02-01', 'GetResolveCountSummary')
		self.set_method('POST')

	def get_TimeSpan(self):
		return self.get_query_params().get('TimeSpan')

	def set_TimeSpan(self,TimeSpan):
		self.add_query_param('TimeSpan',TimeSpan)

	def get_Granularity(self):
		return self.get_query_params().get('Granularity')

	def set_Granularity(self,Granularity):
		self.add_query_param('Granularity',Granularity)