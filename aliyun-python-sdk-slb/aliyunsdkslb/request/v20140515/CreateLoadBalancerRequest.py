# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateLoadBalancerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Slb', '2014-05-15', 'CreateLoadBalancer','slb')

	def get_access_key_id(self):
		return self.get_query_params().get('access_key_id')

	def set_access_key_id(self,access_key_id):
		self.add_query_param('access_key_id',access_key_id)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_AddressIPVersion(self):
		return self.get_query_params().get('AddressIPVersion')

	def set_AddressIPVersion(self,AddressIPVersion):
		self.add_query_param('AddressIPVersion',AddressIPVersion)

	def get_MasterZoneId(self):
		return self.get_query_params().get('MasterZoneId')

	def set_MasterZoneId(self,MasterZoneId):
		self.add_query_param('MasterZoneId',MasterZoneId)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_LoadBalancerName(self):
		return self.get_query_params().get('LoadBalancerName')

	def set_LoadBalancerName(self,LoadBalancerName):
		self.add_query_param('LoadBalancerName',LoadBalancerName)

	def get_AddressType(self):
		return self.get_query_params().get('AddressType')

	def set_AddressType(self,AddressType):
		self.add_query_param('AddressType',AddressType)

	def get_SlaveZoneId(self):
		return self.get_query_params().get('SlaveZoneId')

	def set_SlaveZoneId(self,SlaveZoneId):
		self.add_query_param('SlaveZoneId',SlaveZoneId)

	def get_LoadBalancerSpec(self):
		return self.get_query_params().get('LoadBalancerSpec')

	def set_LoadBalancerSpec(self,LoadBalancerSpec):
		self.add_query_param('LoadBalancerSpec',LoadBalancerSpec)

	def get_AutoPay(self):
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self,AutoPay):
		self.add_query_param('AutoPay',AutoPay)

	def get_Address(self):
		return self.get_query_params().get('Address')

	def set_Address(self,Address):
		self.add_query_param('Address',Address)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_Bandwidth(self):
		return self.get_query_params().get('Bandwidth')

	def set_Bandwidth(self,Bandwidth):
		self.add_query_param('Bandwidth',Bandwidth)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Tags(self):
		return self.get_query_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_query_param('Tags',Tags)

	def get_VSwitchId(self):
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_query_param('VSwitchId',VSwitchId)

	def get_EnableVpcVipFlow(self):
		return self.get_query_params().get('EnableVpcVipFlow')

	def set_EnableVpcVipFlow(self,EnableVpcVipFlow):
		self.add_query_param('EnableVpcVipFlow',EnableVpcVipFlow)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_PricingCycle(self):
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self,PricingCycle):
		self.add_query_param('PricingCycle',PricingCycle)

	def get_Ratio(self):
		return self.get_query_params().get('Ratio')

	def set_Ratio(self,Ratio):
		self.add_query_param('Ratio',Ratio)