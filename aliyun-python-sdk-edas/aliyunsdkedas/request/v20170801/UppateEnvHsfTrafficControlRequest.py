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

class UppateEnvHsfTrafficControlRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UppateEnvHsfTrafficControl','Edas')
		self.set_uri_pattern('/pop/v5/gray/env_hsf_traffic_control')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ParamTypes(self):
		return self.get_body_params().get('ParamTypes')

	def set_ParamTypes(self,ParamTypes):
		self.add_body_params('ParamTypes', ParamTypes)

	def get_Condition(self):
		return self.get_body_params().get('Condition')

	def set_Condition(self,Condition):
		self.add_body_params('Condition', Condition)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_LabelAdviceName(self):
		return self.get_body_params().get('LabelAdviceName')

	def set_LabelAdviceName(self,LabelAdviceName):
		self.add_body_params('LabelAdviceName', LabelAdviceName)

	def get_PointcutName(self):
		return self.get_body_params().get('PointcutName')

	def set_PointcutName(self,PointcutName):
		self.add_body_params('PointcutName', PointcutName)

	def get_ServiceName(self):
		return self.get_body_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_body_params('ServiceName', ServiceName)

	def get_TriggerPolicy(self):
		return self.get_body_params().get('TriggerPolicy')

	def set_TriggerPolicy(self,TriggerPolicy):
		self.add_body_params('TriggerPolicy', TriggerPolicy)

	def get_Group(self):
		return self.get_body_params().get('Group')

	def set_Group(self,Group):
		self.add_body_params('Group', Group)

	def get_MethodName(self):
		return self.get_body_params().get('MethodName')

	def set_MethodName(self,MethodName):
		self.add_body_params('MethodName', MethodName)