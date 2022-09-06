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
import json

class CreateAppInstanceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'CreateAppInstanceGroup')
		self.set_method('POST')

	def get_BizRegionId(self): # String
		return self.get_body_params().get('BizRegionId')

	def set_BizRegionId(self, BizRegionId):  # String
		self.add_body_params('BizRegionId', BizRegionId)
	def get_ProductType(self): # String
		return self.get_body_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_body_params('ProductType', ProductType)
	def get_SessionTimeout(self): # Integer
		return self.get_body_params().get('SessionTimeout')

	def set_SessionTimeout(self, SessionTimeout):  # Integer
		self.add_body_params('SessionTimeout', SessionTimeout)
	def get_ChargeResourceMode(self): # String
		return self.get_body_params().get('ChargeResourceMode')

	def set_ChargeResourceMode(self, ChargeResourceMode):  # String
		self.add_body_params('ChargeResourceMode', ChargeResourceMode)
	def get_AppCenterImageId(self): # String
		return self.get_body_params().get('AppCenterImageId')

	def set_AppCenterImageId(self, AppCenterImageId):  # String
		self.add_body_params('AppCenterImageId', AppCenterImageId)
	def get_UserInfo(self): # Struct
		return self.get_body_params().get('UserInfo')

	def set_UserInfo(self, UserInfo):  # Struct
		self.add_body_params("UserInfo", json.dumps(UserInfo))
	def get_Period(self): # Integer
		return self.get_body_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_body_params('Period', Period)
	def get_AutoPay(self): # Boolean
		return self.get_body_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_body_params('AutoPay', AutoPay)
	def get_NodePool(self): # Struct
		return self.get_body_params().get('NodePool')

	def set_NodePool(self, NodePool):  # Struct
		self.add_body_params("NodePool", json.dumps(NodePool))
	def get_PromotionId(self): # String
		return self.get_body_params().get('PromotionId')

	def set_PromotionId(self, PromotionId):  # String
		self.add_body_params('PromotionId', PromotionId)
	def get_Userss(self): # RepeatList
		return self.get_body_params().get('Users')

	def set_Userss(self, Users):  # RepeatList
		for depth1 in range(len(Users)):
			self.add_body_params('Users.' + str(depth1 + 1), Users[depth1])
	def get_AppInstanceGroupName(self): # String
		return self.get_body_params().get('AppInstanceGroupName')

	def set_AppInstanceGroupName(self, AppInstanceGroupName):  # String
		self.add_body_params('AppInstanceGroupName', AppInstanceGroupName)
	def get_PeriodUnit(self): # String
		return self.get_body_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_body_params('PeriodUnit', PeriodUnit)
	def get_AutoRenew(self): # Boolean
		return self.get_body_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_body_params('AutoRenew', AutoRenew)
	def get_ChargeType(self): # String
		return self.get_body_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_body_params('ChargeType', ChargeType)
