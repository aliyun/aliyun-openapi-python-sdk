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
from aliyunsdkvod.endpoint import endpoint_data

class DescribeVodMediaPlayDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'DescribeVodMediaPlayData','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_PlayDate(self): # String
		return self.get_query_params().get('PlayDate')

	def set_PlayDate(self, PlayDate):  # String
		self.add_query_param('PlayDate', PlayDate)
	def get_Os(self): # String
		return self.get_query_params().get('Os')

	def set_Os(self, Os):  # String
		self.add_query_param('Os', Os)
	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
	def get_OrderName(self): # String
		return self.get_query_params().get('OrderName')

	def set_OrderName(self, OrderName):  # String
		self.add_query_param('OrderName', OrderName)
	def get_PageNo(self): # Long
		return self.get_query_params().get('PageNo')

	def set_PageNo(self, PageNo):  # Long
		self.add_query_param('PageNo', PageNo)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
	def get_TerminalType(self): # String
		return self.get_query_params().get('TerminalType')

	def set_TerminalType(self, TerminalType):  # String
		self.add_query_param('TerminalType', TerminalType)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
