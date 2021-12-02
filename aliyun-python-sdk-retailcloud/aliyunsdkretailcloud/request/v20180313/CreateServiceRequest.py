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
from aliyunsdkretailcloud.endpoint import endpoint_data

class CreateServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'CreateService')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Headless(self): # Boolean
		return self.get_query_params().get('Headless')

	def set_Headless(self, Headless):  # Boolean
		self.add_query_param('Headless', Headless)
	def get_ServiceType(self): # String
		return self.get_query_params().get('ServiceType')

	def set_ServiceType(self, ServiceType):  # String
		self.add_query_param('ServiceType', ServiceType)
	def get_K8sServiceId(self): # String
		return self.get_query_params().get('K8sServiceId')

	def set_K8sServiceId(self, K8sServiceId):  # String
		self.add_query_param('K8sServiceId', K8sServiceId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_PortMappingss(self): # RepeatList
		return self.get_body_params().get('PortMappings')

	def set_PortMappingss(self, PortMappings):  # RepeatList
		for depth1 in range(len(PortMappings)):
			if PortMappings[depth1].get('Protocol') is not None:
				self.add_body_params('PortMappings.' + str(depth1 + 1) + '.Protocol', PortMappings[depth1].get('Protocol'))
			if PortMappings[depth1].get('Port') is not None:
				self.add_body_params('PortMappings.' + str(depth1 + 1) + '.Port', PortMappings[depth1].get('Port'))
			if PortMappings[depth1].get('Name') is not None:
				self.add_body_params('PortMappings.' + str(depth1 + 1) + '.Name', PortMappings[depth1].get('Name'))
			if PortMappings[depth1].get('NodePort') is not None:
				self.add_body_params('PortMappings.' + str(depth1 + 1) + '.NodePort', PortMappings[depth1].get('NodePort'))
			if PortMappings[depth1].get('TargetPort') is not None:
				self.add_body_params('PortMappings.' + str(depth1 + 1) + '.TargetPort', PortMappings[depth1].get('TargetPort'))
	def get_EnvId(self): # Long
		return self.get_query_params().get('EnvId')

	def set_EnvId(self, EnvId):  # Long
		self.add_query_param('EnvId', EnvId)
