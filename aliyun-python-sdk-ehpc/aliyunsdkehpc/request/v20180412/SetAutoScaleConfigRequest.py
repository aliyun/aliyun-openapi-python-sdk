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
class SetAutoScaleConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'SetAutoScaleConfig','ehs')

	def get_ShrinkIdleTimes(self):
		return self.get_query_params().get('ShrinkIdleTimes')

	def set_ShrinkIdleTimes(self,ShrinkIdleTimes):
		self.add_query_param('ShrinkIdleTimes',ShrinkIdleTimes)

	def get_GrowTimeoutInMinutes(self):
		return self.get_query_params().get('GrowTimeoutInMinutes')

	def set_GrowTimeoutInMinutes(self,GrowTimeoutInMinutes):
		self.add_query_param('GrowTimeoutInMinutes',GrowTimeoutInMinutes)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_EnableAutoGrow(self):
		return self.get_query_params().get('EnableAutoGrow')

	def set_EnableAutoGrow(self,EnableAutoGrow):
		self.add_query_param('EnableAutoGrow',EnableAutoGrow)

	def get_EnableAutoShrink(self):
		return self.get_query_params().get('EnableAutoShrink')

	def set_EnableAutoShrink(self,EnableAutoShrink):
		self.add_query_param('EnableAutoShrink',EnableAutoShrink)

	def get_MaxNodesInCluster(self):
		return self.get_query_params().get('MaxNodesInCluster')

	def set_MaxNodesInCluster(self,MaxNodesInCluster):
		self.add_query_param('MaxNodesInCluster',MaxNodesInCluster)

	def get_ExcludeNodes(self):
		return self.get_query_params().get('ExcludeNodes')

	def set_ExcludeNodes(self,ExcludeNodes):
		self.add_query_param('ExcludeNodes',ExcludeNodes)

	def get_ShrinkIntervalInMinutes(self):
		return self.get_query_params().get('ShrinkIntervalInMinutes')

	def set_ShrinkIntervalInMinutes(self,ShrinkIntervalInMinutes):
		self.add_query_param('ShrinkIntervalInMinutes',ShrinkIntervalInMinutes)

	def get_ExtraNodesGrowRatio(self):
		return self.get_query_params().get('ExtraNodesGrowRatio')

	def set_ExtraNodesGrowRatio(self,ExtraNodesGrowRatio):
		self.add_query_param('ExtraNodesGrowRatio',ExtraNodesGrowRatio)

	def get_GrowIntervalInMinutes(self):
		return self.get_query_params().get('GrowIntervalInMinutes')

	def set_GrowIntervalInMinutes(self,GrowIntervalInMinutes):
		self.add_query_param('GrowIntervalInMinutes',GrowIntervalInMinutes)

	def get_GrowRatio(self):
		return self.get_query_params().get('GrowRatio')

	def set_GrowRatio(self,GrowRatio):
		self.add_query_param('GrowRatio',GrowRatio)