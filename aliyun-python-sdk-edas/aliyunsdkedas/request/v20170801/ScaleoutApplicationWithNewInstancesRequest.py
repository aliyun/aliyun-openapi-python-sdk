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

class ScaleoutApplicationWithNewInstancesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'ScaleoutApplicationWithNewInstances','edas')
		self.set_uri_pattern('/pop/v5/scaling/scale_out')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AutoRenewPeriod(self):
		return self.get_query_params().get('AutoRenewPeriod')

	def set_AutoRenewPeriod(self,AutoRenewPeriod):
		self.add_query_param('AutoRenewPeriod',AutoRenewPeriod)

	def get_TemplateInstanceId(self):
		return self.get_query_params().get('TemplateInstanceId')

	def set_TemplateInstanceId(self,TemplateInstanceId):
		self.add_query_param('TemplateInstanceId',TemplateInstanceId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_InstanceChargePeriodUnit(self):
		return self.get_query_params().get('InstanceChargePeriodUnit')

	def set_InstanceChargePeriodUnit(self,InstanceChargePeriodUnit):
		self.add_query_param('InstanceChargePeriodUnit',InstanceChargePeriodUnit)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ScalingNum(self):
		return self.get_query_params().get('ScalingNum')

	def set_ScalingNum(self,ScalingNum):
		self.add_query_param('ScalingNum',ScalingNum)

	def get_TemplateId(self):
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self,TemplateId):
		self.add_query_param('TemplateId',TemplateId)

	def get_ScalingPolicy(self):
		return self.get_query_params().get('ScalingPolicy')

	def set_ScalingPolicy(self,ScalingPolicy):
		self.add_query_param('ScalingPolicy',ScalingPolicy)

	def get_TemplateVersion(self):
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self,TemplateVersion):
		self.add_query_param('TemplateVersion',TemplateVersion)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_InstanceChargePeriod(self):
		return self.get_query_params().get('InstanceChargePeriod')

	def set_InstanceChargePeriod(self,InstanceChargePeriod):
		self.add_query_param('InstanceChargePeriod',InstanceChargePeriod)

	def get_InstanceChargeType(self):
		return self.get_query_params().get('InstanceChargeType')

	def set_InstanceChargeType(self,InstanceChargeType):
		self.add_query_param('InstanceChargeType',InstanceChargeType)