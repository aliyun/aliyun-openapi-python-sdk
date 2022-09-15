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

class AddCasterProgramRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddCasterProgram','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Episodes(self): # RepeatList
		return self.get_query_params().get('Episode')

	def set_Episodes(self, Episode):  # RepeatList
		for depth1 in range(len(Episode)):
			if Episode[depth1].get('EndTime') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.EndTime', Episode[depth1].get('EndTime'))
			if Episode[depth1].get('StartTime') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.StartTime', Episode[depth1].get('StartTime'))
			if Episode[depth1].get('EpisodeName') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.EpisodeName', Episode[depth1].get('EpisodeName'))
			if Episode[depth1].get('EpisodeType') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.EpisodeType', Episode[depth1].get('EpisodeType'))
			if Episode[depth1].get('ResourceId') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.ResourceId', Episode[depth1].get('ResourceId'))
			if Episode[depth1].get('ComponentId') is not None:
				for depth2 in range(len(Episode[depth1].get('ComponentId'))):
					self.add_query_param('Episode.' + str(depth1 + 1) + '.ComponentId.' + str(depth2 + 1), Episode[depth1].get('ComponentId')[depth2])
			if Episode[depth1].get('SwitchType') is not None:
				self.add_query_param('Episode.' + str(depth1 + 1) + '.SwitchType', Episode[depth1].get('SwitchType'))
	def get_CasterId(self): # String
		return self.get_query_params().get('CasterId')

	def set_CasterId(self, CasterId):  # String
		self.add_query_param('CasterId', CasterId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
