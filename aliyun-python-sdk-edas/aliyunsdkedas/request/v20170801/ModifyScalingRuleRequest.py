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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class ModifyScalingRuleRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'ModifyScalingRule','Edas')
		self.set_uri_pattern('/pop/v5/app/scaling_rules')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InStep(self): # Integer
		return self.get_query_params().get('InStep')

	def set_InStep(self, InStep):  # Integer
		self.add_query_param('InStep', InStep)
	def get_OutInstanceNum(self): # Integer
		return self.get_query_params().get('OutInstanceNum')

	def set_OutInstanceNum(self, OutInstanceNum):  # Integer
		self.add_query_param('OutInstanceNum', OutInstanceNum)
	def get_OutRT(self): # Integer
		return self.get_query_params().get('OutRT')

	def set_OutRT(self, OutRT):  # Integer
		self.add_query_param('OutRT', OutRT)
	def get_InInstanceNum(self): # Integer
		return self.get_query_params().get('InInstanceNum')

	def set_InInstanceNum(self, InInstanceNum):  # Integer
		self.add_query_param('InInstanceNum', InInstanceNum)
	def get_VSwitchIds(self): # String
		return self.get_query_params().get('VSwitchIds')

	def set_VSwitchIds(self, VSwitchIds):  # String
		self.add_query_param('VSwitchIds', VSwitchIds)
	def get_TemplateInstanceId(self): # String
		return self.get_query_params().get('TemplateInstanceId')

	def set_TemplateInstanceId(self, TemplateInstanceId):  # String
		self.add_query_param('TemplateInstanceId', TemplateInstanceId)
	def get_AcceptEULA(self): # Boolean
		return self.get_query_params().get('AcceptEULA')

	def set_AcceptEULA(self, AcceptEULA):  # Boolean
		self.add_query_param('AcceptEULA', AcceptEULA)
	def get_OutStep(self): # Integer
		return self.get_query_params().get('OutStep')

	def set_OutStep(self, OutStep):  # Integer
		self.add_query_param('OutStep', OutStep)
	def get_OutCPU(self): # Integer
		return self.get_query_params().get('OutCPU')

	def set_OutCPU(self, OutCPU):  # Integer
		self.add_query_param('OutCPU', OutCPU)
	def get_KeyPairName(self): # String
		return self.get_query_params().get('KeyPairName')

	def set_KeyPairName(self, KeyPairName):  # String
		self.add_query_param('KeyPairName', KeyPairName)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_TemplateVersion(self): # Integer
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self, TemplateVersion):  # Integer
		self.add_query_param('TemplateVersion', TemplateVersion)
	def get_InCondition(self): # String
		return self.get_query_params().get('InCondition')

	def set_InCondition(self, InCondition):  # String
		self.add_query_param('InCondition', InCondition)
	def get_InRT(self): # Integer
		return self.get_query_params().get('InRT')

	def set_InRT(self, InRT):  # Integer
		self.add_query_param('InRT', InRT)
	def get_InCpu(self): # Integer
		return self.get_query_params().get('InCpu')

	def set_InCpu(self, InCpu):  # Integer
		self.add_query_param('InCpu', InCpu)
	def get_OutDuration(self): # Integer
		return self.get_query_params().get('OutDuration')

	def set_OutDuration(self, OutDuration):  # Integer
		self.add_query_param('OutDuration', OutDuration)
	def get_MultiAzPolicy(self): # String
		return self.get_query_params().get('MultiAzPolicy')

	def set_MultiAzPolicy(self, MultiAzPolicy):  # String
		self.add_query_param('MultiAzPolicy', MultiAzPolicy)
	def get_OutLoad(self): # Integer
		return self.get_query_params().get('OutLoad')

	def set_OutLoad(self, OutLoad):  # Integer
		self.add_query_param('OutLoad', OutLoad)
	def get_InLoad(self): # Integer
		return self.get_query_params().get('InLoad')

	def set_InLoad(self, InLoad):  # Integer
		self.add_query_param('InLoad', InLoad)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_ResourceFrom(self): # String
		return self.get_query_params().get('ResourceFrom')

	def set_ResourceFrom(self, ResourceFrom):  # String
		self.add_query_param('ResourceFrom', ResourceFrom)
	def get_OutEnable(self): # Boolean
		return self.get_query_params().get('OutEnable')

	def set_OutEnable(self, OutEnable):  # Boolean
		self.add_query_param('OutEnable', OutEnable)
	def get_TemplateId(self): # String
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # String
		self.add_query_param('TemplateId', TemplateId)
	def get_ScalingPolicy(self): # String
		return self.get_query_params().get('ScalingPolicy')

	def set_ScalingPolicy(self, ScalingPolicy):  # String
		self.add_query_param('ScalingPolicy', ScalingPolicy)
	def get_OutCondition(self): # String
		return self.get_query_params().get('OutCondition')

	def set_OutCondition(self, OutCondition):  # String
		self.add_query_param('OutCondition', OutCondition)
	def get_InDuration(self): # Integer
		return self.get_query_params().get('InDuration')

	def set_InDuration(self, InDuration):  # Integer
		self.add_query_param('InDuration', InDuration)
	def get_InEnable(self): # Boolean
		return self.get_query_params().get('InEnable')

	def set_InEnable(self, InEnable):  # Boolean
		self.add_query_param('InEnable', InEnable)
	def get_AppId(self): # String
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_query_param('AppId', AppId)
	def get_VpcId(self): # String
		return self.get_query_params().get('VpcId')

	def set_VpcId(self, VpcId):  # String
		self.add_query_param('VpcId', VpcId)
	def get_TemplateInstanceName(self): # String
		return self.get_query_params().get('TemplateInstanceName')

	def set_TemplateInstanceName(self, TemplateInstanceName):  # String
		self.add_query_param('TemplateInstanceName', TemplateInstanceName)
