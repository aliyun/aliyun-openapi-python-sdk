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
from aliyunsdkdds.endpoint import endpoint_data

class DescribeAvailabilityZonesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'DescribeAvailabilityZones','dds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_ReplicationFactor(self): # String
		return self.get_query_params().get('ReplicationFactor')

	def set_ReplicationFactor(self, ReplicationFactor):  # String
		self.add_query_param('ReplicationFactor', ReplicationFactor)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ExcludeZoneId(self): # String
		return self.get_query_params().get('ExcludeZoneId')

	def set_ExcludeZoneId(self, ExcludeZoneId):  # String
		self.add_query_param('ExcludeZoneId', ExcludeZoneId)
	def get_ExcludeSecondaryZoneId(self): # String
		return self.get_query_params().get('ExcludeSecondaryZoneId')

	def set_ExcludeSecondaryZoneId(self, ExcludeSecondaryZoneId):  # String
		self.add_query_param('ExcludeSecondaryZoneId', ExcludeSecondaryZoneId)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_MongoType(self): # String
		return self.get_query_params().get('MongoType')

	def set_MongoType(self, MongoType):  # String
		self.add_query_param('MongoType', MongoType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DBInstanceClass(self): # String
		return self.get_query_params().get('DBInstanceClass')

	def set_DBInstanceClass(self, DBInstanceClass):  # String
		self.add_query_param('DBInstanceClass', DBInstanceClass)
	def get_StorageSupport(self): # String
		return self.get_query_params().get('StorageSupport')

	def set_StorageSupport(self, StorageSupport):  # String
		self.add_query_param('StorageSupport', StorageSupport)
	def get_DbType(self): # String
		return self.get_query_params().get('DbType')

	def set_DbType(self, DbType):  # String
		self.add_query_param('DbType', DbType)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
