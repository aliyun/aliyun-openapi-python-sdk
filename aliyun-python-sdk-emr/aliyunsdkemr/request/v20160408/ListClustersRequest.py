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

class ListClustersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListClusters','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_StatusLists(self):
		return self.get_query_params().get('StatusList')

	def set_StatusLists(self, StatusLists):
		for depth1 in range(len(StatusLists)):
			if StatusLists[depth1] is not None:
				self.add_query_param('StatusList.' + str(depth1 + 1) , StatusLists[depth1])

	def get_IsDesc(self):
		return self.get_query_params().get('IsDesc')

	def set_IsDesc(self,IsDesc):
		self.add_query_param('IsDesc',IsDesc)

	def get_DepositType(self):
		return self.get_query_params().get('DepositType')

	def set_DepositType(self,DepositType):
		self.add_query_param('DepositType',DepositType)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_MachineType(self):
		return self.get_query_params().get('MachineType')

	def set_MachineType(self,MachineType):
		self.add_query_param('MachineType',MachineType)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Tags(self):
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tags):
		for depth1 in range(len(Tags)):
			if Tags[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tags[depth1].get('Value'))
			if Tags[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tags[depth1].get('Key'))

	def get_CreateType(self):
		return self.get_query_params().get('CreateType')

	def set_CreateType(self,CreateType):
		self.add_query_param('CreateType',CreateType)

	def get_ExpiredTagLists(self):
		return self.get_query_params().get('ExpiredTagList')

	def set_ExpiredTagLists(self, ExpiredTagLists):
		for depth1 in range(len(ExpiredTagLists)):
			if ExpiredTagLists[depth1] is not None:
				self.add_query_param('ExpiredTagList.' + str(depth1 + 1) , ExpiredTagLists[depth1])

	def get_DefaultStatus(self):
		return self.get_query_params().get('DefaultStatus')

	def set_DefaultStatus(self,DefaultStatus):
		self.add_query_param('DefaultStatus',DefaultStatus)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ClusterTypeLists(self):
		return self.get_query_params().get('ClusterTypeList')

	def set_ClusterTypeLists(self, ClusterTypeLists):
		for depth1 in range(len(ClusterTypeLists)):
			if ClusterTypeLists[depth1] is not None:
				self.add_query_param('ClusterTypeList.' + str(depth1 + 1) , ClusterTypeLists[depth1])