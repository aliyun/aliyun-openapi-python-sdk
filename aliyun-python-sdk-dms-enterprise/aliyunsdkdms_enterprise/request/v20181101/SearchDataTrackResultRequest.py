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
from aliyunsdkdms_enterprise.endpoint import endpoint_data
import json

class SearchDataTrackResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'SearchDataTrackResult','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_FilterStartTime(self): # String
		return self.get_query_params().get('FilterStartTime')

	def set_FilterStartTime(self, FilterStartTime):  # String
		self.add_query_param('FilterStartTime', FilterStartTime)
	def get_FilterTypeList(self): # Array
		return self.get_query_params().get('FilterTypeList')

	def set_FilterTypeList(self, FilterTypeList):  # Array
		self.add_query_param("FilterTypeList", json.dumps(FilterTypeList))
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_OrderId(self): # Long
		return self.get_query_params().get('OrderId')

	def set_OrderId(self, OrderId):  # Long
		self.add_query_param('OrderId', OrderId)
	def get_FilterTableList(self): # Array
		return self.get_query_params().get('FilterTableList')

	def set_FilterTableList(self, FilterTableList):  # Array
		self.add_query_param("FilterTableList", json.dumps(FilterTableList))
	def get_FilterEndTime(self): # String
		return self.get_query_params().get('FilterEndTime')

	def set_FilterEndTime(self, FilterEndTime):  # String
		self.add_query_param('FilterEndTime', FilterEndTime)
	def get_ColumnFilter(self): # Struct
		return self.get_query_params().get('ColumnFilter')

	def set_ColumnFilter(self, ColumnFilter):  # Struct
		self.add_query_param("ColumnFilter", json.dumps(ColumnFilter))
