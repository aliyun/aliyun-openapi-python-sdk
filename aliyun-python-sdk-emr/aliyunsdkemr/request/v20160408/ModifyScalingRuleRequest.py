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
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LaunchTime(self):
		return self.get_query_params().get('LaunchTime')

	def set_LaunchTime(self,LaunchTime):
		self.add_query_param('LaunchTime',LaunchTime)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_AdjustmentValue(self):
		return self.get_query_params().get('AdjustmentValue')

	def set_AdjustmentValue(self,AdjustmentValue):
		self.add_query_param('AdjustmentValue',AdjustmentValue)

	def get_AdjustmentType(self):
		return self.get_query_params().get('AdjustmentType')

	def set_AdjustmentType(self,AdjustmentType):
		self.add_query_param('AdjustmentType',AdjustmentType)

	def get_RuleName(self):
		return self.get_query_params().get('RuleName')

	def set_RuleName(self,RuleName):
		self.add_query_param('RuleName',RuleName)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ScalingRuleId(self):
		return self.get_query_params().get('ScalingRuleId')

	def set_ScalingRuleId(self,ScalingRuleId):
		self.add_query_param('ScalingRuleId',ScalingRuleId)

	def get_LaunchExpirationTime(self):
		return self.get_query_params().get('LaunchExpirationTime')

	def set_LaunchExpirationTime(self,LaunchExpirationTime):
		self.add_query_param('LaunchExpirationTime',LaunchExpirationTime)

	def get_RecurrenceValue(self):
		return self.get_query_params().get('RecurrenceValue')

	def set_RecurrenceValue(self,RecurrenceValue):
		self.add_query_param('RecurrenceValue',RecurrenceValue)

	def get_RecurrenceEndTime(self):
		return self.get_query_params().get('RecurrenceEndTime')

	def set_RecurrenceEndTime(self,RecurrenceEndTime):
		self.add_query_param('RecurrenceEndTime',RecurrenceEndTime)

	def get_CloudWatchTriggers(self):
		return self.get_query_params().get('CloudWatchTriggers')

	def set_CloudWatchTriggers(self,CloudWatchTriggers):
		for i in range(len(CloudWatchTriggers)):	
			if CloudWatchTriggers[i].get('Period') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.Period' , CloudWatchTriggers[i].get('Period'))
			if CloudWatchTriggers[i].get('EvaluationCount') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.EvaluationCount' , CloudWatchTriggers[i].get('EvaluationCount'))
			if CloudWatchTriggers[i].get('Threshold') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.Threshold' , CloudWatchTriggers[i].get('Threshold'))
			if CloudWatchTriggers[i].get('MetricName') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.MetricName' , CloudWatchTriggers[i].get('MetricName'))
			if CloudWatchTriggers[i].get('ComparisonOperator') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.ComparisonOperator' , CloudWatchTriggers[i].get('ComparisonOperator'))
			if CloudWatchTriggers[i].get('Statistics') is not None:
				self.add_query_param('CloudWatchTrigger.' + str(i + 1) + '.Statistics' , CloudWatchTriggers[i].get('Statistics'))


	def get_HostGroupId(self):
		return self.get_query_params().get('HostGroupId')

	def set_HostGroupId(self,HostGroupId):
		self.add_query_param('HostGroupId',HostGroupId)

	def get_SchedulerTriggers(self):
		return self.get_query_params().get('SchedulerTriggers')

	def set_SchedulerTriggers(self,SchedulerTriggers):
		for i in range(len(SchedulerTriggers)):	
			if SchedulerTriggers[i].get('LaunchTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(i + 1) + '.LaunchTime' , SchedulerTriggers[i].get('LaunchTime'))
			if SchedulerTriggers[i].get('LaunchExpirationTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(i + 1) + '.LaunchExpirationTime' , SchedulerTriggers[i].get('LaunchExpirationTime'))
			if SchedulerTriggers[i].get('RecurrenceValue') is not None:
				self.add_query_param('SchedulerTrigger.' + str(i + 1) + '.RecurrenceValue' , SchedulerTriggers[i].get('RecurrenceValue'))
			if SchedulerTriggers[i].get('RecurrenceEndTime') is not None:
				self.add_query_param('SchedulerTrigger.' + str(i + 1) + '.RecurrenceEndTime' , SchedulerTriggers[i].get('RecurrenceEndTime'))
			if SchedulerTriggers[i].get('RecurrenceType') is not None:
				self.add_query_param('SchedulerTrigger.' + str(i + 1) + '.RecurrenceType' , SchedulerTriggers[i].get('RecurrenceType'))


	def get_Cooldown(self):
		return self.get_query_params().get('Cooldown')

	def set_Cooldown(self,Cooldown):
		self.add_query_param('Cooldown',Cooldown)

	def get_RecurrenceType(self):
		return self.get_query_params().get('RecurrenceType')

	def set_RecurrenceType(self,RecurrenceType):
		self.add_query_param('RecurrenceType',RecurrenceType)