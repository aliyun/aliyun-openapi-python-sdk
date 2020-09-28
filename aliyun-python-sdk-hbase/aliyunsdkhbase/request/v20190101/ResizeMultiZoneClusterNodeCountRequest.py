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
from aliyunsdkhbase.endpoint import endpoint_data

class ResizeMultiZoneClusterNodeCountRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'ResizeMultiZoneClusterNodeCount','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PrimaryVSwitchId(self):
		return self.get_query_params().get('PrimaryVSwitchId')

	def set_PrimaryVSwitchId(self,PrimaryVSwitchId):
		self.add_query_param('PrimaryVSwitchId',PrimaryVSwitchId)

	def get_StandbyVSwitchId(self):
		return self.get_query_params().get('StandbyVSwitchId')

	def set_StandbyVSwitchId(self,StandbyVSwitchId):
		self.add_query_param('StandbyVSwitchId',StandbyVSwitchId)

	def get_LogNodeCount(self):
		return self.get_query_params().get('LogNodeCount')

	def set_LogNodeCount(self,LogNodeCount):
		self.add_query_param('LogNodeCount',LogNodeCount)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_PrimaryCoreNodeCount(self):
		return self.get_query_params().get('PrimaryCoreNodeCount')

	def set_PrimaryCoreNodeCount(self,PrimaryCoreNodeCount):
		self.add_query_param('PrimaryCoreNodeCount',PrimaryCoreNodeCount)

	def get_CoreNodeCount(self):
		return self.get_query_params().get('CoreNodeCount')

	def set_CoreNodeCount(self,CoreNodeCount):
		self.add_query_param('CoreNodeCount',CoreNodeCount)

	def get_StandbyCoreNodeCount(self):
		return self.get_query_params().get('StandbyCoreNodeCount')

	def set_StandbyCoreNodeCount(self,StandbyCoreNodeCount):
		self.add_query_param('StandbyCoreNodeCount',StandbyCoreNodeCount)

	def get_ArbiterVSwitchId(self):
		return self.get_query_params().get('ArbiterVSwitchId')

	def set_ArbiterVSwitchId(self,ArbiterVSwitchId):
		self.add_query_param('ArbiterVSwitchId',ArbiterVSwitchId)