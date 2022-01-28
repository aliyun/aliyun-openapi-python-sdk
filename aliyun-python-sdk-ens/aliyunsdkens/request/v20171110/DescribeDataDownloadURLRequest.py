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

class DescribeDataDownloadURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeDataDownloadURL','ens')
		self.set_method('GET')

	def get_ExpireTimeout(self): # Long
		return self.get_query_params().get('ExpireTimeout')

	def set_ExpireTimeout(self, ExpireTimeout):  # Long
		self.add_query_param('ExpireTimeout', ExpireTimeout)
	def get_ServerFilterStrategy(self): # String
		return self.get_query_params().get('ServerFilterStrategy')

	def set_ServerFilterStrategy(self, ServerFilterStrategy):  # String
		self.add_query_param('ServerFilterStrategy', ServerFilterStrategy)
	def get_DataName(self): # String
		return self.get_query_params().get('DataName')

	def set_DataName(self, DataName):  # String
		self.add_query_param('DataName', DataName)
	def get_DataVersion(self): # String
		return self.get_query_params().get('DataVersion')

	def set_DataVersion(self, DataVersion):  # String
		self.add_query_param('DataVersion', DataVersion)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
