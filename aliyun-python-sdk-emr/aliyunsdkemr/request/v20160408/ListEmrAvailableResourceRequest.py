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

class ListEmrAvailableResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListEmrAvailableResource','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DepositType(self):
		return self.get_query_params().get('DepositType')

	def set_DepositType(self,DepositType):
		self.add_query_param('DepositType',DepositType)

	def get_SystemDiskType(self):
		return self.get_query_params().get('SystemDiskType')

	def set_SystemDiskType(self,SystemDiskType):
		self.add_query_param('SystemDiskType',SystemDiskType)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_DestinationResource(self):
		return self.get_query_params().get('DestinationResource')

	def set_DestinationResource(self,DestinationResource):
		self.add_query_param('DestinationResource',DestinationResource)

	def get_ClusterType(self):
		return self.get_query_params().get('ClusterType')

	def set_ClusterType(self,ClusterType):
		self.add_query_param('ClusterType',ClusterType)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_ZoneId(self):
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_query_param('ZoneId',ZoneId)

	def get_DataDiskType(self):
		return self.get_query_params().get('DataDiskType')

	def set_DataDiskType(self,DataDiskType):
		self.add_query_param('DataDiskType',DataDiskType)