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
from aliyunsdkros.endpoint import endpoint_data

class CreateStackInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ROS', '2019-09-10', 'CreateStackInstances','ros')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_StackGroupName(self):
		return self.get_query_params().get('StackGroupName')

	def set_StackGroupName(self,StackGroupName):
		self.add_query_param('StackGroupName',StackGroupName)

	def get_OperationDescription(self):
		return self.get_query_params().get('OperationDescription')

	def set_OperationDescription(self,OperationDescription):
		self.add_query_param('OperationDescription',OperationDescription)

	def get_OperationPreferences(self):
		return self.get_query_params().get('OperationPreferences')

	def set_OperationPreferences(self,OperationPreferences):
		self.add_query_param('OperationPreferences',OperationPreferences)

	def get_DisableRollback(self):
		return self.get_query_params().get('DisableRollback')

	def set_DisableRollback(self,DisableRollback):
		self.add_query_param('DisableRollback',DisableRollback)

	def get_RegionIds(self):
		return self.get_query_params().get('RegionIds')

	def set_RegionIds(self,RegionIds):
		self.add_query_param('RegionIds',RegionIds)

	def get_AccountIds(self):
		return self.get_query_params().get('AccountIds')

	def set_AccountIds(self,AccountIds):
		self.add_query_param('AccountIds',AccountIds)

	def get_ParameterOverrides(self):
		return self.get_query_params().get('ParameterOverrides')

	def set_ParameterOverrides(self, ParameterOverridess):
		for depth1 in range(len(ParameterOverridess)):
			if ParameterOverridess[depth1].get('ParameterValue') is not None:
				self.add_query_param('ParameterOverrides.' + str(depth1 + 1) + '.ParameterValue', ParameterOverridess[depth1].get('ParameterValue'))
			if ParameterOverridess[depth1].get('ParameterKey') is not None:
				self.add_query_param('ParameterOverrides.' + str(depth1 + 1) + '.ParameterKey', ParameterOverridess[depth1].get('ParameterKey'))