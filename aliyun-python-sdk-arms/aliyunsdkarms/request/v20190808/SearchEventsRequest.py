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
from aliyunsdkarms.endpoint import endpoint_data

class SearchEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'SearchEvents','arms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsTrigger(self):
		return self.get_query_params().get('IsTrigger')

	def set_IsTrigger(self,IsTrigger):
		self.add_query_param('IsTrigger',IsTrigger)

	def get_AppType(self):
		return self.get_query_params().get('AppType')

	def set_AppType(self,AppType):
		self.add_query_param('AppType',AppType)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_Pid(self):
		return self.get_query_params().get('Pid')

	def set_Pid(self,Pid):
		self.add_query_param('Pid',Pid)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_AlertType(self):
		return self.get_query_params().get('AlertType')

	def set_AlertType(self,AlertType):
		self.add_query_param('AlertType',AlertType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AlertId(self):
		return self.get_query_params().get('AlertId')

	def set_AlertId(self,AlertId):
		self.add_query_param('AlertId',AlertId)