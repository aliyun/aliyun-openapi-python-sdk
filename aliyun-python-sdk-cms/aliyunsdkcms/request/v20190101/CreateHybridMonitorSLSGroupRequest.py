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

class CreateHybridMonitorSLSGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'CreateHybridMonitorSLSGroup','cms')
		self.set_method('POST')

	def get_SLSGroupDescription(self): # String
		return self.get_query_params().get('SLSGroupDescription')

	def set_SLSGroupDescription(self, SLSGroupDescription):  # String
		self.add_query_param('SLSGroupDescription', SLSGroupDescription)
	def get_SLSGroupConfigs(self): # RepeatList
		return self.get_query_params().get('SLSGroupConfig')

	def set_SLSGroupConfigs(self, SLSGroupConfig):  # RepeatList
		for depth1 in range(len(SLSGroupConfig)):
			if SLSGroupConfig[depth1].get('SLSLogstore') is not None:
				self.add_query_param('SLSGroupConfig.' + str(depth1 + 1) + '.SLSLogstore', SLSGroupConfig[depth1].get('SLSLogstore'))
			if SLSGroupConfig[depth1].get('SLSUserId') is not None:
				self.add_query_param('SLSGroupConfig.' + str(depth1 + 1) + '.SLSUserId', SLSGroupConfig[depth1].get('SLSUserId'))
			if SLSGroupConfig[depth1].get('SLSProject') is not None:
				self.add_query_param('SLSGroupConfig.' + str(depth1 + 1) + '.SLSProject', SLSGroupConfig[depth1].get('SLSProject'))
			if SLSGroupConfig[depth1].get('SLSRegion') is not None:
				self.add_query_param('SLSGroupConfig.' + str(depth1 + 1) + '.SLSRegion', SLSGroupConfig[depth1].get('SLSRegion'))
	def get_SLSGroupName(self): # String
		return self.get_query_params().get('SLSGroupName')

	def set_SLSGroupName(self, SLSGroupName):  # String
		self.add_query_param('SLSGroupName', SLSGroupName)
