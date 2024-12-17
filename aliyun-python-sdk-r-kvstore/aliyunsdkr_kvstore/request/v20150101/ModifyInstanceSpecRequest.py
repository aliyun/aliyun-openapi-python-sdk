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

class ModifyInstanceSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'R-kvstore', '2015-01-01', 'ModifyInstanceSpec','redisa')
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
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SlaveReadOnlyCount(self): # Integer
		return self.get_query_params().get('SlaveReadOnlyCount')

	def set_SlaveReadOnlyCount(self, SlaveReadOnlyCount):  # Integer
		self.add_query_param('SlaveReadOnlyCount', SlaveReadOnlyCount)
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_Storage(self): # Integer
		return self.get_query_params().get('Storage')

	def set_Storage(self, Storage):  # Integer
		self.add_query_param('Storage', Storage)
	def get_InstanceClass(self): # String
		return self.get_query_params().get('InstanceClass')

	def set_InstanceClass(self, InstanceClass):  # String
		self.add_query_param('InstanceClass', InstanceClass)
	def get_StorageType(self): # String
		return self.get_query_params().get('StorageType')

	def set_StorageType(self, StorageType):  # String
		self.add_query_param('StorageType', StorageType)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_EffectiveTime(self): # String
		return self.get_query_params().get('EffectiveTime')

	def set_EffectiveTime(self, EffectiveTime):  # String
		self.add_query_param('EffectiveTime', EffectiveTime)
	def get_SourceBiz(self): # String
		return self.get_query_params().get('SourceBiz')

	def set_SourceBiz(self, SourceBiz):  # String
		self.add_query_param('SourceBiz', SourceBiz)
	def get_BusinessInfo(self): # String
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self, BusinessInfo):  # String
		self.add_query_param('BusinessInfo', BusinessInfo)
	def get_ShardCount(self): # Integer
		return self.get_query_params().get('ShardCount')

	def set_ShardCount(self, ShardCount):  # Integer
		self.add_query_param('ShardCount', ShardCount)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_MajorVersion(self): # String
		return self.get_query_params().get('MajorVersion')

	def set_MajorVersion(self, MajorVersion):  # String
		self.add_query_param('MajorVersion', MajorVersion)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ForceTrans(self): # Boolean
		return self.get_query_params().get('ForceTrans')

	def set_ForceTrans(self, ForceTrans):  # Boolean
		self.add_query_param('ForceTrans', ForceTrans)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ReadOnlyCount(self): # Integer
		return self.get_query_params().get('ReadOnlyCount')

	def set_ReadOnlyCount(self, ReadOnlyCount):  # Integer
		self.add_query_param('ReadOnlyCount', ReadOnlyCount)
	def get_ForceUpgrade(self): # Boolean
		return self.get_query_params().get('ForceUpgrade')

	def set_ForceUpgrade(self, ForceUpgrade):  # Boolean
		self.add_query_param('ForceUpgrade', ForceUpgrade)
	def get_SlaveReplicaCount(self): # Integer
		return self.get_query_params().get('SlaveReplicaCount')

	def set_SlaveReplicaCount(self, SlaveReplicaCount):  # Integer
		self.add_query_param('SlaveReplicaCount', SlaveReplicaCount)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
	def get_ReplicaCount(self): # Integer
		return self.get_query_params().get('ReplicaCount')

	def set_ReplicaCount(self, ReplicaCount):  # Integer
		self.add_query_param('ReplicaCount', ReplicaCount)
