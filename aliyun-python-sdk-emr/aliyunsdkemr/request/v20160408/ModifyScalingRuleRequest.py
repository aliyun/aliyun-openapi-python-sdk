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

class ModifyScalingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyScalingRule','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_ScalingRuleId(self):
		return self.get_query_params().get('ScalingRuleId')

	def set_ScalingRuleId(self,ScalingRuleId):
		self.add_query_param('ScalingRuleId',ScalingRuleId)

	def get_RecurrenceEndTime(self):
		return self.get_query_params().get('RecurrenceEndTime')

	def set_RecurrenceEndTime(self,RecurrenceEndTime):
		self.add_query_param('RecurrenceEndTime',RecurrenceEndTime)

	def get_CloudWatchTriggers(self):
		return self.get_query_params().get('CloudWatchTriggers')

	def set_CloudWatchTriggers(self, CloudWatchTriggers):
		for depth1 in range(len(CloudWatchTriggers)):
			if CloudWatchTriggers[depth1].get('Period') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.Period', CloudWatchTriggers[depth1].get('Period'))
			if CloudWatchTriggers[depth1].get('EvaluationCount') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.EvaluationCount', CloudWatchTriggers[depth1].get('EvaluationCount'))
			if CloudWatchTriggers[depth1].get('Threshold') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.Threshold', CloudWatchTriggers[depth1].get('Threshold'))
			if CloudWatchTriggers[depth1].get('MetricName') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.MetricName', CloudWatchTriggers[depth1].get('MetricName'))
			if CloudWatchTriggers[depth1].get('ComparisonOperator') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.ComparisonOperator', CloudWatchTriggers[depth1].get('ComparisonOperator'))
			if CloudWatchTriggers[depth1].get('Statistics') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(depth1 + 1) + '.Statistics', CloudWatchTriggers[depth1].get('Statistics'))

	def get_TimeoutWithGrace(self):
		return self.get_query_params().get('TimeoutWithGrace')

	def set_TimeoutWithGrace(self,TimeoutWithGrace):
		self.add_query_param('TimeoutWithGrace',TimeoutWithGrace)

	def get_Cooldown(self):
		return self.get_query_params().get('Cooldown')

	def set_Cooldown(self,Cooldown):
		self.add_query_param('Cooldown',Cooldown)

	def get_LaunchTime(self):
		return self.get_query_params().get('LaunchTime')

	def set_LaunchTime(self,LaunchTime):
		self.add_query_param('LaunchTime',LaunchTime)

	def get_WithGrace(self):
		return self.get_query_params().get('WithGrace')

	def set_WithGrace(self,WithGrace):
		self.add_query_param('WithGrace',WithGrace)

	def get_AdjustmentValue(self):
		return self.get_query_params().get('AdjustmentValue')

	def set_AdjustmentValue(self,AdjustmentValue):
		self.add_query_param('AdjustmentValue',AdjustmentValue)

	def get_AdjustmentType(self):
		return self.get_query_params().get('AdjustmentType')

	def set_AdjustmentType(self,AdjustmentType):
		self.add_query_param('AdjustmentType',AdjustmentType)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_LaunchExpirationTime(self):
		return self.get_query_params().get('LaunchExpirationTime')

	def set_LaunchExpirationTime(self,LaunchExpirationTime):
		self.add_query_param('LaunchExpirationTime',LaunchExpirationTime)

	def get_RecurrenceValue(self):
		return self.get_query_params().get('RecurrenceValue')

	def set_RecurrenceValue(self,RecurrenceValue):
		self.add_query_param('RecurrenceValue',RecurrenceValue)

	def get_HostGroupId(self):
		return self.get_query_params().get('HostGroupId')

	def set_HostGroupId(self,HostGroupId):
		self.add_query_param('HostGroupId',HostGroupId)

	def get_SchedulerTriggers(self):
		return self.get_query_params().get('SchedulerTriggers')

	def set_SchedulerTriggers(self, SchedulerTriggers):
		for depth1 in range(len(SchedulerTriggers)):
			if SchedulerTriggers[depth1].get('LaunchTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(depth1 + 1) + '.LaunchTime', SchedulerTriggers[depth1].get('LaunchTime'))
			if SchedulerTriggers[depth1].get('LaunchExpirationTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(depth1 + 1) + '.LaunchExpirationTime', SchedulerTriggers[depth1].get('LaunchExpirationTime'))
			if SchedulerTriggers[depth1].get('RecurrenceValue') is not None:
				self.add_query_param('SchedulerTrigger.' + str(depth1 + 1) + '.RecurrenceValue', SchedulerTriggers[depth1].get('RecurrenceValue'))
			if SchedulerTriggers[depth1].get('RecurrenceEndTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(depth1 + 1) + '.RecurrenceEndTime', SchedulerTriggers[depth1].get('RecurrenceEndTime'))
			if SchedulerTriggers[depth1].get('RecurrenceType') is not None:
				self.add_query_param('SchedulerTrigger.' + str(depth1 + 1) + '.RecurrenceType', SchedulerTriggers[depth1].get('RecurrenceType'))

	def get_RecurrenceType(self):
		return self.get_query_params().get('RecurrenceType')

	def set_RecurrenceType(self,RecurrenceType):
		self.add_query_param('RecurrenceType',RecurrenceType)