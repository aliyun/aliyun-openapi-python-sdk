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
from aliyunsdkelasticsearch.endpoint import endpoint_data

class ListDiagnoseReportRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListDiagnoseReport','elasticsearch')
		self.set_uri_pattern('/openapi/diagnosis/instances/[InstanceId]/reports')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_size(self):
		return self.get_query_params().get('size')

	def set_size(self,size):
		self.add_query_param('size',size)

	def get_endTime(self):
		return self.get_query_params().get('endTime')

	def set_endTime(self,endTime):
		self.add_query_param('endTime',endTime)

	def get_startTime(self):
		return self.get_query_params().get('startTime')

	def set_startTime(self,startTime):
		self.add_query_param('startTime',startTime)

	def get_page(self):
		return self.get_query_params().get('page')

	def set_page(self,page):
		self.add_query_param('page',page)

	def get_detail(self):
		return self.get_query_params().get('detail')

	def set_detail(self,detail):
		self.add_query_param('detail',detail)

	def get_trigger(self):
		return self.get_query_params().get('trigger')

	def set_trigger(self,trigger):
		self.add_query_param('trigger',trigger)

	def get_lang(self):
		return self.get_query_params().get('lang')

	def set_lang(self,lang):
		self.add_query_param('lang',lang)