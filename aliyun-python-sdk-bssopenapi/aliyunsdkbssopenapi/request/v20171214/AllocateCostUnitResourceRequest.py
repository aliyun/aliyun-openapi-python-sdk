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
from aliyunsdkbssopenapi.endpoint import endpoint_data

class AllocateCostUnitResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'AllocateCostUnitResource')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceInstanceLists(self):
		return self.get_query_params().get('ResourceInstanceLists')

	def set_ResourceInstanceLists(self, ResourceInstanceLists):
		for depth1 in range(len(ResourceInstanceLists)):
			if ResourceInstanceLists[depth1].get('ResourceId') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.ResourceId', ResourceInstanceLists[depth1].get('ResourceId'))
			if ResourceInstanceLists[depth1].get('CommodityCode') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.CommodityCode', ResourceInstanceLists[depth1].get('CommodityCode'))
			if ResourceInstanceLists[depth1].get('ResourceUserId') is not None:
				self.add_query_param('ResourceInstanceList.' + str(depth1 + 1) + '.ResourceUserId', ResourceInstanceLists[depth1].get('ResourceUserId'))

	def get_FromUnitId(self):
		return self.get_query_params().get('FromUnitId')

	def set_FromUnitId(self,FromUnitId):
		self.add_query_param('FromUnitId',FromUnitId)

	def get_ToUnitId(self):
		return self.get_query_params().get('ToUnitId')

	def set_ToUnitId(self,ToUnitId):
		self.add_query_param('ToUnitId',ToUnitId)

	def get_FromUnitUserId(self):
		return self.get_query_params().get('FromUnitUserId')

	def set_FromUnitUserId(self,FromUnitUserId):
		self.add_query_param('FromUnitUserId',FromUnitUserId)

	def get_ToUnitUserId(self):
		return self.get_query_params().get('ToUnitUserId')

	def set_ToUnitUserId(self,ToUnitUserId):
		self.add_query_param('ToUnitUserId',ToUnitUserId)