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
from aliyunsdksas.endpoint import endpoint_data

class DescribeExposedInstanceListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeExposedInstanceList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ExposurePort(self): # String
		return self.get_query_params().get('ExposurePort')

	def set_ExposurePort(self, ExposurePort):  # String
		self.add_query_param('ExposurePort', ExposurePort)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_VulStatus(self): # Boolean
		return self.get_query_params().get('VulStatus')

	def set_VulStatus(self, VulStatus):  # Boolean
		self.add_query_param('VulStatus', VulStatus)
	def get_ExposureIp(self): # String
		return self.get_query_params().get('ExposureIp')

	def set_ExposureIp(self, ExposureIp):  # String
		self.add_query_param('ExposureIp', ExposureIp)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_ExposureComponent(self): # String
		return self.get_query_params().get('ExposureComponent')

	def set_ExposureComponent(self, ExposureComponent):  # String
		self.add_query_param('ExposureComponent', ExposureComponent)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_HealthStatus(self): # Boolean
		return self.get_query_params().get('HealthStatus')

	def set_HealthStatus(self, HealthStatus):  # Boolean
		self.add_query_param('HealthStatus', HealthStatus)
