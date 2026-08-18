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

class DescribePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'DescribePrice','redisa')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_NodeType(self): # String
		return self.get_query_params().get('NodeType')

	def set_NodeType(self, NodeType):  # String
		self.add_query_param('NodeType', NodeType)
	def get_Instances(self): # String
		return self.get_query_params().get('Instances')

	def set_Instances(self, Instances):  # String
		self.add_query_param('Instances', Instances)
	def get_SecondaryZoneId(self): # String
		return self.get_query_params().get('SecondaryZoneId')

	def set_SecondaryZoneId(self, SecondaryZoneId):  # String
		self.add_query_param('SecondaryZoneId', SecondaryZoneId)
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_EngineVersion(self): # String
		return self.get_query_params().get('EngineVersion')

	def set_EngineVersion(self, EngineVersion):  # String
		self.add_query_param('EngineVersion', EngineVersion)
	def get_InstanceClass(self): # String
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self, InstanceClass):  # String
		self.add_query_param('InstanceClass', InstanceClass)
	def get_Capacity(self): # Long
		return self.get_query_params().get('Capacity')

	def set_Capacity(self, Capacity):  # Long
		self.add_query_param('Capacity', Capacity)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_BusinessInfo(self): # String
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self, BusinessInfo):  # String
		self.add_query_param('BusinessInfo', BusinessInfo)
	def get_ShardCount(self): # Integer
		return self.get_query_params().get('ShardCount')

	def set_ShardCount(self, ShardCount):  # Integer
		self.add_query_param('ShardCount', ShardCount)
	def get_Period(self): # Long
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Long
		self.add_query_param('Period', Period)
	def get_Quantity(self): # Long
		return self.get_query_params().get('Quantity')

	def set_Quantity(self, Quantity):  # Long
		self.add_query_param('Quantity', Quantity)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OrderParamOut(self): # String
		return self.get_query_params().get('OrderParamOut')

	def set_OrderParamOut(self, OrderParamOut):  # String
		self.add_query_param('OrderParamOut', OrderParamOut)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
	def get_ForceUpgrade(self): # Boolean
		return self.get_query_params().get('ForceUpgrade')

	def set_ForceUpgrade(self, ForceUpgrade):  # Boolean
		self.add_query_param('ForceUpgrade', ForceUpgrade)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
