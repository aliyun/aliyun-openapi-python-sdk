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

class AllocateEipAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'AllocateEipAddress','ens')
		self.set_method('POST')

	def get_MinCount(self):
		return self.get_query_params().get('MinCount')

	def set_MinCount(self,MinCount):
		self.add_query_param('MinCount',MinCount)

	def get_EnsRegionId(self):
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self,EnsRegionId):
		self.add_query_param('EnsRegionId',EnsRegionId)

	def get_Count(self):
		return self.get_query_params().get('Count')

	def set_Count(self,Count):
		self.add_query_param('Count',Count)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)