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
from aliyunsdkiot.endpoint import endpoint_data

class QueryAppDeviceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'QueryAppDeviceList','Iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_TagLists(self):
		return self.get_query_params().get('TagLists')

	def set_TagLists(self, TagLists):
		for depth1 in range(len(TagLists)):
			if TagLists[depth1].get('TagName') is not None:
				self.add_query_param('TagList.' + str(depth1 + 1) + '.TagName', TagLists[depth1].get('TagName'))
			if TagLists[depth1].get('TagValue') is not None:
				self.add_query_param('TagList.' + str(depth1 + 1) + '.TagValue', TagLists[depth1].get('TagValue'))

	def get_ProductKeyLists(self):
		return self.get_query_params().get('ProductKeyLists')

	def set_ProductKeyLists(self, ProductKeyLists):
		for depth1 in range(len(ProductKeyLists)):
			if ProductKeyLists[depth1] is not None:
				self.add_query_param('ProductKeyList.' + str(depth1 + 1) , ProductKeyLists[depth1])

	def get_CategoryKeyLists(self):
		return self.get_query_params().get('CategoryKeyLists')

	def set_CategoryKeyLists(self, CategoryKeyLists):
		for depth1 in range(len(CategoryKeyLists)):
			if CategoryKeyLists[depth1] is not None:
				self.add_query_param('CategoryKeyList.' + str(depth1 + 1) , CategoryKeyLists[depth1])

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)