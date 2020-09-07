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
from aliyunsdkedas.endpoint import endpoint_data

class QueryMonitorInfoRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'QueryMonitorInfo','Edas')
		self.set_uri_pattern('/pop/v5/monitor/queryMonitorInfo')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Metric(self):
		return self.get_query_params().get('Metric')

	def set_Metric(self,Metric):
		self.add_query_param('Metric',Metric)

	def get_Aggregator(self):
		return self.get_query_params().get('Aggregator')

	def set_Aggregator(self,Aggregator):
		self.add_query_param('Aggregator',Aggregator)

	def get_Start(self):
		return self.get_query_params().get('Start')

	def set_Start(self,Start):
		self.add_query_param('Start',Start)

	def get_End(self):
		return self.get_query_params().get('End')

	def set_End(self,End):
		self.add_query_param('End',End)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)