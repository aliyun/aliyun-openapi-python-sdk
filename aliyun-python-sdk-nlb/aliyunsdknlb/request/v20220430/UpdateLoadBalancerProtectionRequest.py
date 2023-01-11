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
from aliyunsdknlb.endpoint import endpoint_data

class UpdateLoadBalancerProtectionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Nlb', '2022-04-30', 'UpdateLoadBalancerProtection','nlb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DeletionProtectionReason(self): # String
		return self.get_body_params().get('DeletionProtectionReason')

	def set_DeletionProtectionReason(self, DeletionProtectionReason):  # String
		self.add_body_params('DeletionProtectionReason', DeletionProtectionReason)
	def get_ModificationProtectionReason(self): # String
		return self.get_body_params().get('ModificationProtectionReason')

	def set_ModificationProtectionReason(self, ModificationProtectionReason):  # String
		self.add_body_params('ModificationProtectionReason', ModificationProtectionReason)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_DeletionProtectionEnabled(self): # Boolean
		return self.get_body_params().get('DeletionProtectionEnabled')

	def set_DeletionProtectionEnabled(self, DeletionProtectionEnabled):  # Boolean
		self.add_body_params('DeletionProtectionEnabled', DeletionProtectionEnabled)
	def get_DryRun(self): # Boolean
		return self.get_body_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_body_params('DryRun', DryRun)
	def get_ModificationProtectionStatus(self): # String
		return self.get_body_params().get('ModificationProtectionStatus')

	def set_ModificationProtectionStatus(self, ModificationProtectionStatus):  # String
		self.add_body_params('ModificationProtectionStatus', ModificationProtectionStatus)
	def get_LoadBalancerId(self): # String
		return self.get_body_params().get('LoadBalancerId')

	def set_LoadBalancerId(self, LoadBalancerId):  # String
		self.add_body_params('LoadBalancerId', LoadBalancerId)
