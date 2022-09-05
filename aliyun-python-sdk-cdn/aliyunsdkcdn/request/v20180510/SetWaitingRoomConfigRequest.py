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
from aliyunsdkcdn.endpoint import endpoint_data

class SetWaitingRoomConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'SetWaitingRoomConfig')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_WaitUrl(self): # String
		return self.get_query_params().get('WaitUrl')

	def set_WaitUrl(self, WaitUrl):  # String
		self.add_query_param('WaitUrl', WaitUrl)
	def get_WaitUri(self): # String
		return self.get_query_params().get('WaitUri')

	def set_WaitUri(self, WaitUri):  # String
		self.add_query_param('WaitUri', WaitUri)
	def get_MaxTimeWait(self): # Integer
		return self.get_query_params().get('MaxTimeWait')

	def set_MaxTimeWait(self, MaxTimeWait):  # Integer
		self.add_query_param('MaxTimeWait', MaxTimeWait)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_AllowPct(self): # Integer
		return self.get_query_params().get('AllowPct')

	def set_AllowPct(self, AllowPct):  # Integer
		self.add_query_param('AllowPct', AllowPct)
	def get_GapTime(self): # Integer
		return self.get_query_params().get('GapTime')

	def set_GapTime(self, GapTime):  # Integer
		self.add_query_param('GapTime', GapTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
