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
from aliyunsdklinkedmall.endpoint import endpoint_data

class ListItemActivitiesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'linkedmall', '2018-01-16', 'ListItemActivities','linkedmall')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LmItemIds(self):
		return self.get_query_params().get('LmItemIds')

	def set_LmItemIds(self,LmItemIds):
		self.add_query_param('LmItemIds',LmItemIds)

	def get_ItemIds(self):
		return self.get_query_params().get('ItemIds')

	def set_ItemIds(self,ItemIds):
		self.add_query_param('ItemIds',ItemIds)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)