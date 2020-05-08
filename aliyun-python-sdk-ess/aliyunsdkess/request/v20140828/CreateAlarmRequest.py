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

class CreateAlarmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateAlarm','ess')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MetricType(self):
		return self.get_query_params().get('MetricType')

	def set_MetricType(self,MetricType):
		self.add_query_param('MetricType',MetricType)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AlarmActions(self):
		return self.get_query_params().get('AlarmActions')

	def set_AlarmActions(self,AlarmActions):
		for i in range(len(AlarmActions)):	
			if AlarmActions[i] is not None:
				self.add_query_param('AlarmAction.' + str(i + 1) , AlarmActions[i]);

	def get_Threshold(self):
		return self.get_query_params().get('Threshold')

	def set_Threshold(self,Threshold):
		self.add_query_param('Threshold',Threshold)

	def get_EvaluationCount(self):
		return self.get_query_params().get('EvaluationCount')

	def set_EvaluationCount(self,EvaluationCount):
		self.add_query_param('EvaluationCount',EvaluationCount)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)

	def get_Dimensions(self):
		return self.get_query_params().get('Dimensions')

	def set_Dimensions(self,Dimensions):
		for i in range(len(Dimensions)):	
			if Dimensions[i].get('DimensionValue') is not None:
				self.add_query_param('Dimension.' + str(i + 1) + '.DimensionValue' , Dimensions[i].get('DimensionValue'))
			if Dimensions[i].get('DimensionKey') is not None:
				self.add_query_param('Dimension.' + str(i + 1) + '.DimensionKey' , Dimensions[i].get('DimensionKey'))


	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_ComparisonOperator(self):
		return self.get_query_params().get('ComparisonOperator')

	def set_ComparisonOperator(self,ComparisonOperator):
		self.add_query_param('ComparisonOperator',ComparisonOperator)

	def get_Statistics(self):
		return self.get_query_params().get('Statistics')

	def set_Statistics(self,Statistics):
		self.add_query_param('Statistics',Statistics)