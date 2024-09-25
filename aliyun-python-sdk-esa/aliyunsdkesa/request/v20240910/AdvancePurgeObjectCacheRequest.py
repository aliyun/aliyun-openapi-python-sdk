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

class AdvancePurgeObjectCacheRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'AdvancePurgeObjectCache')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Area(self): # String
		return self.get_query_params().get('Area')

	def set_Area(self, Area):  # String
		self.add_query_param('Area', Area)
	def get_TimeRangeBegin(self): # Integer
		return self.get_query_params().get('TimeRangeBegin')

	def set_TimeRangeBegin(self, TimeRangeBegin):  # Integer
		self.add_query_param('TimeRangeBegin', TimeRangeBegin)
	def get_TimeRangeEnd(self): # Integer
		return self.get_query_params().get('TimeRangeEnd')

	def set_TimeRangeEnd(self, TimeRangeEnd):  # Integer
		self.add_query_param('TimeRangeEnd', TimeRangeEnd)
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
	def get_Force(self): # Boolean
		return self.get_query_params().get('Force')

	def set_Force(self, Force):  # Boolean
		self.add_query_param('Force', Force)
	def get_Stations(self): # String
		return self.get_query_params().get('Stations')

	def set_Stations(self, Stations):  # String
		self.add_query_param('Stations', Stations)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
