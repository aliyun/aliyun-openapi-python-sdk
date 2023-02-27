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
from aliyunsdkice.endpoint import endpoint_data

class ListDynamicImageJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'ListDynamicImageJobs','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NextPageToken(self): # String
		return self.get_query_params().get('NextPageToken')

	def set_NextPageToken(self, NextPageToken):  # String
		self.add_query_param('NextPageToken', NextPageToken)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EndOfCreateTime(self): # String
		return self.get_query_params().get('EndOfCreateTime')

	def set_EndOfCreateTime(self, EndOfCreateTime):  # String
		self.add_query_param('EndOfCreateTime', EndOfCreateTime)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_StartOfCreateTime(self): # String
		return self.get_query_params().get('StartOfCreateTime')

	def set_StartOfCreateTime(self, StartOfCreateTime):  # String
		self.add_query_param('StartOfCreateTime', StartOfCreateTime)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
