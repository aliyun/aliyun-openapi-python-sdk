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

class CreateRoomRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateRoom','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TemplateIds(self):
		return self.get_query_params().get('TemplateIds')

	def set_TemplateIds(self,TemplateIds):
		self.add_query_param('TemplateIds',TemplateIds)

	def get_AnchorId(self):
		return self.get_query_params().get('AnchorId')

	def set_AnchorId(self,AnchorId):
		self.add_query_param('AnchorId',AnchorId)

	def get_UseAppTranscode(self):
		return self.get_query_params().get('UseAppTranscode')

	def set_UseAppTranscode(self,UseAppTranscode):
		self.add_query_param('UseAppTranscode',UseAppTranscode)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RoomId(self):
		return self.get_query_params().get('RoomId')

	def set_RoomId(self,RoomId):
		self.add_query_param('RoomId',RoomId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)