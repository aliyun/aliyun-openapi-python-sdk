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
from aliyunsdkoos.endpoint import endpoint_data
import json

class UpdateInstancePackageStateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'UpdateInstancePackageState','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TemplateVersion(self): # String
		return self.get_query_params().get('TemplateVersion')

	def set_TemplateVersion(self, TemplateVersion):  # String
		self.add_query_param('TemplateVersion', TemplateVersion)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_ConfigureAction(self): # String
		return self.get_query_params().get('ConfigureAction')

	def set_ConfigureAction(self, ConfigureAction):  # String
		self.add_query_param('ConfigureAction', ConfigureAction)
	def get_TemplateName(self): # String
		return self.get_query_params().get('TemplateName')

	def set_TemplateName(self, TemplateName):  # String
		self.add_query_param('TemplateName', TemplateName)
	def get_Parameters(self): # Map
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # Map
		self.add_query_param("Parameters", json.dumps(Parameters))
