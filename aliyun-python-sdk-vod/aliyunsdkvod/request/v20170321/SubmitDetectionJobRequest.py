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
from aliyunsdkvod.endpoint import endpoint_data

class SubmitDetectionJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SubmitDetectionJob','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_WhiteListUrls(self):
		return self.get_query_params().get('WhiteListUrls')

	def set_WhiteListUrls(self,WhiteListUrls):
		self.add_query_param('WhiteListUrls',WhiteListUrls)

	def get_CopyrightEndTime(self):
		return self.get_query_params().get('CopyrightEndTime')

	def set_CopyrightEndTime(self,CopyrightEndTime):
		self.add_query_param('CopyrightEndTime',CopyrightEndTime)

	def get_CopyrightStatus(self):
		return self.get_query_params().get('CopyrightStatus')

	def set_CopyrightStatus(self,CopyrightStatus):
		self.add_query_param('CopyrightStatus',CopyrightStatus)

	def get_CopyrightBeginTime(self):
		return self.get_query_params().get('CopyrightBeginTime')

	def set_CopyrightBeginTime(self,CopyrightBeginTime):
		self.add_query_param('CopyrightBeginTime',CopyrightBeginTime)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_VideoId(self):
		return self.get_query_params().get('VideoId')

	def set_VideoId(self,VideoId):
		self.add_query_param('VideoId',VideoId)

	def get_BeginTime(self):
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self,BeginTime):
		self.add_query_param('BeginTime',BeginTime)

	def get_ShortVideo(self):
		return self.get_query_params().get('ShortVideo')

	def set_ShortVideo(self,ShortVideo):
		self.add_query_param('ShortVideo',ShortVideo)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_CopyrightFile(self):
		return self.get_query_params().get('CopyrightFile')

	def set_CopyrightFile(self,CopyrightFile):
		self.add_query_param('CopyrightFile',CopyrightFile)