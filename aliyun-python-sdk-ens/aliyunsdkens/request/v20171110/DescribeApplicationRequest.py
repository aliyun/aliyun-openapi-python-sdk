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

class DescribeApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeApplication','ens')
		self.set_method('POST')

	def get_ResourceSelector(self): # String
		return self.get_query_params().get('ResourceSelector')

	def set_ResourceSelector(self, ResourceSelector):  # String
		self.add_query_param('ResourceSelector', ResourceSelector)
	def get_AppVersions(self): # String
		return self.get_query_params().get('AppVersions')

	def set_AppVersions(self, AppVersions):  # String
		self.add_query_param('AppVersions', AppVersions)
	def get_OutDetailStatParams(self): # String
		return self.get_query_params().get('OutDetailStatParams')

	def set_OutDetailStatParams(self, OutDetailStatParams):  # String
		self.add_query_param('OutDetailStatParams', OutDetailStatParams)
	def get_Level(self): # String
		return self.get_query_params().get('Level')

	def set_Level(self, Level):  # String
		self.add_query_param('Level', Level)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
