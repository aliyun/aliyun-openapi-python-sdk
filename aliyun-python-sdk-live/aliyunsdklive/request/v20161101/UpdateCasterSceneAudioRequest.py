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
class UpdateCasterSceneAudioRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateCasterSceneAudio','live')

	def get_AudioLayers(self):
		return self.get_query_params().get('AudioLayers')

	def set_AudioLayers(self,AudioLayers):
		for i in range(len(AudioLayers)):	
			if AudioLayers[i].get('FixedDelayDuration') is not None:
				self.add_query_param('AudioLayer.' + str(i + 1) + '.FixedDelayDuration' , AudioLayers[i].get('FixedDelayDuration'))
			if AudioLayers[i].get('VolumeRate') is not None:
				self.add_query_param('AudioLayer.' + str(i + 1) + '.VolumeRate' , AudioLayers[i].get('VolumeRate'))
			if AudioLayers[i].get('ValidChannel') is not None:
				self.add_query_param('AudioLayer.' + str(i + 1) + '.ValidChannel' , AudioLayers[i].get('ValidChannel'))


	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_SceneId(self):
		return self.get_query_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_query_param('SceneId',SceneId)

	def get_MixLists(self):
		return self.get_query_params().get('MixLists')

	def set_MixLists(self,MixLists):
		for i in range(len(MixLists)):	
			if MixLists[i] is not None:
				self.add_query_param('MixList.' + str(i + 1) , MixLists[i]);

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_FollowEnable(self):
		return self.get_query_params().get('FollowEnable')

	def set_FollowEnable(self,FollowEnable):
		self.add_query_param('FollowEnable',FollowEnable)