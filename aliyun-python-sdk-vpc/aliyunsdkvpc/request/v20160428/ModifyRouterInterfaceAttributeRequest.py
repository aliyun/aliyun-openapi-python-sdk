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

class ModifyRouterInterfaceAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyRouterInterfaceAttribute','Vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OppositeRouterId(self):
		return self.get_query_params().get('OppositeRouterId')

	def set_OppositeRouterId(self,OppositeRouterId):
		self.add_query_param('OppositeRouterId',OppositeRouterId)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_HealthCheckTargetIp(self):
		return self.get_query_params().get('HealthCheckTargetIp')

	def set_HealthCheckTargetIp(self,HealthCheckTargetIp):
		self.add_query_param('HealthCheckTargetIp',HealthCheckTargetIp)

	def get_OppositeInterfaceId(self):
		return self.get_query_params().get('OppositeInterfaceId')

	def set_OppositeInterfaceId(self,OppositeInterfaceId):
		self.add_query_param('OppositeInterfaceId',OppositeInterfaceId)

	def get_HcThreshold(self):
		return self.get_query_params().get('HcThreshold')

	def set_HcThreshold(self,HcThreshold):
		self.add_query_param('HcThreshold',HcThreshold)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_DeleteHealthCheckIp(self):
		return self.get_query_params().get('DeleteHealthCheckIp')

	def set_DeleteHealthCheckIp(self,DeleteHealthCheckIp):
		self.add_query_param('DeleteHealthCheckIp',DeleteHealthCheckIp)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RouterInterfaceId(self):
		return self.get_query_params().get('RouterInterfaceId')

	def set_RouterInterfaceId(self,RouterInterfaceId):
		self.add_query_param('RouterInterfaceId',RouterInterfaceId)

	def get_OppositeInterfaceOwnerId(self):
		return self.get_query_params().get('OppositeInterfaceOwnerId')

	def set_OppositeInterfaceOwnerId(self,OppositeInterfaceOwnerId):
		self.add_query_param('OppositeInterfaceOwnerId',OppositeInterfaceOwnerId)

	def get_HealthCheckSourceIp(self):
		return self.get_query_params().get('HealthCheckSourceIp')

	def set_HealthCheckSourceIp(self,HealthCheckSourceIp):
		self.add_query_param('HealthCheckSourceIp',HealthCheckSourceIp)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_OppositeRouterType(self):
		return self.get_query_params().get('OppositeRouterType')

	def set_OppositeRouterType(self,OppositeRouterType):
		self.add_query_param('OppositeRouterType',OppositeRouterType)

	def get_HcRate(self):
		return self.get_query_params().get('HcRate')

	def set_HcRate(self,HcRate):
		self.add_query_param('HcRate',HcRate)