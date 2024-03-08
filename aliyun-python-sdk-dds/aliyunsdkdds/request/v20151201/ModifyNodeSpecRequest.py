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
from aliyunsdkdds.endpoint import endpoint_data

class ModifyNodeSpecRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dds', '2015-12-01', 'ModifyNodeSpec','dds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ReadonlyReplicas(self): # Integer
		return self.get_query_params().get('ReadonlyReplicas')

	def set_ReadonlyReplicas(self, ReadonlyReplicas):  # Integer
		self.add_query_param('ReadonlyReplicas', ReadonlyReplicas)
	def get_CouponNo(self): # String
		return self.get_query_params().get('CouponNo')

	def set_CouponNo(self, CouponNo):  # String
		self.add_query_param('CouponNo', CouponNo)
	def get_NodeClass(self): # String
		return self.get_query_params().get('NodeClass')

	def set_NodeClass(self, NodeClass):  # String
		self.add_query_param('NodeClass', NodeClass)
	def get_EffectiveTime(self): # String
		return self.get_query_params().get('EffectiveTime')

	def set_EffectiveTime(self, EffectiveTime):  # String
		self.add_query_param('EffectiveTime', EffectiveTime)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_SwitchTime(self): # String
		return self.get_query_params().get('SwitchTime')

	def set_SwitchTime(self, SwitchTime):  # String
		self.add_query_param('SwitchTime', SwitchTime)
	def get_NodeId(self): # String
		return self.get_query_params().get('NodeId')

	def set_NodeId(self, NodeId):  # String
		self.add_query_param('NodeId', NodeId)
	def get_BusinessInfo(self): # String
		return self.get_query_params().get('BusinessInfo')

	def set_BusinessInfo(self, BusinessInfo):  # String
		self.add_query_param('BusinessInfo', BusinessInfo)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_FromApp(self): # String
		return self.get_query_params().get('FromApp')

	def set_FromApp(self, FromApp):  # String
		self.add_query_param('FromApp', FromApp)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_NodeStorage(self): # Integer
		return self.get_query_params().get('NodeStorage')

	def set_NodeStorage(self, NodeStorage):  # Integer
		self.add_query_param('NodeStorage', NodeStorage)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_OrderType(self): # String
		return self.get_query_params().get('OrderType')

	def set_OrderType(self, OrderType):  # String
		self.add_query_param('OrderType', OrderType)
