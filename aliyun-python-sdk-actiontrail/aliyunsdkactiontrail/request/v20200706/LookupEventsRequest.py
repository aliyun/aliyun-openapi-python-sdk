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
from aliyunsdkactiontrail.endpoint import endpoint_data

class LookupEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Actiontrail', '2020-07-06', 'LookupEvents','actiontrail')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_LookupAttributes(self):
		return self.get_query_params().get('LookupAttribute')

	def set_LookupAttributes(self, LookupAttributes):
		for depth1 in range(len(LookupAttributes)):
			if LookupAttributes[depth1].get('Value') is not None:
				self.add_query_param('LookupAttribute.' + str(depth1 + 1) + '.Value', LookupAttributes[depth1].get('Value'))
			if LookupAttributes[depth1].get('Key') is not None:
				self.add_query_param('LookupAttribute.' + str(depth1 + 1) + '.Key', LookupAttributes[depth1].get('Key'))

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_Direction(self):
		return self.get_query_params().get('Direction')

	def set_Direction(self,Direction):
		self.add_query_param('Direction',Direction)