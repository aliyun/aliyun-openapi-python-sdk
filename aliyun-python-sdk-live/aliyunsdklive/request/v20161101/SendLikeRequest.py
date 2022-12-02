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

class SendLikeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SendLike','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OperatorUserId(self): # String
		return self.get_body_params().get('OperatorUserId')

	def set_OperatorUserId(self, OperatorUserId):  # String
		self.add_body_params('OperatorUserId', OperatorUserId)
	def get_BroadCastType(self): # Integer
		return self.get_body_params().get('BroadCastType')

	def set_BroadCastType(self, BroadCastType):  # Integer
		self.add_body_params('BroadCastType', BroadCastType)
	def get_GroupId(self): # String
		return self.get_body_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_body_params('GroupId', GroupId)
	def get_Count(self): # String
		return self.get_body_params().get('Count')

	def set_Count(self, Count):  # String
		self.add_body_params('Count', Count)
	def get_AppId(self): # String
		return self.get_body_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_body_params('AppId', AppId)
