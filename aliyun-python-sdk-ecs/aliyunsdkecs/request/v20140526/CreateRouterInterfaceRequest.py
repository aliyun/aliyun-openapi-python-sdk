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

class CreateRouterInterfaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'CreateRouterInterface','ecs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AccessPointId(self):
		return self.get_query_params().get('AccessPointId')

	def set_AccessPointId(self,AccessPointId):
		self.add_query_param('AccessPointId',AccessPointId)

	def get_OppositeRouterId(self):
		return self.get_query_params().get('OppositeRouterId')

	def set_OppositeRouterId(self,OppositeRouterId):
		self.add_query_param('OppositeRouterId',OppositeRouterId)

	def get_OppositeAccessPointId(self):
		return self.get_query_params().get('OppositeAccessPointId')

	def set_OppositeAccessPointId(self,OppositeAccessPointId):
		self.add_query_param('OppositeAccessPointId',OppositeAccessPointId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Role(self):
		return self.get_query_params().get('Role')

	def set_Role(self,Role):
		self.add_query_param('Role',Role)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_HealthCheckTargetIp(self):
		return self.get_query_params().get('HealthCheckTargetIp')

	def set_HealthCheckTargetIp(self,HealthCheckTargetIp):
		self.add_query_param('HealthCheckTargetIp',HealthCheckTargetIp)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Spec(self):
		return self.get_query_params().get('Spec')

	def set_Spec(self,Spec):
		self.add_query_param('Spec',Spec)

	def get_UserCidr(self):
		return self.get_query_params().get('UserCidr')

	def set_UserCidr(self,UserCidr):
		self.add_query_param('UserCidr',UserCidr)

	def get_OppositeInterfaceId(self):
		return self.get_query_params().get('OppositeInterfaceId')

	def set_OppositeInterfaceId(self,OppositeInterfaceId):
		self.add_query_param('OppositeInterfaceId',OppositeInterfaceId)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OppositeRegionId(self):
		return self.get_query_params().get('OppositeRegionId')

	def set_OppositeRegionId(self,OppositeRegionId):
		self.add_query_param('OppositeRegionId',OppositeRegionId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_OppositeInterfaceOwnerId(self):
		return self.get_query_params().get('OppositeInterfaceOwnerId')

	def set_OppositeInterfaceOwnerId(self,OppositeInterfaceOwnerId):
		self.add_query_param('OppositeInterfaceOwnerId',OppositeInterfaceOwnerId)

	def get_RouterType(self):
		return self.get_query_params().get('RouterType')

	def set_RouterType(self,RouterType):
		self.add_query_param('RouterType',RouterType)

	def get_HealthCheckSourceIp(self):
		return self.get_query_params().get('HealthCheckSourceIp')

	def set_HealthCheckSourceIp(self,HealthCheckSourceIp):
		self.add_query_param('HealthCheckSourceIp',HealthCheckSourceIp)

	def get_RouterId(self):
		return self.get_query_params().get('RouterId')

	def set_RouterId(self,RouterId):
		self.add_query_param('RouterId',RouterId)

	def get_OppositeRouterType(self):
		return self.get_query_params().get('OppositeRouterType')

	def set_OppositeRouterType(self,OppositeRouterType):
		self.add_query_param('OppositeRouterType',OppositeRouterType)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)