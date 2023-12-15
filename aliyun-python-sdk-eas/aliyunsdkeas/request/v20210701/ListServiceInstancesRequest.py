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
from aliyunsdkeas.endpoint import endpoint_data

class ListServiceInstancesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'eas', '2021-07-01', 'ListServiceInstances','eas')
		self.set_uri_pattern('/api/v2/services/[ClusterId]/[ServiceName]/instances')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceStatus(self): # String
		return self.get_query_params().get('InstanceStatus')

	def set_InstanceStatus(self, InstanceStatus):  # String
		self.add_query_param('InstanceStatus', InstanceStatus)
	def get_Role(self): # String
		return self.get_query_params().get('Role')

	def set_Role(self, Role):  # String
		self.add_query_param('Role', Role)
	def get_HostIP(self): # String
		return self.get_query_params().get('HostIP')

	def set_HostIP(self, HostIP):  # String
		self.add_query_param('HostIP', HostIP)
	def get_ClusterId(self): # String
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_path_param('ClusterId', ClusterId)
	def get_Sort(self): # String
		return self.get_query_params().get('Sort')

	def set_Sort(self, Sort):  # String
		self.add_query_param('Sort', Sort)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_Filter(self): # String
		return self.get_query_params().get('Filter')

	def set_Filter(self, Filter):  # String
		self.add_query_param('Filter', Filter)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_ServiceName(self): # String
		return self.get_path_params().get('ServiceName')

	def set_ServiceName(self, ServiceName):  # String
		self.add_path_param('ServiceName', ServiceName)
	def get_IsSpot(self): # Boolean
		return self.get_query_params().get('IsSpot')

	def set_IsSpot(self, IsSpot):  # Boolean
		self.add_query_param('IsSpot', IsSpot)
	def get_InstanceIP(self): # String
		return self.get_query_params().get('InstanceIP')

	def set_InstanceIP(self, InstanceIP):  # String
		self.add_query_param('InstanceIP', InstanceIP)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
