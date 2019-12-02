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
from aliyunsdkpts.endpoint import endpoint_data

class ListReportsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'PTS', '2019-08-10', 'ListReports','1.0.0')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SceneType(self):
		return self.get_query_params().get('SceneType')

	def set_SceneType(self,SceneType):
		self.add_query_param('SceneType',SceneType)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_BeginTime(self):
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self,BeginTime):
		self.add_query_param('BeginTime',BeginTime)

	def get_Keyword(self):
		return self.get_query_params().get('Keyword')

	def set_Keyword(self,Keyword):
		self.add_query_param('Keyword',Keyword)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)