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
from aliyunsdkecs.endpoint import endpoint_data

class ModifyDiskSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyDiskSpec','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DestinationZoneId(self): # String
		return self.get_query_params().get('DestinationZoneId')

	def set_DestinationZoneId(self, DestinationZoneId):  # String
		self.add_query_param('DestinationZoneId', DestinationZoneId)
	def get_DiskCategory(self): # String
		return self.get_query_params().get('DiskCategory')

	def set_DiskCategory(self, DiskCategory):  # String
		self.add_query_param('DiskCategory', DiskCategory)
	def get_DiskId(self): # String
		return self.get_query_params().get('DiskId')

	def set_DiskId(self, DiskId):  # String
		self.add_query_param('DiskId', DiskId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_PerformanceLevel(self): # String
		return self.get_query_params().get('PerformanceLevel')

	def set_PerformanceLevel(self, PerformanceLevel):  # String
		self.add_query_param('PerformanceLevel', PerformanceLevel)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_PerformanceControlOptions(self): # Struct
		return self.get_query_params().get('PerformanceControlOptions')

	def set_PerformanceControlOptions(self, PerformanceControlOptions):  # Struct
		if PerformanceControlOptions.get('IOPS') is not None:
			self.add_query_param('PerformanceControlOptions.IOPS', PerformanceControlOptions.get('IOPS'))
		if PerformanceControlOptions.get('Throughput') is not None:
			self.add_query_param('PerformanceControlOptions.Throughput', PerformanceControlOptions.get('Throughput'))
		if PerformanceControlOptions.get('Recover') is not None:
			self.add_query_param('PerformanceControlOptions.Recover', PerformanceControlOptions.get('Recover'))
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ProvisionedIops(self): # Long
		return self.get_query_params().get('ProvisionedIops')

	def set_ProvisionedIops(self, ProvisionedIops):  # Long
		self.add_query_param('ProvisionedIops', ProvisionedIops)
