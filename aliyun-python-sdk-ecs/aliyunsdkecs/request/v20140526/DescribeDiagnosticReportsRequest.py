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
from aliyunsdkecs.endpoint import endpoint_data

class DescribeDiagnosticReportsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeDiagnosticReports','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Severity(self): # String
		return self.get_query_params().get('Severity')

	def set_Severity(self, Severity):  # String
		self.add_query_param('Severity', Severity)
	def get_ReportIdss(self): # RepeatList
		return self.get_query_params().get('ReportIds')

	def set_ReportIdss(self, ReportIds):  # RepeatList
		for depth1 in range(len(ReportIds)):
			self.add_query_param('ReportIds.' + str(depth1 + 1), ReportIds[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_ResourceIdss(self): # RepeatList
		return self.get_query_params().get('ResourceIds')

	def set_ResourceIdss(self, ResourceIds):  # RepeatList
		for depth1 in range(len(ResourceIds)):
			self.add_query_param('ResourceIds.' + str(depth1 + 1), ResourceIds[depth1])
