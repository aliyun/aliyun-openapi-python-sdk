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
import json

class DescribePlayQosListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ICE', '2020-11-09', 'DescribePlayQosList','ice')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Network(self): # String
		return self.get_query_params().get('Network')

	def set_Network(self, Network):  # String
		self.add_query_param('Network', Network)
	def get_MetricTypes(self): # Array
		return self.get_query_params().get('MetricTypes')

	def set_MetricTypes(self, MetricTypes):  # Array
		self.add_query_param("MetricTypes", json.dumps(MetricTypes))
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EndTs(self): # String
		return self.get_query_params().get('EndTs')

	def set_EndTs(self, EndTs):  # String
		self.add_query_param('EndTs', EndTs)
	def get_Definition(self): # String
		return self.get_query_params().get('Definition')

	def set_Definition(self, Definition):  # String
		self.add_query_param('Definition', Definition)
	def get_ItemConfigs(self): # String
		return self.get_query_params().get('ItemConfigs')

	def set_ItemConfigs(self, ItemConfigs):  # String
		self.add_query_param('ItemConfigs', ItemConfigs)
	def get_Os(self): # String
		return self.get_query_params().get('Os')

	def set_Os(self, Os):  # String
		self.add_query_param('Os', Os)
	def get_OrderName(self): # String
		return self.get_query_params().get('OrderName')

	def set_OrderName(self, OrderName):  # String
		self.add_query_param('OrderName', OrderName)
	def get_BeginTs(self): # String
		return self.get_query_params().get('BeginTs')

	def set_BeginTs(self, BeginTs):  # String
		self.add_query_param('BeginTs', BeginTs)
	def get_PageNo(self): # Integer
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Integer
		self.add_query_param('PageNo', PageNo)
	def get_TerminalType(self): # String
		return self.get_query_params().get('TerminalType')

	def set_TerminalType(self, TerminalType):  # String
		self.add_query_param('TerminalType', TerminalType)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
