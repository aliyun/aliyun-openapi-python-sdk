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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class ModifyTenantPrimaryZoneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'ModifyTenantPrimaryZone','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserVSwitchId(self): # String
		return self.get_body_params().get('UserVSwitchId')

	def set_UserVSwitchId(self, UserVSwitchId):  # String
		self.add_body_params('UserVSwitchId', UserVSwitchId)
	def get_MasterIntranetAddressZone(self): # String
		return self.get_body_params().get('MasterIntranetAddressZone')

	def set_MasterIntranetAddressZone(self, MasterIntranetAddressZone):  # String
		self.add_body_params('MasterIntranetAddressZone', MasterIntranetAddressZone)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_TenantEndpointId(self): # String
		return self.get_body_params().get('TenantEndpointId')

	def set_TenantEndpointId(self, TenantEndpointId):  # String
		self.add_body_params('TenantEndpointId', TenantEndpointId)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_PrimaryZone(self): # String
		return self.get_body_params().get('PrimaryZone')

	def set_PrimaryZone(self, PrimaryZone):  # String
		self.add_body_params('PrimaryZone', PrimaryZone)
