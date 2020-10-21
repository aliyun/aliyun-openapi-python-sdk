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
from aliyunsdkhbr.endpoint import endpoint_data

class RegisterApplianceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'RegisterAppliance','hbr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IpAddress(self):
		return self.get_query_params().get('IpAddress')

	def set_IpAddress(self,IpAddress):
		self.add_query_param('IpAddress',IpAddress)

	def get_ApplianceVersion(self):
		return self.get_query_params().get('ApplianceVersion')

	def set_ApplianceVersion(self,ApplianceVersion):
		self.add_query_param('ApplianceVersion',ApplianceVersion)

	def get_HardwareModel(self):
		return self.get_query_params().get('HardwareModel')

	def set_HardwareModel(self,HardwareModel):
		self.add_query_param('HardwareModel',HardwareModel)

	def get_ApplianceType(self):
		return self.get_query_params().get('ApplianceType')

	def set_ApplianceType(self,ApplianceType):
		self.add_query_param('ApplianceType',ApplianceType)

	def get_Uuid(self):
		return self.get_query_params().get('Uuid')

	def set_Uuid(self,Uuid):
		self.add_query_param('Uuid',Uuid)

	def get_Hostname(self):
		return self.get_query_params().get('Hostname')

	def set_Hostname(self,Hostname):
		self.add_query_param('Hostname',Hostname)

	def get_ApplianceName(self):
		return self.get_query_params().get('ApplianceName')

	def set_ApplianceName(self,ApplianceName):
		self.add_query_param('ApplianceName',ApplianceName)

	def get_MacAddress(self):
		return self.get_query_params().get('MacAddress')

	def set_MacAddress(self,MacAddress):
		self.add_query_param('MacAddress',MacAddress)