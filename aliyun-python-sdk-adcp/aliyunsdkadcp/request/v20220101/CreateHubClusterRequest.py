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
from aliyunsdkadcp.endpoint import endpoint_data

class CreateHubClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'adcp', '2022-01-01', 'CreateHubCluster','adcp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Profile(self): # String
		return self.get_body_params().get('Profile')

	def set_Profile(self, Profile):  # String
		self.add_body_params('Profile', Profile)
	def get_VSwitches(self): # String
		return self.get_body_params().get('VSwitches')

	def set_VSwitches(self, VSwitches):  # String
		self.add_body_params('VSwitches', VSwitches)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_ArgoServerEnabled(self): # Boolean
		return self.get_body_params().get('ArgoServerEnabled')

	def set_ArgoServerEnabled(self, ArgoServerEnabled):  # Boolean
		self.add_body_params('ArgoServerEnabled', ArgoServerEnabled)
	def get_WorkflowScheduleMode(self): # String
		return self.get_body_params().get('WorkflowScheduleMode')

	def set_WorkflowScheduleMode(self, WorkflowScheduleMode):  # String
		self.add_body_params('WorkflowScheduleMode', WorkflowScheduleMode)
	def get_ApiServerPublicEip(self): # Boolean
		return self.get_body_params().get('ApiServerPublicEip')

	def set_ApiServerPublicEip(self, ApiServerPublicEip):  # Boolean
		self.add_body_params('ApiServerPublicEip', ApiServerPublicEip)
	def get_AuditLogEnabled(self): # Boolean
		return self.get_body_params().get('AuditLogEnabled')

	def set_AuditLogEnabled(self, AuditLogEnabled):  # Boolean
		self.add_body_params('AuditLogEnabled', AuditLogEnabled)
	def get_PriceLimit(self): # String
		return self.get_body_params().get('PriceLimit')

	def set_PriceLimit(self, PriceLimit):  # String
		self.add_body_params('PriceLimit', PriceLimit)
	def get_IsEnterpriseSecurityGroup(self): # Boolean
		return self.get_body_params().get('IsEnterpriseSecurityGroup')

	def set_IsEnterpriseSecurityGroup(self, IsEnterpriseSecurityGroup):  # Boolean
		self.add_body_params('IsEnterpriseSecurityGroup', IsEnterpriseSecurityGroup)
	def get_VpcId(self): # String
		return self.get_body_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_body_params('VpcId', VpcId)
