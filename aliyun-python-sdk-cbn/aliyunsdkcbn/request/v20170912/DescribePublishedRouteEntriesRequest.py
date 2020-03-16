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
from aliyunsdkcbn.endpoint import endpoint_data

class DescribePublishedRouteEntriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cbn', '2017-09-12', 'DescribePublishedRouteEntries','Cbn')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CenId(self):
		return self.get_query_params().get('CenId')

	def set_CenId(self,CenId):
		self.add_query_param('CenId',CenId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ChildInstanceRegionId(self):
		return self.get_query_params().get('ChildInstanceRegionId')

	def set_ChildInstanceRegionId(self,ChildInstanceRegionId):
		self.add_query_param('ChildInstanceRegionId',ChildInstanceRegionId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DestinationCidrBlock(self):
		return self.get_query_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self,DestinationCidrBlock):
		self.add_query_param('DestinationCidrBlock',DestinationCidrBlock)

	def get_ChildInstanceType(self):
		return self.get_query_params().get('ChildInstanceType')

	def set_ChildInstanceType(self,ChildInstanceType):
		self.add_query_param('ChildInstanceType',ChildInstanceType)

	def get_ChildInstanceId(self):
		return self.get_query_params().get('ChildInstanceId')

	def set_ChildInstanceId(self,ChildInstanceId):
		self.add_query_param('ChildInstanceId',ChildInstanceId)

	def get_ChildInstanceRouteTableId(self):
		return self.get_query_params().get('ChildInstanceRouteTableId')

	def set_ChildInstanceRouteTableId(self,ChildInstanceRouteTableId):
		self.add_query_param('ChildInstanceRouteTableId',ChildInstanceRouteTableId)