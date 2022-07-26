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

class UpdateStateConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'UpdateStateConfiguration','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ScheduleType(self): # String
		return self.get_query_params().get('ScheduleType')

	def set_ScheduleType(self, ScheduleType):  # String
		self.add_query_param('ScheduleType', ScheduleType)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Targets(self): # String
		return self.get_query_params().get('Targets')

	def set_Targets(self, Targets):  # String
		self.add_query_param('Targets', Targets)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_ScheduleExpression(self): # String
		return self.get_query_params().get('ScheduleExpression')

	def set_ScheduleExpression(self, ScheduleExpression):  # String
		self.add_query_param('ScheduleExpression', ScheduleExpression)
	def get_ConfigureMode(self): # String
		return self.get_query_params().get('ConfigureMode')

	def set_ConfigureMode(self, ConfigureMode):  # String
		self.add_query_param('ConfigureMode', ConfigureMode)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_Parameters(self): # String
		return self.get_query_params().get('Parameters')

	def set_Parameters(self, Parameters):  # String
		self.add_query_param('Parameters', Parameters)
	def get_StateConfigurationId(self): # String
		return self.get_query_params().get('StateConfigurationId')

	def set_StateConfigurationId(self, StateConfigurationId):  # String
		self.add_query_param('StateConfigurationId', StateConfigurationId)
