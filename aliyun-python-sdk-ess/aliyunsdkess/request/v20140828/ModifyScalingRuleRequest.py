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
from aliyunsdkess.endpoint import endpoint_data

class ModifyScalingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'ModifyScalingRule','ess')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_StepAdjustments(self):
		return self.get_query_params().get('StepAdjustments')

	def set_StepAdjustments(self,StepAdjustments):
		for i in range(len(StepAdjustments)):	
			if StepAdjustments[i].get('MetricIntervalLowerBound') is not None:
				self.add_query_param('StepAdjustment.' + str(i + 1) + '.MetricIntervalLowerBound' , StepAdjustments[i].get('MetricIntervalLowerBound'))
			if StepAdjustments[i].get('MetricIntervalUpperBound') is not None:
				self.add_query_param('StepAdjustment.' + str(i + 1) + '.MetricIntervalUpperBound' , StepAdjustments[i].get('MetricIntervalUpperBound'))
			if StepAdjustments[i].get('ScalingAdjustment') is not None:
				self.add_query_param('StepAdjustment.' + str(i + 1) + '.ScalingAdjustment' , StepAdjustments[i].get('ScalingAdjustment'))


	def get_DisableScaleIn(self):
		return self.get_query_params().get('DisableScaleIn')

	def set_DisableScaleIn(self,DisableScaleIn):
		self.add_query_param('DisableScaleIn',DisableScaleIn)

	def get_ScalingRuleId(self):
		return self.get_query_params().get('ScalingRuleId')

	def set_ScalingRuleId(self,ScalingRuleId):
		self.add_query_param('ScalingRuleId',ScalingRuleId)

	def get_InitialMaxSize(self):
		return self.get_query_params().get('InitialMaxSize')

	def set_InitialMaxSize(self,InitialMaxSize):
		self.add_query_param('InitialMaxSize',InitialMaxSize)

	def get_ScalingRuleName(self):
		return self.get_query_params().get('ScalingRuleName')

	def set_ScalingRuleName(self,ScalingRuleName):
		self.add_query_param('ScalingRuleName',ScalingRuleName)

	def get_Cooldown(self):
		return self.get_query_params().get('Cooldown')

	def set_Cooldown(self,Cooldown):
		self.add_query_param('Cooldown',Cooldown)

	def get_PredictiveValueBehavior(self):
		return self.get_query_params().get('PredictiveValueBehavior')

	def set_PredictiveValueBehavior(self,PredictiveValueBehavior):
		self.add_query_param('PredictiveValueBehavior',PredictiveValueBehavior)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)

	def get_PredictiveScalingMode(self):
		return self.get_query_params().get('PredictiveScalingMode')

	def set_PredictiveScalingMode(self,PredictiveScalingMode):
		self.add_query_param('PredictiveScalingMode',PredictiveScalingMode)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_AdjustmentValue(self):
		return self.get_query_params().get('AdjustmentValue')

	def set_AdjustmentValue(self,AdjustmentValue):
		self.add_query_param('AdjustmentValue',AdjustmentValue)

	def get_EstimatedInstanceWarmup(self):
		return self.get_query_params().get('EstimatedInstanceWarmup')

	def set_EstimatedInstanceWarmup(self,EstimatedInstanceWarmup):
		self.add_query_param('EstimatedInstanceWarmup',EstimatedInstanceWarmup)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_PredictiveTaskBufferTime(self):
		return self.get_query_params().get('PredictiveTaskBufferTime')

	def set_PredictiveTaskBufferTime(self,PredictiveTaskBufferTime):
		self.add_query_param('PredictiveTaskBufferTime',PredictiveTaskBufferTime)

	def get_AdjustmentType(self):
		return self.get_query_params().get('AdjustmentType')

	def set_AdjustmentType(self,AdjustmentType):
		self.add_query_param('AdjustmentType',AdjustmentType)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PredictiveValueBuffer(self):
		return self.get_query_params().get('PredictiveValueBuffer')

	def set_PredictiveValueBuffer(self,PredictiveValueBuffer):
		self.add_query_param('PredictiveValueBuffer',PredictiveValueBuffer)

	def get_MinAdjustmentMagnitude(self):
		return self.get_query_params().get('MinAdjustmentMagnitude')

	def set_MinAdjustmentMagnitude(self,MinAdjustmentMagnitude):
		self.add_query_param('MinAdjustmentMagnitude',MinAdjustmentMagnitude)

	def get_TargetValue(self):
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self,TargetValue):
		self.add_query_param('TargetValue',TargetValue)