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
from aliyunsdkehpc.endpoint import endpoint_data

class SetAutoScaleConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2017-07-14', 'SetAutoScaleConfig')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExcludeNodes(self): # String
		return self.get_query_params().get('ExcludeNodes')

	def set_ExcludeNodes(self, ExcludeNodes):  # String
		self.add_query_param('ExcludeNodes', ExcludeNodes)
	def get_ExtraNodesGrowRatio(self): # Integer
		return self.get_query_params().get('ExtraNodesGrowRatio')

	def set_ExtraNodesGrowRatio(self, ExtraNodesGrowRatio):  # Integer
		self.add_query_param('ExtraNodesGrowRatio', ExtraNodesGrowRatio)
	def get_ShrinkIdleTimes(self): # Integer
		return self.get_query_params().get('ShrinkIdleTimes')

	def set_ShrinkIdleTimes(self, ShrinkIdleTimes):  # Integer
		self.add_query_param('ShrinkIdleTimes', ShrinkIdleTimes)
	def get_GrowTimeoutInMinutes(self): # Integer
		return self.get_query_params().get('GrowTimeoutInMinutes')

	def set_GrowTimeoutInMinutes(self, GrowTimeoutInMinutes):  # Integer
		self.add_query_param('GrowTimeoutInMinutes', GrowTimeoutInMinutes)
	def get_ClusterId(self): # String
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_query_param('ClusterId', ClusterId)
	def get_EnableAutoGrow(self): # Boolean
		return self.get_query_params().get('EnableAutoGrow')

	def set_EnableAutoGrow(self, EnableAutoGrow):  # Boolean
		self.add_query_param('EnableAutoGrow', EnableAutoGrow)
	def get_EnableAutoShrink(self): # Boolean
		return self.get_query_params().get('EnableAutoShrink')

	def set_EnableAutoShrink(self, EnableAutoShrink):  # Boolean
		self.add_query_param('EnableAutoShrink', EnableAutoShrink)
	def get_MaxNodesInCluster(self): # Integer
		return self.get_query_params().get('MaxNodesInCluster')

	def set_MaxNodesInCluster(self, MaxNodesInCluster):  # Integer
		self.add_query_param('MaxNodesInCluster', MaxNodesInCluster)
	def get_ShrinkIntervalInMinutes(self): # Integer
		return self.get_query_params().get('ShrinkIntervalInMinutes')

	def set_ShrinkIntervalInMinutes(self, ShrinkIntervalInMinutes):  # Integer
		self.add_query_param('ShrinkIntervalInMinutes', ShrinkIntervalInMinutes)
	def get_GrowIntervalInMinutes(self): # Integer
		return self.get_query_params().get('GrowIntervalInMinutes')

	def set_GrowIntervalInMinutes(self, GrowIntervalInMinutes):  # Integer
		self.add_query_param('GrowIntervalInMinutes', GrowIntervalInMinutes)
	def get_GrowRatio(self): # Integer
		return self.get_query_params().get('GrowRatio')

	def set_GrowRatio(self, GrowRatio):  # Integer
		self.add_query_param('GrowRatio', GrowRatio)
