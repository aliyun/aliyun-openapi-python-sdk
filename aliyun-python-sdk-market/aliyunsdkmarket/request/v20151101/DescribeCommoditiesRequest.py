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
from aliyunsdkmarket.endpoint import endpoint_data

class DescribeCommoditiesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Market', '2015-11-01', 'DescribeCommodities','yunmarket')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CommodityGmtModifiedTo(self):
		return self.get_query_params().get('CommodityGmtModifiedTo')

	def set_CommodityGmtModifiedTo(self,CommodityGmtModifiedTo):
		self.add_query_param('CommodityGmtModifiedTo',CommodityGmtModifiedTo)

	def get_CommodityGmtModifiedFrom(self):
		return self.get_query_params().get('CommodityGmtModifiedFrom')

	def set_CommodityGmtModifiedFrom(self,CommodityGmtModifiedFrom):
		self.add_query_param('CommodityGmtModifiedFrom',CommodityGmtModifiedFrom)

	def get_CommodityId(self):
		return self.get_query_params().get('CommodityId')

	def set_CommodityId(self,CommodityId):
		self.add_query_param('CommodityId',CommodityId)

	def get_CommodityGmtPublishFrom(self):
		return self.get_query_params().get('CommodityGmtPublishFrom')

	def set_CommodityGmtPublishFrom(self,CommodityGmtPublishFrom):
		self.add_query_param('CommodityGmtPublishFrom',CommodityGmtPublishFrom)

	def get_CommodityStatuses(self):
		return self.get_query_params().get('CommodityStatuses')

	def set_CommodityStatuses(self,CommodityStatuses):
		self.add_query_param('CommodityStatuses',CommodityStatuses)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_CommodityGmtCreatedFrom(self):
		return self.get_query_params().get('CommodityGmtCreatedFrom')

	def set_CommodityGmtCreatedFrom(self,CommodityGmtCreatedFrom):
		self.add_query_param('CommodityGmtCreatedFrom',CommodityGmtCreatedFrom)

	def get_CommodityIds(self):
		return self.get_query_params().get('CommodityIds')

	def set_CommodityIds(self,CommodityIds):
		self.add_query_param('CommodityIds',CommodityIds)

	def get_CommodityGmtCreatedTo(self):
		return self.get_query_params().get('CommodityGmtCreatedTo')

	def set_CommodityGmtCreatedTo(self,CommodityGmtCreatedTo):
		self.add_query_param('CommodityGmtCreatedTo',CommodityGmtCreatedTo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CommodityGmtPublishTo(self):
		return self.get_query_params().get('CommodityGmtPublishTo')

	def set_CommodityGmtPublishTo(self,CommodityGmtPublishTo):
		self.add_query_param('CommodityGmtPublishTo',CommodityGmtPublishTo)

	def get_CommodityAuditStatuses(self):
		return self.get_query_params().get('CommodityAuditStatuses')

	def set_CommodityAuditStatuses(self,CommodityAuditStatuses):
		self.add_query_param('CommodityAuditStatuses',CommodityAuditStatuses)

	def get_Properties(self):
		return self.get_query_params().get('Properties')

	def set_Properties(self,Properties):
		self.add_query_param('Properties',Properties)

	def get_CommodityCategoryIds(self):
		return self.get_query_params().get('CommodityCategoryIds')

	def set_CommodityCategoryIds(self,CommodityCategoryIds):
		self.add_query_param('CommodityCategoryIds',CommodityCategoryIds)