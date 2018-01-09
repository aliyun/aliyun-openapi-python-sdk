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
class ModifyCasterLayoutRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'ModifyCasterLayout')

	def get_BlendLists(self):
		return self.get_query_params().get('BlendLists')

	def set_BlendLists(self,BlendLists):
		for i in range(len(BlendLists)):	
			if BlendLists[i] is not None:
				self.add_query_param('BlendList.' + bytes(i + 1) , BlendLists[i]);

	def get_AudioLayers(self):
		return self.get_query_params().get('AudioLayers')

	def set_AudioLayers(self,AudioLayers):
		for i in range(len(AudioLayers)):	
			if AudioLayers[i].get('VolumeRate') is not None:
				self.add_query_param('AudioLayer.' + bytes(i + 1) + '.VolumeRate' , AudioLayers[i].get('VolumeRate'))
			if AudioLayers[i].get('ValidChannel') is not None:
				self.add_query_param('AudioLayer.' + bytes(i + 1) + '.ValidChannel' , AudioLayers[i].get('ValidChannel'))


	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_VideoLayers(self):
		return self.get_query_params().get('VideoLayers')

	def set_VideoLayers(self,VideoLayers):
		for i in range(len(VideoLayers)):	
			if VideoLayers[i].get('HeightNormalized') is not None:
				self.add_query_param('VideoLayer.' + bytes(i + 1) + '.HeightNormalized' , VideoLayers[i].get('HeightNormalized'))
			if VideoLayers[i].get('WidthNormalized') is not None:
				self.add_query_param('VideoLayer.' + bytes(i + 1) + '.WidthNormalized' , VideoLayers[i].get('WidthNormalized'))
			if VideoLayers[i].get('PositionRefer') is not None:
				self.add_query_param('VideoLayer.' + bytes(i + 1) + '.PositionRefer' , VideoLayers[i].get('PositionRefer'))
			for j in range(len(VideoLayers[i].get('PositionNormalizeds'))):
				if VideoLayers[i].get('PositionNormalizeds')[j] is not None:
					self.add_query_param('VideoLayer.' + bytes(i + 1) + '.PositionNormalized.'+bytes(j + 1), VideoLayers[i].get('PositionNormalizeds')[j])


	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_MixLists(self):
		return self.get_query_params().get('MixLists')

	def set_MixLists(self,MixLists):
		for i in range(len(MixLists)):	
			if MixLists[i] is not None:
				self.add_query_param('MixList.' + bytes(i + 1) , MixLists[i]);

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_LayoutId(self):
		return self.get_query_params().get('LayoutId')

	def set_LayoutId(self,LayoutId):
		self.add_query_param('LayoutId',LayoutId)