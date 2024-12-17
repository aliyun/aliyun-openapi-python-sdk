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
from aliyunsdkr_kvstore.endpoint import endpoint_data

class ModifyInstanceConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'ModifyInstanceConfig','redisa')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ParamSemisyncReplTimeout(self): # String
		return self.get_query_params().get('ParamSemisyncReplTimeout')

	def set_ParamSemisyncReplTimeout(self, ParamSemisyncReplTimeout):  # String
		self.add_query_param('ParamSemisyncReplTimeout', ParamSemisyncReplTimeout)
	def get_ParamNoLooseSentinelPasswordFreeCommands(self): # String
		return self.get_query_params().get('ParamNoLooseSentinelPasswordFreeCommands')

	def set_ParamNoLooseSentinelPasswordFreeCommands(self, ParamNoLooseSentinelPasswordFreeCommands):  # String
		self.add_query_param('ParamNoLooseSentinelPasswordFreeCommands', ParamNoLooseSentinelPasswordFreeCommands)
	def get_ParamNoLooseSentinelPasswordFreeAccess(self): # String
		return self.get_query_params().get('ParamNoLooseSentinelPasswordFreeAccess')

	def set_ParamNoLooseSentinelPasswordFreeAccess(self, ParamNoLooseSentinelPasswordFreeAccess):  # String
		self.add_query_param('ParamNoLooseSentinelPasswordFreeAccess', ParamNoLooseSentinelPasswordFreeAccess)
	def get_ParamReplMode(self): # String
		return self.get_query_params().get('ParamReplMode')

	def set_ParamReplMode(self, ParamReplMode):  # String
		self.add_query_param('ParamReplMode', ParamReplMode)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_ParamNoLooseSentinelEnabled(self): # String
		return self.get_query_params().get('ParamNoLooseSentinelEnabled')

	def set_ParamNoLooseSentinelEnabled(self, ParamNoLooseSentinelEnabled):  # String
		self.add_query_param('ParamNoLooseSentinelEnabled', ParamNoLooseSentinelEnabled)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_ParamSentinelCompatEnable(self): # String
		return self.get_query_params().get('ParamSentinelCompatEnable')

	def set_ParamSentinelCompatEnable(self, ParamSentinelCompatEnable):  # String
		self.add_query_param('ParamSentinelCompatEnable', ParamSentinelCompatEnable)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Config(self): # String
		return self.get_query_params().get('Config')

	def set_Config(self, Config):  # String
		self.add_query_param('Config', Config)
