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

class DescribeMeterImsMediaConvertUsageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'DescribeMeterImsMediaConvertUsage','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_StartTs(self): # Long
		return self.get_query_params().get('StartTs')

	def set_StartTs(self, StartTs):  # Long
		self.add_query_param('StartTs', StartTs)
	def get_EndTs(self): # Long
		return self.get_query_params().get('EndTs')

	def set_EndTs(self, EndTs):  # Long
		self.add_query_param('EndTs', EndTs)
	def get_Interval(self): # Long
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # Long
		self.add_query_param('Interval', Interval)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
