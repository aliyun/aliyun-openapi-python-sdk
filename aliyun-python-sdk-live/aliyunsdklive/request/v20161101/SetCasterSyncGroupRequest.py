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
from aliyunsdklive.endpoint import endpoint_data

class SetCasterSyncGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SetCasterSyncGroup','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CasterId(self): # String
		return self.get_query_params().get('CasterId')

	def set_CasterId(self, CasterId):  # String
		self.add_query_param('CasterId', CasterId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SyncGroups(self): # RepeatList
		return self.get_query_params().get('SyncGroup')

	def set_SyncGroups(self, SyncGroup):  # RepeatList
		for depth1 in range(len(SyncGroup)):
			if SyncGroup[depth1].get('HostResourceId') is not None:
				self.add_query_param('SyncGroup.' + str(depth1 + 1) + '.HostResourceId', SyncGroup[depth1].get('HostResourceId'))
			if SyncGroup[depth1].get('ResourceIds') is not None:
				for depth2 in range(len(SyncGroup[depth1].get('ResourceIds'))):
					self.add_query_param('SyncGroup.' + str(depth1 + 1) + '.ResourceIds.' + str(depth2 + 1), SyncGroup[depth1].get('ResourceIds')[depth2])
			if SyncGroup[depth1].get('SyncOffsets') is not None:
				for depth2 in range(len(SyncGroup[depth1].get('SyncOffsets'))):
					self.add_query_param('SyncGroup.' + str(depth1 + 1) + '.SyncOffsets.' + str(depth2 + 1), SyncGroup[depth1].get('SyncOffsets')[depth2])
			if SyncGroup[depth1].get('SyncDelayThreshold') is not None:
				self.add_query_param('SyncGroup.' + str(depth1 + 1) + '.SyncDelayThreshold', SyncGroup[depth1].get('SyncDelayThreshold'))
			if SyncGroup[depth1].get('Mode') is not None:
				self.add_query_param('SyncGroup.' + str(depth1 + 1) + '.Mode', SyncGroup[depth1].get('Mode'))
