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
from aliyunsdkemr.endpoint import endpoint_data

class ListFlowEntitySnapshotRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListFlowEntitySnapshot','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageCount(self):
		return self.get_query_params().get('PageCount')

	def set_PageCount(self,PageCount):
		self.add_query_param('PageCount',PageCount)

	def get_OrderMode(self):
		return self.get_query_params().get('OrderMode')

	def set_OrderMode(self,OrderMode):
		self.add_query_param('OrderMode',OrderMode)

	def get_EntityId(self):
		return self.get_query_params().get('EntityId')

	def set_EntityId(self,EntityId):
		self.add_query_param('EntityId',EntityId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CommitterId(self):
		return self.get_query_params().get('CommitterId')

	def set_CommitterId(self,CommitterId):
		self.add_query_param('CommitterId',CommitterId)

	def get_CurrentSize(self):
		return self.get_query_params().get('CurrentSize')

	def set_CurrentSize(self,CurrentSize):
		self.add_query_param('CurrentSize',CurrentSize)

	def get_OrderField(self):
		return self.get_query_params().get('OrderField')

	def set_OrderField(self,OrderField):
		self.add_query_param('OrderField',OrderField)

	def get_EntityGroupId(self):
		return self.get_query_params().get('EntityGroupId')

	def set_EntityGroupId(self,EntityGroupId):
		self.add_query_param('EntityGroupId',EntityGroupId)

	def get_Revision(self):
		return self.get_query_params().get('Revision')

	def set_Revision(self,Revision):
		self.add_query_param('Revision',Revision)

	def get_EntityType(self):
		return self.get_query_params().get('EntityType')

	def set_EntityType(self,EntityType):
		self.add_query_param('EntityType',EntityType)