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
from aliyunsdkiot.endpoint import endpoint_data

class UpdateEdgeDriverVersionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'UpdateEdgeDriverVersion','Iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfigCheckRule(self):
		return self.get_query_params().get('ConfigCheckRule')

	def set_ConfigCheckRule(self,ConfigCheckRule):
		self.add_query_param('ConfigCheckRule',ConfigCheckRule)

	def get_EdgeVersion(self):
		return self.get_query_params().get('EdgeVersion')

	def set_EdgeVersion(self,EdgeVersion):
		self.add_query_param('EdgeVersion',EdgeVersion)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_DriverId(self):
		return self.get_query_params().get('DriverId')

	def set_DriverId(self,DriverId):
		self.add_query_param('DriverId',DriverId)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_ContainerConfig(self):
		return self.get_query_params().get('ContainerConfig')

	def set_ContainerConfig(self,ContainerConfig):
		self.add_query_param('ContainerConfig',ContainerConfig)

	def get_DriverVersion(self):
		return self.get_query_params().get('DriverVersion')

	def set_DriverVersion(self,DriverVersion):
		self.add_query_param('DriverVersion',DriverVersion)

	def get_DriverConfig(self):
		return self.get_query_params().get('DriverConfig')

	def set_DriverConfig(self,DriverConfig):
		self.add_query_param('DriverConfig',DriverConfig)

	def get_SourceConfig(self):
		return self.get_query_params().get('SourceConfig')

	def set_SourceConfig(self,SourceConfig):
		self.add_query_param('SourceConfig',SourceConfig)