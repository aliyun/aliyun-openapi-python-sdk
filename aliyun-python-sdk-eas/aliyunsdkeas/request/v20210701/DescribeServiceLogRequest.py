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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkeas.endpoint import endpoint_data

class DescribeServiceLogRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2021-07-01', 'DescribeServiceLog','eas')
		self.set_uri_pattern('/api/v2/services/[ClusterId]/[ServiceName]/logs')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Ip(self): # string
		return self.get_query_params().get('Ip')

	def set_Ip(self, Ip):  # string
		self.add_query_param('Ip', Ip)
	def get_PageSize(self): # integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # integer
		self.add_query_param('PageSize', PageSize)
	def get_EndTime(self): # string
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # string
		self.add_query_param('EndTime', EndTime)
	def get_ServiceName(self): # string
		return self.get_path_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # string
		self.add_path_param('ServiceName', ServiceName)
	def get_StartTime(self): # string
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # string
		self.add_query_param('StartTime', StartTime)
	def get_ClusterId(self): # string
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_path_param('ClusterId', ClusterId)
	def get_PageNum(self): # integer
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # integer
		self.add_query_param('PageNum', PageNum)
	def get_Keyword(self): # string
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # string
		self.add_query_param('Keyword', Keyword)
