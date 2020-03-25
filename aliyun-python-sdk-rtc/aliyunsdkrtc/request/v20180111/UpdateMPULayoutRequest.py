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
from aliyunsdkrtc.endpoint import endpoint_data

class UpdateMPULayoutRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'UpdateMPULayout','rtc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UserPaness(self):
		return self.get_query_params().get('UserPaness')

	def set_UserPaness(self,UserPaness):
		for i in range(len(UserPaness)):	
			if UserPaness[i].get('PaneId') is not None:
				self.add_query_param('UserPanes.' + str(i + 1) + '.PaneId' , UserPaness[i].get('PaneId'))
			if UserPaness[i].get('UserId') is not None:
				self.add_query_param('UserPanes.' + str(i + 1) + '.UserId' , UserPaness[i].get('UserId'))
			if UserPaness[i].get('SourceType') is not None:
				self.add_query_param('UserPanes.' + str(i + 1) + '.SourceType' , UserPaness[i].get('SourceType'))


	def get_BackgroundColor(self):
		return self.get_query_params().get('BackgroundColor')

	def set_BackgroundColor(self,BackgroundColor):
		self.add_query_param('BackgroundColor',BackgroundColor)

	def get_CropMode(self):
		return self.get_query_params().get('CropMode')

	def set_CropMode(self,CropMode):
		self.add_query_param('CropMode',CropMode)

	def get_LayoutIdss(self):
		return self.get_query_params().get('LayoutIdss')

	def set_LayoutIdss(self,LayoutIdss):
		for i in range(len(LayoutIdss)):	
			if LayoutIdss[i] is not None:
				self.add_query_param('LayoutIds.' + str(i + 1) , LayoutIdss[i]);

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)