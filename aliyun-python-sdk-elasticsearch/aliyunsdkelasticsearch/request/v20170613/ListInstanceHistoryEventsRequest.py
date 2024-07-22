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

	def get_eventFinashEndTime(self): # String
		return self.get_query_params().get('eventFinashEndTime')

	def set_eventFinashEndTime(self, eventFinashEndTime):  # String
		self.add_query_param('eventFinashEndTime', eventFinashEndTime)
	def get_instanceId(self): # String
		return self.get_query_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_query_param('instanceId', instanceId)
	def get_size(self): # Integer
		return self.get_query_params().get('size')

	def set_size(self, size):  # Integer
		self.add_query_param('size', size)
	def get_eventExecuteStartTime(self): # String
		return self.get_query_params().get('eventExecuteStartTime')

	def set_eventExecuteStartTime(self, eventExecuteStartTime):  # String
		self.add_query_param('eventExecuteStartTime', eventExecuteStartTime)
	def get_eventFinashStartTime(self): # String
		return self.get_query_params().get('eventFinashStartTime')

	def set_eventFinashStartTime(self, eventFinashStartTime):  # String
		self.add_query_param('eventFinashStartTime', eventFinashStartTime)
	def get_nodeIP(self): # String
		return self.get_query_params().get('nodeIP')

	def set_nodeIP(self, nodeIP):  # String
		self.add_query_param('nodeIP', nodeIP)
	def get_page(self): # Integer
		return self.get_query_params().get('page')

	def set_page(self, page):  # Integer
		self.add_query_param('page', page)
	def get_eventCreateEndTime(self): # String
		return self.get_query_params().get('eventCreateEndTime')

	def set_eventCreateEndTime(self, eventCreateEndTime):  # String
		self.add_query_param('eventCreateEndTime', eventCreateEndTime)
	def get_body(self): # String
		return self.get_body_params().get('body')

	def set_body(self, body):  # String
		self.add_body_params('body', body)
	def get_eventCreateStartTime(self): # String
		return self.get_query_params().get('eventCreateStartTime')

	def set_eventCreateStartTime(self, eventCreateStartTime):  # String
		self.add_query_param('eventCreateStartTime', eventCreateStartTime)
	def get_eventExecuteEndTime(self): # String
		return self.get_query_params().get('eventExecuteEndTime')

	def set_eventExecuteEndTime(self, eventExecuteEndTime):  # String
		self.add_query_param('eventExecuteEndTime', eventExecuteEndTime)
