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
from aliyunsdkpolardb.endpoint import endpoint_data

class ModifyDBClusterAndNodesParametersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'ModifyDBClusterAndNodesParameters','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PlannedEndTime(self): # String
		return self.get_query_params().get('PlannedEndTime')

	def set_PlannedEndTime(self, PlannedEndTime):  # String
		self.add_query_param('PlannedEndTime', PlannedEndTime)
	def get_DBNodeIds(self): # String
		return self.get_query_params().get('DBNodeIds')

	def set_DBNodeIds(self, DBNodeIds):  # String
		self.add_query_param('DBNodeIds', DBNodeIds)
	def get_ParameterGroupId(self): # String
		return self.get_query_params().get('ParameterGroupId')

	def set_ParameterGroupId(self, ParameterGroupId):  # String
		self.add_query_param('ParameterGroupId', ParameterGroupId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_DBClusterId(self): # String
		return self.get_query_params().get('DBClusterId')

	def set_DBClusterId(self, DBClusterId):  # String
		self.add_query_param('DBClusterId', DBClusterId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PlannedStartTime(self): # String
		return self.get_query_params().get('PlannedStartTime')

	def set_PlannedStartTime(self, PlannedStartTime):  # String
		self.add_query_param('PlannedStartTime', PlannedStartTime)
	def get_StandbyClusterIdListNeedToSync(self): # String
		return self.get_query_params().get('StandbyClusterIdListNeedToSync')

	def set_StandbyClusterIdListNeedToSync(self, StandbyClusterIdListNeedToSync):  # String
		self.add_query_param('StandbyClusterIdListNeedToSync', StandbyClusterIdListNeedToSync)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
	def get_FromTimeService(self): # Boolean
		return self.get_query_params().get('FromTimeService')

	def set_FromTimeService(self, FromTimeService):  # Boolean
		self.add_query_param('FromTimeService', FromTimeService)
