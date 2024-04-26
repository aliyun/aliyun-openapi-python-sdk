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
import json

class ModifyCloudAssistantSettingsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'ModifyCloudAssistantSettings','ecs')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AgentUpgradeConfig(self): # Struct
		return self.get_query_params().get('AgentUpgradeConfig')

	def set_AgentUpgradeConfig(self, AgentUpgradeConfig):  # Struct
		self.add_query_param("AgentUpgradeConfig", json.dumps(AgentUpgradeConfig))
	def get_OssDeliveryConfig(self): # Struct
		return self.get_query_params().get('OssDeliveryConfig')

	def set_OssDeliveryConfig(self, OssDeliveryConfig):  # Struct
		self.add_query_param("OssDeliveryConfig", json.dumps(OssDeliveryConfig))
	def get_SettingType(self): # String
		return self.get_query_params().get('SettingType')

	def set_SettingType(self, SettingType):  # String
		self.add_query_param('SettingType', SettingType)
	def get_SlsDeliveryConfig(self): # Struct
		return self.get_query_params().get('SlsDeliveryConfig')

	def set_SlsDeliveryConfig(self, SlsDeliveryConfig):  # Struct
		self.add_query_param("SlsDeliveryConfig", json.dumps(SlsDeliveryConfig))
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
