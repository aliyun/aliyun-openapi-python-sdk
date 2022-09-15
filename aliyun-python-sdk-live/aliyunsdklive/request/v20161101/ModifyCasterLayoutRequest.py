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

class ModifyCasterLayoutRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyCasterLayout','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BlendLists(self): # RepeatList
		return self.get_query_params().get('BlendList')

	def set_BlendLists(self, BlendList):  # RepeatList
		for depth1 in range(len(BlendList)):
			self.add_query_param('BlendList.' + str(depth1 + 1), BlendList[depth1])
	def get_LayoutId(self): # String
		return self.get_query_params().get('LayoutId')

	def set_LayoutId(self, LayoutId):  # String
		self.add_query_param('LayoutId', LayoutId)
	def get_CasterId(self): # String
		return self.get_query_params().get('CasterId')

	def set_CasterId(self, CasterId):  # String
		self.add_query_param('CasterId', CasterId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_AudioLayers(self): # RepeatList
		return self.get_query_params().get('AudioLayer')

	def set_AudioLayers(self, AudioLayer):  # RepeatList
		for depth1 in range(len(AudioLayer)):
			if AudioLayer[depth1].get('VolumeRate') is not None:
				self.add_query_param('AudioLayer.' + str(depth1 + 1) + '.VolumeRate', AudioLayer[depth1].get('VolumeRate'))
			if AudioLayer[depth1].get('FixedDelayDuration') is not None:
				self.add_query_param('AudioLayer.' + str(depth1 + 1) + '.FixedDelayDuration', AudioLayer[depth1].get('FixedDelayDuration'))
			if AudioLayer[depth1].get('ValidChannel') is not None:
				self.add_query_param('AudioLayer.' + str(depth1 + 1) + '.ValidChannel', AudioLayer[depth1].get('ValidChannel'))
	def get_VideoLayers(self): # RepeatList
		return self.get_query_params().get('VideoLayer')

	def set_VideoLayers(self, VideoLayer):  # RepeatList
		for depth1 in range(len(VideoLayer)):
			if VideoLayer[depth1].get('FixedDelayDuration') is not None:
				self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.FixedDelayDuration', VideoLayer[depth1].get('FixedDelayDuration'))
			if VideoLayer[depth1].get('FillMode') is not None:
				self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.FillMode', VideoLayer[depth1].get('FillMode'))
			if VideoLayer[depth1].get('HeightNormalized') is not None:
				self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.HeightNormalized', VideoLayer[depth1].get('HeightNormalized'))
			if VideoLayer[depth1].get('PositionRefer') is not None:
				self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.PositionRefer', VideoLayer[depth1].get('PositionRefer'))
			if VideoLayer[depth1].get('PositionNormalized') is not None:
				for depth2 in range(len(VideoLayer[depth1].get('PositionNormalized'))):
					self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.PositionNormalized.' + str(depth2 + 1), VideoLayer[depth1].get('PositionNormalized')[depth2])
			if VideoLayer[depth1].get('WidthNormalized') is not None:
				self.add_query_param('VideoLayer.' + str(depth1 + 1) + '.WidthNormalized', VideoLayer[depth1].get('WidthNormalized'))
	def get_MixLists(self): # RepeatList
		return self.get_query_params().get('MixList')

	def set_MixLists(self, MixList):  # RepeatList
		for depth1 in range(len(MixList)):
			self.add_query_param('MixList.' + str(depth1 + 1), MixList[depth1])
