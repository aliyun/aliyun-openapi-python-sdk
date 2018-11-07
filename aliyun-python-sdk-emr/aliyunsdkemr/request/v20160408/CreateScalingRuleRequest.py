# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateScalingRuleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateScalingRule')

	def get_LaunchTime(self):
		return self.get_query_params().get('LaunchTime')

	def set_LaunchTime(self,LaunchTime):
		self.add_query_param('LaunchTime',LaunchTime)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_RuleCategory(self):
		return self.get_query_params().get('RuleCategory')

	def set_RuleCategory(self,RuleCategory):
		self.add_query_param('RuleCategory',RuleCategory)

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

	def get_HostGroupId(self):
		return self.get_query_params().get('HostGroupId')

	def set_HostGroupId(self,HostGroupId):
		self.add_query_param('HostGroupId',HostGroupId)

	def get_Cooldown(self):
		return self.get_query_params().get('Cooldown')

	def set_Cooldown(self,Cooldown):
		self.add_query_param('Cooldown',Cooldown)

	def get_RecurrenceType(self):
		return self.get_query_params().get('RecurrenceType')

	def set_RecurrenceType(self,RecurrenceType):
		self.add_query_param('RecurrenceType',RecurrenceType)