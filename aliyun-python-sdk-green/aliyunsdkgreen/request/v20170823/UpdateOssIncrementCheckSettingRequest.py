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
class UpdateOssIncrementCheckSettingRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'UpdateOssIncrementCheckSetting','green')

	def get_ImageAutoFreeze(self):
		return self.get_query_params().get('ImageAutoFreeze')

	def set_ImageAutoFreeze(self,ImageAutoFreeze):
		self.add_query_param('ImageAutoFreeze',ImageAutoFreeze)

	def get_VideoSceneList(self):
		return self.get_query_params().get('VideoSceneList')

	def set_VideoSceneList(self,VideoSceneList):
		self.add_query_param('VideoSceneList',VideoSceneList)

	def get_AutoFreezeType(self):
		return self.get_query_params().get('AutoFreezeType')

	def set_AutoFreezeType(self,AutoFreezeType):
		self.add_query_param('AutoFreezeType',AutoFreezeType)

	def get_ImageSceneList(self):
		return self.get_query_params().get('ImageSceneList')

	def set_ImageSceneList(self,ImageSceneList):
		self.add_query_param('ImageSceneList',ImageSceneList)

	def get_BucketConfigList(self):
		return self.get_query_params().get('BucketConfigList')

	def set_BucketConfigList(self,BucketConfigList):
		self.add_query_param('BucketConfigList',BucketConfigList)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ImageScanLimit(self):
		return self.get_query_params().get('ImageScanLimit')

	def set_ImageScanLimit(self,ImageScanLimit):
		self.add_query_param('ImageScanLimit',ImageScanLimit)

	def get_VideoAutoFreezeSceneList(self):
		return self.get_query_params().get('VideoAutoFreezeSceneList')

	def set_VideoAutoFreezeSceneList(self,VideoAutoFreezeSceneList):
		self.add_query_param('VideoAutoFreezeSceneList',VideoAutoFreezeSceneList)

	def get_VideoFrameInterval(self):
		return self.get_query_params().get('VideoFrameInterval')

	def set_VideoFrameInterval(self,VideoFrameInterval):
		self.add_query_param('VideoFrameInterval',VideoFrameInterval)

	def get_VideoMaxSize(self):
		return self.get_query_params().get('VideoMaxSize')

	def set_VideoMaxSize(self,VideoMaxSize):
		self.add_query_param('VideoMaxSize',VideoMaxSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_VideoMaxFrames(self):
		return self.get_query_params().get('VideoMaxFrames')

	def set_VideoMaxFrames(self,VideoMaxFrames):
		self.add_query_param('VideoMaxFrames',VideoMaxFrames)