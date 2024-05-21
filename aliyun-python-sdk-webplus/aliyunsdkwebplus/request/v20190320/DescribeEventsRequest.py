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
from aliyunsdkwebplus.endpoint import endpoint_data

class DescribeEventsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'DescribeEvents','webx')
		self.set_uri_pattern('/pop/v1/wam/event')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LastChangeEvents(self):
		return self.get_query_params().get('LastChangeEvents')

	def set_LastChangeEvents(self,LastChangeEvents):
		self.add_query_param('LastChangeEvents',LastChangeEvents)

	def get_ReverseByTimestamp(self):
		return self.get_query_params().get('ReverseByTimestamp')

	def set_ReverseByTimestamp(self,ReverseByTimestamp):
		self.add_query_param('ReverseByTimestamp',ReverseByTimestamp)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_EnvId(self):
		return self.get_query_params().get('EnvId')

	def set_EnvId(self,EnvId):
		self.add_query_param('EnvId',EnvId)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_ChangeId(self):
		return self.get_query_params().get('ChangeId')

	def set_ChangeId(self,ChangeId):
		self.add_query_param('ChangeId',ChangeId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)