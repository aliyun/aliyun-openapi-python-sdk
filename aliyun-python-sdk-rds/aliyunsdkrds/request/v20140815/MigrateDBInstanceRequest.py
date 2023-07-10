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
from aliyunsdkrds.endpoint import endpoint_data

class MigrateDBInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'MigrateDBInstance')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_SpecifiedTime(self): # String
		return self.get_query_params().get('SpecifiedTime')

	def set_SpecifiedTime(self, SpecifiedTime):  # String
		self.add_query_param('SpecifiedTime', SpecifiedTime)
	def get_TargetDedicatedHostIdForSlave(self): # String
		return self.get_query_params().get('TargetDedicatedHostIdForSlave')

	def set_TargetDedicatedHostIdForSlave(self, TargetDedicatedHostIdForSlave):  # String
		self.add_query_param('TargetDedicatedHostIdForSlave', TargetDedicatedHostIdForSlave)
	def get_ZoneIdForFollower(self): # String
		return self.get_query_params().get('ZoneIdForFollower')

	def set_ZoneIdForFollower(self, ZoneIdForFollower):  # String
		self.add_query_param('ZoneIdForFollower', ZoneIdForFollower)
	def get_EffectiveTime(self): # String
		return self.get_query_params().get('EffectiveTime')

	def set_EffectiveTime(self, EffectiveTime):  # String
		self.add_query_param('EffectiveTime', EffectiveTime)
	def get_TargetDedicatedHostIdForMaster(self): # String
		return self.get_query_params().get('TargetDedicatedHostIdForMaster')

	def set_TargetDedicatedHostIdForMaster(self, TargetDedicatedHostIdForMaster):  # String
		self.add_query_param('TargetDedicatedHostIdForMaster', TargetDedicatedHostIdForMaster)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DedicatedHostGroupId(self): # String
		return self.get_query_params().get('DedicatedHostGroupId')

	def set_DedicatedHostGroupId(self, DedicatedHostGroupId):  # String
		self.add_query_param('DedicatedHostGroupId', DedicatedHostGroupId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_ZoneIdForLog(self): # String
		return self.get_query_params().get('ZoneIdForLog')

	def set_ZoneIdForLog(self, ZoneIdForLog):  # String
		self.add_query_param('ZoneIdForLog', ZoneIdForLog)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
