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

class GetServiceStatisticsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2018-05-22', 'GetServiceStatistics')
		self.set_uri_pattern('/api/services/[region]/[service_name]/statistics')
		self.set_method('GET')

	def get_metric(self):
		return self.get_query_params().get('metric')

	def set_metric(self,metric):
		self.add_query_param('metric',metric)

	def get_service_name(self):
		return self.get_path_params().get('service_name')

	def set_service_name(self,service_name):
		self.add_path_param('service_name',service_name)

	def get_count(self):
		return self.get_query_params().get('count')

	def set_count(self,count):
		self.add_query_param('count',count)

	def get__from(self):
		return self.get_query_params().get('from')

	def set__from(self,_from):
		self.add_query_param('from',_from)

	def get_to(self):
		return self.get_query_params().get('to')

	def set_to(self,to):
		self.add_query_param('to',to)

	def get_region(self):
		return self.get_path_params().get('region')

	def set_region(self,region):
		self.add_path_param('region',region)