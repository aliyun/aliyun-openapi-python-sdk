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

class ModifyServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'ModifyService','retailcloud')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_PortMappingss(self):
		return self.get_body_params().get('PortMappingss')

	def set_PortMappingss(self,PortMappingss):
		for i in range(len(PortMappingss)):	
			if PortMappingss[i].get('Protocol') is not None:
				self.add_body_params('PortMappings.' + str(i + 1) + '.Protocol' , PortMappingss[i].get('Protocol'))
			if PortMappingss[i].get('Port') is not None:
				self.add_body_params('PortMappings.' + str(i + 1) + '.Port' , PortMappingss[i].get('Port'))
			if PortMappingss[i].get('Name') is not None:
				self.add_body_params('PortMappings.' + str(i + 1) + '.Name' , PortMappingss[i].get('Name'))
			if PortMappingss[i].get('NodePort') is not None:
				self.add_body_params('PortMappings.' + str(i + 1) + '.NodePort' , PortMappingss[i].get('NodePort'))
			if PortMappingss[i].get('TargetPort') is not None:
				self.add_body_params('PortMappings.' + str(i + 1) + '.TargetPort' , PortMappingss[i].get('TargetPort'))


	def get_ServiceId(self):
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self,ServiceId):
		self.add_query_param('ServiceId',ServiceId)