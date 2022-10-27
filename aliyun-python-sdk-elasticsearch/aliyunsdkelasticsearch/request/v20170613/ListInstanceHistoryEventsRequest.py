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

class ListInstanceHistoryEventsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'elasticsearch', '2017-06-13', 'ListInstanceHistoryEvents','elasticsearch')
		self.set_uri_pattern('/openapi/events')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_eventFinashEndTime(self): # string
		return self.get_query_params().get('eventFinashEndTime')

	def set_eventFinashEndTime(self, eventFinashEndTime):  # string
		self.add_query_param('eventFinashEndTime', eventFinashEndTime)
	def get_instanceId(self): # string
		return self.get_query_params().get('instanceId')

	def set_instanceId(self, instanceId):  # string
		self.add_query_param('instanceId', instanceId)
	def get_size(self): # integer
		return self.get_query_params().get('size')

	def set_size(self, size):  # integer
		self.add_query_param('size', size)
	def get_eventExecuteStartTime(self): # string
		return self.get_query_params().get('eventExecuteStartTime')

	def set_eventExecuteStartTime(self, eventExecuteStartTime):  # string
		self.add_query_param('eventExecuteStartTime', eventExecuteStartTime)
	def get_eventFinashStartTime(self): # string
		return self.get_query_params().get('eventFinashStartTime')

	def set_eventFinashStartTime(self, eventFinashStartTime):  # string
		self.add_query_param('eventFinashStartTime', eventFinashStartTime)
	def get_nodeIP(self): # string
		return self.get_query_params().get('nodeIP')

	def set_nodeIP(self, nodeIP):  # string
		self.add_query_param('nodeIP', nodeIP)
	def get_page(self): # integer
		return self.get_query_params().get('page')

	def set_page(self, page):  # integer
		self.add_query_param('page', page)
	def get_eventCreateEndTime(self): # string
		return self.get_query_params().get('eventCreateEndTime')

	def set_eventCreateEndTime(self, eventCreateEndTime):  # string
		self.add_query_param('eventCreateEndTime', eventCreateEndTime)
	def get_eventCreateStartTime(self): # string
		return self.get_query_params().get('eventCreateStartTime')

	def set_eventCreateStartTime(self, eventCreateStartTime):  # string
		self.add_query_param('eventCreateStartTime', eventCreateStartTime)
	def get_eventExecuteEndTime(self): # string
		return self.get_query_params().get('eventExecuteEndTime')

	def set_eventExecuteEndTime(self, eventExecuteEndTime):  # string
		self.add_query_param('eventExecuteEndTime', eventExecuteEndTime)
