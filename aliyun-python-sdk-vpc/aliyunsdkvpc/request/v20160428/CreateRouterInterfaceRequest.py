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

class CreateRouterInterfaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'CreateRouterInterface','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AccessPointId(self): # String
		return self.get_query_params().get('AccessPointId')

	def set_AccessPointId(self, AccessPointId):  # String
		self.add_query_param('AccessPointId', AccessPointId)
	def get_OppositeRouterId(self): # String
		return self.get_query_params().get('OppositeRouterId')

	def set_OppositeRouterId(self, OppositeRouterId):  # String
		self.add_query_param('OppositeRouterId', OppositeRouterId)
	def get_OppositeAccessPointId(self): # String
		return self.get_query_params().get('OppositeAccessPointId')

	def set_OppositeAccessPointId(self, OppositeAccessPointId):  # String
		self.add_query_param('OppositeAccessPointId', OppositeAccessPointId)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_Role(self): # String
		return self.get_query_params().get('Role')

	def set_Role(self, Role):  # String
		self.add_query_param('Role', Role)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_HealthCheckTargetIp(self): # String
		return self.get_query_params().get('HealthCheckTargetIp')

	def set_HealthCheckTargetIp(self, HealthCheckTargetIp):  # String
		self.add_query_param('HealthCheckTargetIp', HealthCheckTargetIp)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Spec(self): # String
		return self.get_query_params().get('Spec')

	def set_Spec(self, Spec):  # String
		self.add_query_param('Spec', Spec)
	def get_FastLinkMode(self): # Boolean
		return self.get_query_params().get('FastLinkMode')

	def set_FastLinkMode(self, FastLinkMode):  # Boolean
		self.add_query_param('FastLinkMode', FastLinkMode)
	def get_OppositeInterfaceId(self): # String
		return self.get_query_params().get('OppositeInterfaceId')

	def set_OppositeInterfaceId(self, OppositeInterfaceId):  # String
		self.add_query_param('OppositeInterfaceId', OppositeInterfaceId)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OppositeRegionId(self): # String
		return self.get_query_params().get('OppositeRegionId')

	def set_OppositeRegionId(self, OppositeRegionId):  # String
		self.add_query_param('OppositeRegionId', OppositeRegionId)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_OppositeInterfaceOwnerId(self): # String
		return self.get_query_params().get('OppositeInterfaceOwnerId')

	def set_OppositeInterfaceOwnerId(self, OppositeInterfaceOwnerId):  # String
		self.add_query_param('OppositeInterfaceOwnerId', OppositeInterfaceOwnerId)
	def get_RouterType(self): # String
		return self.get_query_params().get('RouterType')

	def set_RouterType(self, RouterType):  # String
		self.add_query_param('RouterType', RouterType)
	def get_HealthCheckSourceIp(self): # String
		return self.get_query_params().get('HealthCheckSourceIp')

	def set_HealthCheckSourceIp(self, HealthCheckSourceIp):  # String
		self.add_query_param('HealthCheckSourceIp', HealthCheckSourceIp)
	def get_RouterId(self): # String
		return self.get_query_params().get('RouterId')

	def set_RouterId(self, RouterId):  # String
		self.add_query_param('RouterId', RouterId)
	def get_OppositeRouterType(self): # String
		return self.get_query_params().get('OppositeRouterType')

	def set_OppositeRouterType(self, OppositeRouterType):  # String
		self.add_query_param('OppositeRouterType', OppositeRouterType)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
