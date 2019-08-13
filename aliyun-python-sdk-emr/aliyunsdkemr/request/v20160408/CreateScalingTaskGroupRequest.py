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
from aliyunsdkemr.endpoint import endpoint_data

class CreateScalingTaskGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateScalingTaskGroup','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DataDiskCategory(self):
		return self.get_query_params().get('DataDiskCategory')

	def set_DataDiskCategory(self,DataDiskCategory):
		self.add_query_param('DataDiskCategory',DataDiskCategory)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_MinSize(self):
		return self.get_query_params().get('MinSize')

	def set_MinSize(self,MinSize):
		self.add_query_param('MinSize',MinSize)

	def get_SpotStrategy(self):
		return self.get_query_params().get('SpotStrategy')

	def set_SpotStrategy(self,SpotStrategy):
		self.add_query_param('SpotStrategy',SpotStrategy)

	def get_DataDiskSize(self):
		return self.get_query_params().get('DataDiskSize')

	def set_DataDiskSize(self,DataDiskSize):
		self.add_query_param('DataDiskSize',DataDiskSize)

	def get_SpotPriceLimitss(self):
		return self.get_query_params().get('SpotPriceLimitss')

	def set_SpotPriceLimitss(self,SpotPriceLimitss):
		for i in range(len(SpotPriceLimitss)):	
			if SpotPriceLimitss[i].get('InstanceType') is not None:
				self.add_query_param('SpotPriceLimits.' + str(i + 1) + '.InstanceType' , SpotPriceLimitss[i].get('InstanceType'))
			if SpotPriceLimitss[i].get('PriceLimit') is not None:
				self.add_query_param('SpotPriceLimits.' + str(i + 1) + '.PriceLimit' , SpotPriceLimitss[i].get('PriceLimit'))


	def get_ScalingRules(self):
		return self.get_query_params().get('ScalingRules')

	def set_ScalingRules(self,ScalingRules):
		for i in range(len(ScalingRules)):	
			if ScalingRules[i].get('LaunchTime') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.LaunchTime' , ScalingRules[i].get('LaunchTime'))
			if ScalingRules[i].get('RuleCategory') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.RuleCategory' , ScalingRules[i].get('RuleCategory'))
			if ScalingRules[i].get('AdjustmentValue') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.AdjustmentValue' , ScalingRules[i].get('AdjustmentValue'))
			for j in range(len(ScalingRules[i].get('SchedulerTriggers'))):
				if ScalingRules[i].get('SchedulerTriggers')[j] is not None:
					self.add_query_param('ScalingRule.' + str(i + 1) + '.SchedulerTrigger.'+str(j + 1), ScalingRules[i].get('SchedulerTriggers')[j])
			if ScalingRules[i].get('AdjustmentType') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.AdjustmentType' , ScalingRules[i].get('AdjustmentType'))
			if ScalingRules[i].get('Cooldown') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.Cooldown' , ScalingRules[i].get('Cooldown'))
			if ScalingRules[i].get('RuleName') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.RuleName' , ScalingRules[i].get('RuleName'))
			if ScalingRules[i].get('LaunchExpirationTime') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.LaunchExpirationTime' , ScalingRules[i].get('LaunchExpirationTime'))
			if ScalingRules[i].get('RecurrenceValue') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.RecurrenceValue' , ScalingRules[i].get('RecurrenceValue'))
			if ScalingRules[i].get('RecurrenceEndTime') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.RecurrenceEndTime' , ScalingRules[i].get('RecurrenceEndTime'))
			for j in range(len(ScalingRules[i].get('CloudWatchTriggers'))):
				if ScalingRules[i].get('CloudWatchTriggers')[j] is not None:
					self.add_query_param('ScalingRule.' + str(i + 1) + '.CloudWatchTrigger.'+str(j + 1), ScalingRules[i].get('CloudWatchTriggers')[j])
			if ScalingRules[i].get('RecurrenceType') is not None:
				self.add_query_param('ScalingRule.' + str(i + 1) + '.RecurrenceType' , ScalingRules[i].get('RecurrenceType'))


	def get_ActiveRuleCategory(self):
		return self.get_query_params().get('ActiveRuleCategory')

	def set_ActiveRuleCategory(self,ActiveRuleCategory):
		self.add_query_param('ActiveRuleCategory',ActiveRuleCategory)

	def get_MaxSize(self):
		return self.get_query_params().get('MaxSize')

	def set_MaxSize(self,MaxSize):
		self.add_query_param('MaxSize',MaxSize)

	def get_DataDiskCount(self):
		return self.get_query_params().get('DataDiskCount')

	def set_DataDiskCount(self,DataDiskCount):
		self.add_query_param('DataDiskCount',DataDiskCount)

	def get_DefaultCooldown(self):
		return self.get_query_params().get('DefaultCooldown')

	def set_DefaultCooldown(self,DefaultCooldown):
		self.add_query_param('DefaultCooldown',DefaultCooldown)

	def get_PayType(self):
		return self.get_query_params().get('PayType')

	def set_PayType(self,PayType):
		self.add_query_param('PayType',PayType)

	def get_InstanceTypeLists(self):
		return self.get_query_params().get('InstanceTypeLists')

	def set_InstanceTypeLists(self,InstanceTypeLists):
		for i in range(len(InstanceTypeLists)):	
			if InstanceTypeLists[i] is not None:
				self.add_query_param('InstanceTypeList.' + str(i + 1) , InstanceTypeLists[i]);