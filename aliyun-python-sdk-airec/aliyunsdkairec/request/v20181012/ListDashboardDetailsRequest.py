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
from aliyunsdkairec.endpoint import endpoint_data

class ListDashboardDetailsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2018-10-12', 'ListDashboardDetails','airec')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/dashboard/details')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MetricType(self):
		return self.get_query_params().get('MetricType')

	def set_MetricType(self,MetricType):
		self.add_query_param('MetricType',MetricType)

	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_TraceIds(self):
		return self.get_query_params().get('TraceIds')

	def set_TraceIds(self,TraceIds):
		self.add_query_param('TraceIds',TraceIds)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_SceneIds(self):
		return self.get_query_params().get('SceneIds')

	def set_SceneIds(self,SceneIds):
		self.add_query_param('SceneIds',SceneIds)