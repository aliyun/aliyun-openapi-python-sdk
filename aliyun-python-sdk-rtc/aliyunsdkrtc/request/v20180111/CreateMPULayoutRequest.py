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

class CreateMPULayoutRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rtc', '2018-01-11', 'CreateMPULayout','rtc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Paness(self):
		return self.get_query_params().get('Panes')

	def set_Paness(self, Paness):
		for depth1 in range(len(Paness)):
			if Paness[depth1].get('PaneId') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.PaneId', Paness[depth1].get('PaneId'))
			if Paness[depth1].get('MajorPane') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.MajorPane', Paness[depth1].get('MajorPane'))
			if Paness[depth1].get('X') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.X', Paness[depth1].get('X'))
			if Paness[depth1].get('Y') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.Y', Paness[depth1].get('Y'))
			if Paness[depth1].get('Width') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.Width', Paness[depth1].get('Width'))
			if Paness[depth1].get('Height') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.Height', Paness[depth1].get('Height'))
			if Paness[depth1].get('ZOrder') is not None:
				self.add_query_param('Panes.' + str(depth1 + 1) + '.ZOrder', Paness[depth1].get('ZOrder'))

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_AudioMixCount(self):
		return self.get_query_params().get('AudioMixCount')

	def set_AudioMixCount(self,AudioMixCount):
		self.add_query_param('AudioMixCount',AudioMixCount)