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

class QueryReleaseMetricRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'QueryReleaseMetric','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ChangeOrderId(self): # String
		return self.get_query_params().get('ChangeOrderId')

	def set_ChangeOrderId(self, ChangeOrderId):  # String
		self.add_query_param('ChangeOrderId', ChangeOrderId)
	def get_MetricType(self): # String
		return self.get_query_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_query_param('MetricType', MetricType)
	def get_CreateTime(self): # Long
		return self.get_query_params().get('CreateTime')

	def set_CreateTime(self, CreateTime):  # Long
		self.add_query_param('CreateTime', CreateTime)
	def get_Pid(self): # String
		return self.get_query_params().get('Pid')

	def set_Pid(self, Pid):  # String
		self.add_query_param('Pid', Pid)
	def get_ProxyUserId(self): # String
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self, ProxyUserId):  # String
		self.add_query_param('ProxyUserId', ProxyUserId)
	def get_ReleaseEndTime(self): # Long
		return self.get_query_params().get('ReleaseEndTime')

	def set_ReleaseEndTime(self, ReleaseEndTime):  # Long
		self.add_query_param('ReleaseEndTime', ReleaseEndTime)
	def get_Service(self): # String
		return self.get_query_params().get('Service')

	def set_Service(self, Service):  # String
		self.add_query_param('Service', Service)
	def get_ReleaseStartTime(self): # Long
		return self.get_query_params().get('ReleaseStartTime')

	def set_ReleaseStartTime(self, ReleaseStartTime):  # Long
		self.add_query_param('ReleaseStartTime', ReleaseStartTime)
