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
class EditEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'EditEvent','cloudphoto')
		self.set_protocol_type('https');

	def get_EventId(self):
		return self.get_query_params().get('EventId')

	def set_EventId(self,EventId):
		self.add_query_param('EventId',EventId)

	def get_BannerPhotoId(self):
		return self.get_query_params().get('BannerPhotoId')

	def set_BannerPhotoId(self,BannerPhotoId):
		self.add_query_param('BannerPhotoId',BannerPhotoId)

	def get_WatermarkPhotoId(self):
		return self.get_query_params().get('WatermarkPhotoId')

	def set_WatermarkPhotoId(self,WatermarkPhotoId):
		self.add_query_param('WatermarkPhotoId',WatermarkPhotoId)

	def get_SplashPhotoId(self):
		return self.get_query_params().get('SplashPhotoId')

	def set_SplashPhotoId(self,SplashPhotoId):
		self.add_query_param('SplashPhotoId',SplashPhotoId)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_WeixinTitle(self):
		return self.get_query_params().get('WeixinTitle')

	def set_WeixinTitle(self,WeixinTitle):
		self.add_query_param('WeixinTitle',WeixinTitle)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_EndAt(self):
		return self.get_query_params().get('EndAt')

	def set_EndAt(self,EndAt):
		self.add_query_param('EndAt',EndAt)

	def get_StartAt(self):
		return self.get_query_params().get('StartAt')

	def set_StartAt(self,StartAt):
		self.add_query_param('StartAt',StartAt)