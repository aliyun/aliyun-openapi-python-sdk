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

class GetRumDataForPageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'GetRumDataForPage','arms')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Query(self): # String
		return self.get_query_params().get('Query')

	def set_Query(self, Query):  # String
		self.add_query_param('Query', Query)
	def get_EndTime(self): # Integer
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Integer
		self.add_query_param('EndTime', EndTime)
	def get_Pid(self): # String
		return self.get_query_params().get('Pid')

	def set_Pid(self, Pid):  # String
		self.add_query_param('Pid', Pid)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_StartTime(self): # Integer
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Integer
		self.add_query_param('StartTime', StartTime)
	def get_AppGroup(self): # String
		return self.get_query_params().get('AppGroup')

	def set_AppGroup(self, AppGroup):  # String
		self.add_query_param('AppGroup', AppGroup)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
