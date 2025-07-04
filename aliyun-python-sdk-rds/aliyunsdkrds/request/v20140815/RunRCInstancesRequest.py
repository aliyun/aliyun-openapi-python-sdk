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
from aliyunsdkrds.endpoint import endpoint_data
import json

class RunRCInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'RunRCInstances','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CreateExtraParam(self): # String
		return self.get_query_params().get('CreateExtraParam')

	def set_CreateExtraParam(self, CreateExtraParam):  # String
		self.add_query_param('CreateExtraParam', CreateExtraParam)
	def get_SecurityEnhancementStrategy(self): # String
		return self.get_query_params().get('SecurityEnhancementStrategy')

	def set_SecurityEnhancementStrategy(self, SecurityEnhancementStrategy):  # String
		self.add_query_param('SecurityEnhancementStrategy', SecurityEnhancementStrategy)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_SystemDisk(self): # Struct
		return self.get_query_params().get('SystemDisk')

	def set_SystemDisk(self, SystemDisk):  # Struct
		self.add_query_param("SystemDisk", json.dumps(SystemDisk))
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_Period(self): # Integer
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # Integer
		self.add_query_param('Period', Period)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_CreateAckEdgeParam(self): # Struct
		return self.get_query_params().get('CreateAckEdgeParam')

	def set_CreateAckEdgeParam(self, CreateAckEdgeParam):  # Struct
		self.add_query_param("CreateAckEdgeParam", json.dumps(CreateAckEdgeParam))
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_SpotStrategy(self): # String
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self, SpotStrategy):  # String
		self.add_query_param('SpotStrategy', SpotStrategy)
	def get_PeriodUnit(self): # String
		return self.get_query_params().get('PeriodUnit')

	def set_PeriodUnit(self, PeriodUnit):  # String
		self.add_query_param('PeriodUnit', PeriodUnit)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_AutoRenew(self): # Boolean
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self, AutoRenew):  # Boolean
		self.add_query_param('AutoRenew', AutoRenew)
	def get_PromotionCode(self): # String
		return self.get_query_params().get('PromotionCode')

	def set_PromotionCode(self, PromotionCode):  # String
		self.add_query_param('PromotionCode', PromotionCode)
	def get_InternetChargeType(self): # String
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self, InternetChargeType):  # String
		self.add_query_param('InternetChargeType', InternetChargeType)
	def get_CreateMode(self): # String
		return self.get_query_params().get('CreateMode')

	def set_CreateMode(self, CreateMode):  # String
		self.add_query_param('CreateMode', CreateMode)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_ImageId(self): # String
		return self.get_query_params().get('ImageId')

	def set_ImageId(self, ImageId):  # String
		self.add_query_param('ImageId', ImageId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_IoOptimized(self): # String
		return self.get_query_params().get('IoOptimized')

	def set_IoOptimized(self, IoOptimized):  # String
		self.add_query_param('IoOptimized', IoOptimized)
	def get_InternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):  # Integer
		self.add_query_param('InternetMaxBandwidthOut', InternetMaxBandwidthOut)
	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_AutoUseCoupon(self): # Boolean
		return self.get_query_params().get('AutoUseCoupon')

	def set_AutoUseCoupon(self, AutoUseCoupon):  # Boolean
		self.add_query_param('AutoUseCoupon', AutoUseCoupon)
	def get_UserDataInBase64(self): # Boolean
		return self.get_query_params().get('UserDataInBase64')

	def set_UserDataInBase64(self, UserDataInBase64):  # Boolean
		self.add_query_param('UserDataInBase64', UserDataInBase64)
	def get_SupportCase(self): # String
		return self.get_query_params().get('SupportCase')

	def set_SupportCase(self, SupportCase):  # String
		self.add_query_param('SupportCase', SupportCase)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceChargeType(self): # String
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self, InstanceChargeType):  # String
		self.add_query_param('InstanceChargeType', InstanceChargeType)
	def get_DeploymentSetId(self): # String
		return self.get_query_params().get('DeploymentSetId')

	def set_DeploymentSetId(self, DeploymentSetId):  # String
		self.add_query_param('DeploymentSetId', DeploymentSetId)
	def get_Amount(self): # Integer
		return self.get_query_params().get('Amount')

	def set_Amount(self, Amount):  # Integer
		self.add_query_param('Amount', Amount)
	def get_AutoPay(self): # Boolean
		return self.get_query_params().get('AutoPay')

	def set_AutoPay(self, AutoPay):  # Boolean
		self.add_query_param('AutoPay', AutoPay)
	def get_DataDisk(self): # Array
		return self.get_query_params().get('DataDisk')

	def set_DataDisk(self, DataDisk):  # Array
		self.add_query_param("DataDisk", json.dumps(DataDisk))
