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

class AddCasterEpisodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddCasterEpisode','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EpisodeName(self): # String
		return self.get_query_params().get('EpisodeName')

	def set_EpisodeName(self, EpisodeName):  # String
		self.add_query_param('EpisodeName', EpisodeName)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_ComponentIds(self): # RepeatList
		return self.get_query_params().get('ComponentId')

	def set_ComponentIds(self, ComponentId):  # RepeatList
		for depth1 in range(len(ComponentId)):
			self.add_query_param('ComponentId.' + str(depth1 + 1), ComponentId[depth1])
	def get_CasterId(self): # String
		return self.get_query_params().get('CasterId')

	def set_CasterId(self, CasterId):  # String
		self.add_query_param('CasterId', CasterId)
	def get_EpisodeType(self): # String
		return self.get_query_params().get('EpisodeType')

	def set_EpisodeType(self, EpisodeType):  # String
		self.add_query_param('EpisodeType', EpisodeType)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_SwitchType(self): # String
		return self.get_query_params().get('SwitchType')

	def set_SwitchType(self, SwitchType):  # String
		self.add_query_param('SwitchType', SwitchType)
