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
from aliyunsdkvpcpeer.endpoint import endpoint_data

class CreateVpcPeerConnectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VpcPeer', '2022-01-01', 'CreateVpcPeerConnection','vpcpeer')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_AcceptingAliUid(self): # Long
		return self.get_body_params().get('AcceptingAliUid')

	def set_AcceptingAliUid(self, AcceptingAliUid):  # Long
		self.add_body_params('AcceptingAliUid', AcceptingAliUid)
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_AcceptingRegionId(self): # String
		return self.get_body_params().get('AcceptingRegionId')

	def set_AcceptingRegionId(self, AcceptingRegionId):  # String
		self.add_body_params('AcceptingRegionId', AcceptingRegionId)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_AcceptingVpcId(self): # String
		return self.get_body_params().get('AcceptingVpcId')

	def set_AcceptingVpcId(self, AcceptingVpcId):  # String
		self.add_body_params('AcceptingVpcId', AcceptingVpcId)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
