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
from aliyunsdkvpc.endpoint import endpoint_data

class UpdateTrafficMirrorSessionAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'UpdateTrafficMirrorSessionAttribute','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TrafficMirrorTargetType(self): # String
		return self.get_query_params().get('TrafficMirrorTargetType')

	def set_TrafficMirrorTargetType(self, TrafficMirrorTargetType):  # String
		self.add_query_param('TrafficMirrorTargetType', TrafficMirrorTargetType)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Enabled(self): # Boolean
		return self.get_query_params().get('Enabled')

	def set_Enabled(self, Enabled):  # Boolean
		self.add_query_param('Enabled', Enabled)
	def get_TrafficMirrorSessionName(self): # String
		return self.get_query_params().get('TrafficMirrorSessionName')

	def set_TrafficMirrorSessionName(self, TrafficMirrorSessionName):  # String
		self.add_query_param('TrafficMirrorSessionName', TrafficMirrorSessionName)
	def get_TrafficMirrorSessionDescription(self): # String
		return self.get_query_params().get('TrafficMirrorSessionDescription')

	def set_TrafficMirrorSessionDescription(self, TrafficMirrorSessionDescription):  # String
		self.add_query_param('TrafficMirrorSessionDescription', TrafficMirrorSessionDescription)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_TrafficMirrorSessionId(self): # String
		return self.get_query_params().get('TrafficMirrorSessionId')

	def set_TrafficMirrorSessionId(self, TrafficMirrorSessionId):  # String
		self.add_query_param('TrafficMirrorSessionId', TrafficMirrorSessionId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_Priority(self): # Integer
		return self.get_query_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_query_param('Priority', Priority)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TrafficMirrorTargetId(self): # String
		return self.get_query_params().get('TrafficMirrorTargetId')

	def set_TrafficMirrorTargetId(self, TrafficMirrorTargetId):  # String
		self.add_query_param('TrafficMirrorTargetId', TrafficMirrorTargetId)
	def get_TrafficMirrorFilterId(self): # String
		return self.get_query_params().get('TrafficMirrorFilterId')

	def set_TrafficMirrorFilterId(self, TrafficMirrorFilterId):  # String
		self.add_query_param('TrafficMirrorFilterId', TrafficMirrorFilterId)
	def get_VirtualNetworkId(self): # Integer
		return self.get_query_params().get('VirtualNetworkId')

	def set_VirtualNetworkId(self, VirtualNetworkId):  # Integer
		self.add_query_param('VirtualNetworkId', VirtualNetworkId)
