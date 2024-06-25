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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class GetLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'GetLog','schedulerx2')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NamespaceSource(self): # String
		return self.get_query_params().get('NamespaceSource')

	def set_NamespaceSource(self, NamespaceSource):  # String
		self.add_query_param('NamespaceSource', NamespaceSource)
	def get_Line(self): # Integer
		return self.get_query_params().get('Line')

	def set_Line(self, Line):  # Integer
		self.add_query_param('Line', Line)
	def get_StartTimestamp(self): # Long
		return self.get_query_params().get('StartTimestamp')

	def set_StartTimestamp(self, StartTimestamp):  # Long
		self.add_query_param('StartTimestamp', StartTimestamp)
	def get_EndTimestamp(self): # Long
		return self.get_query_params().get('EndTimestamp')

	def set_EndTimestamp(self, EndTimestamp):  # Long
		self.add_query_param('EndTimestamp', EndTimestamp)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_Keyword(self): # String
		return self.get_query_params().get('Keyword')

	def set_Keyword(self, Keyword):  # String
		self.add_query_param('Keyword', Keyword)
	def get_Offset(self): # Integer
		return self.get_query_params().get('Offset')

	def set_Offset(self, Offset):  # Integer
		self.add_query_param('Offset', Offset)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_Reverse(self): # Boolean
		return self.get_query_params().get('Reverse')

	def set_Reverse(self, Reverse):  # Boolean
		self.add_query_param('Reverse', Reverse)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_JobInstanceId(self): # String
		return self.get_query_params().get('JobInstanceId')

	def set_JobInstanceId(self, JobInstanceId):  # String
		self.add_query_param('JobInstanceId', JobInstanceId)
