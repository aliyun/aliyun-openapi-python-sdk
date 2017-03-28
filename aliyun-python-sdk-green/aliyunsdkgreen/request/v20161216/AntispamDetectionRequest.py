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
class AntispamDetectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2016-12-16', 'AntispamDetection','green')
		self.set_method('POST')

	def get_ImageUrl(self):
		return self.get_query_params().get('ImageUrl')

	def set_ImageUrl(self,ImageUrl):
		self.add_query_param('ImageUrl',ImageUrl)

	def get_DataId(self):
		return self.get_query_params().get('DataId')

	def set_DataId(self,DataId):
		self.add_query_param('DataId',DataId)

	def get_PostId(self):
		return self.get_query_params().get('PostId')

	def set_PostId(self,PostId):
		self.add_query_param('PostId',PostId)

	def get_SceneId(self):
		return self.get_query_params().get('SceneId')

	def set_SceneId(self,SceneId):
		self.add_query_param('SceneId',SceneId)

	def get_PostNick(self):
		return self.get_query_params().get('PostNick')

	def set_PostNick(self,PostNick):
		self.add_query_param('PostNick',PostNick)

	def get_PostIp(self):
		return self.get_query_params().get('PostIp')

	def set_PostIp(self,PostIp):
		self.add_query_param('PostIp',PostIp)

	def get_PostMac(self):
		return self.get_query_params().get('PostMac')

	def set_PostMac(self,PostMac):
		self.add_query_param('PostMac',PostMac)

	def get_PostTime(self):
		return self.get_query_params().get('PostTime')

	def set_PostTime(self,PostTime):
		self.add_query_param('PostTime',PostTime)

	def get_MachineCode(self):
		return self.get_query_params().get('MachineCode')

	def set_MachineCode(self,MachineCode):
		self.add_query_param('MachineCode',MachineCode)

	def get_ParentDataId(self):
		return self.get_query_params().get('ParentDataId')

	def set_ParentDataId(self,ParentDataId):
		self.add_query_param('ParentDataId',ParentDataId)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_PostContent(self):
		return self.get_query_params().get('PostContent')

	def set_PostContent(self,PostContent):
		self.add_query_param('PostContent',PostContent)