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

class CreateScalingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateScalingRule','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AlarmDimensions(self): # RepeatList
		return self.get_query_params().get('AlarmDimension')

	def set_AlarmDimensions(self, AlarmDimension):  # RepeatList
		for depth1 in range(len(AlarmDimension)):
			if AlarmDimension[depth1].get('DimensionValue') is not None:
				self.add_query_param('AlarmDimension.' + str(depth1 + 1) + '.DimensionValue', AlarmDimension[depth1].get('DimensionValue'))
			if AlarmDimension[depth1].get('DimensionKey') is not None:
				self.add_query_param('AlarmDimension.' + str(depth1 + 1) + '.DimensionKey', AlarmDimension[depth1].get('DimensionKey'))
	def get_StepAdjustments(self): # RepeatList
		return self.get_query_params().get('StepAdjustment')

	def set_StepAdjustments(self, StepAdjustment):  # RepeatList
		for depth1 in range(len(StepAdjustment)):
			if StepAdjustment[depth1].get('MetricIntervalUpperBound') is not None:
				self.add_query_param('StepAdjustment.' + str(depth1 + 1) + '.MetricIntervalUpperBound', StepAdjustment[depth1].get('MetricIntervalUpperBound'))
			if StepAdjustment[depth1].get('MetricIntervalLowerBound') is not None:
				self.add_query_param('StepAdjustment.' + str(depth1 + 1) + '.MetricIntervalLowerBound', StepAdjustment[depth1].get('MetricIntervalLowerBound'))
			if StepAdjustment[depth1].get('ScalingAdjustment') is not None:
				self.add_query_param('StepAdjustment.' + str(depth1 + 1) + '.ScalingAdjustment', StepAdjustment[depth1].get('ScalingAdjustment'))
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_DisableScaleIn(self): # Boolean
		return self.get_query_params().get('DisableScaleIn')

	def set_DisableScaleIn(self, DisableScaleIn):  # Boolean
		self.add_query_param('DisableScaleIn', DisableScaleIn)
	def get_InitialMaxSize(self): # Integer
		return self.get_query_params().get('InitialMaxSize')

	def set_InitialMaxSize(self, InitialMaxSize):  # Integer
		self.add_query_param('InitialMaxSize', InitialMaxSize)
	def get_ScalingRuleName(self): # String
		return self.get_query_params().get('ScalingRuleName')

	def set_ScalingRuleName(self, ScalingRuleName):  # String
		self.add_query_param('ScalingRuleName', ScalingRuleName)
	def get_Cooldown(self): # Integer
		return self.get_query_params().get('Cooldown')

	def set_Cooldown(self, Cooldown):  # Integer
		self.add_query_param('Cooldown', Cooldown)
	def get_PredictiveValueBehavior(self): # String
		return self.get_query_params().get('PredictiveValueBehavior')

	def set_PredictiveValueBehavior(self, PredictiveValueBehavior):  # String
		self.add_query_param('PredictiveValueBehavior', PredictiveValueBehavior)
	def get_ScaleInEvaluationCount(self): # Integer
		return self.get_query_params().get('ScaleInEvaluationCount')

	def set_ScaleInEvaluationCount(self, ScaleInEvaluationCount):  # Integer
		self.add_query_param('ScaleInEvaluationCount', ScaleInEvaluationCount)
	def get_ScalingRuleType(self): # String
		return self.get_query_params().get('ScalingRuleType')

	def set_ScalingRuleType(self, ScalingRuleType):  # String
		self.add_query_param('ScalingRuleType', ScalingRuleType)
	def get_MetricName(self): # String
		return self.get_query_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_query_param('MetricName', MetricName)
	def get_PredictiveScalingMode(self): # String
		return self.get_query_params().get('PredictiveScalingMode')

	def set_PredictiveScalingMode(self, PredictiveScalingMode):  # String
		self.add_query_param('PredictiveScalingMode', PredictiveScalingMode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_AdjustmentValue(self): # Integer
		return self.get_query_params().get('AdjustmentValue')

	def set_AdjustmentValue(self, AdjustmentValue):  # Integer
		self.add_query_param('AdjustmentValue', AdjustmentValue)
	def get_EstimatedInstanceWarmup(self): # Integer
		return self.get_query_params().get('EstimatedInstanceWarmup')

	def set_EstimatedInstanceWarmup(self, EstimatedInstanceWarmup):  # Integer
		self.add_query_param('EstimatedInstanceWarmup', EstimatedInstanceWarmup)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_PredictiveTaskBufferTime(self): # Integer
		return self.get_query_params().get('PredictiveTaskBufferTime')

	def set_PredictiveTaskBufferTime(self, PredictiveTaskBufferTime):  # Integer
		self.add_query_param('PredictiveTaskBufferTime', PredictiveTaskBufferTime)
	def get_AdjustmentType(self): # String
		return self.get_query_params().get('AdjustmentType')

	def set_AdjustmentType(self, AdjustmentType):  # String
		self.add_query_param('AdjustmentType', AdjustmentType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PredictiveValueBuffer(self): # Integer
		return self.get_query_params().get('PredictiveValueBuffer')

	def set_PredictiveValueBuffer(self, PredictiveValueBuffer):  # Integer
		self.add_query_param('PredictiveValueBuffer', PredictiveValueBuffer)
	def get_ScaleOutEvaluationCount(self): # Integer
		return self.get_query_params().get('ScaleOutEvaluationCount')

	def set_ScaleOutEvaluationCount(self, ScaleOutEvaluationCount):  # Integer
		self.add_query_param('ScaleOutEvaluationCount', ScaleOutEvaluationCount)
	def get_MinAdjustmentMagnitude(self): # Integer
		return self.get_query_params().get('MinAdjustmentMagnitude')

	def set_MinAdjustmentMagnitude(self, MinAdjustmentMagnitude):  # Integer
		self.add_query_param('MinAdjustmentMagnitude', MinAdjustmentMagnitude)
	def get_TargetValue(self): # Float
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self, TargetValue):  # Float
		self.add_query_param('TargetValue', TargetValue)
