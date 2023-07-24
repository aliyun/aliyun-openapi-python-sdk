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
from aliyunsdkeipanycast.endpoint import endpoint_data

class AssociateAnycastEipAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Eipanycast', '2020-03-09', 'AssociateAnycastEipAddress','eipanycast')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_PopLocations(self): # Array
		return self.get_query_params().get('PopLocations')

	def set_PopLocations(self, PopLocations):  # Array
		for index1, value1 in enumerate(PopLocations):
			if value1.get('PopLocation') is not None:
				self.add_query_param('PopLocations.' + str(index1 + 1) + '.PopLocation', value1.get('PopLocation'))
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_AssociationMode(self): # String
		return self.get_query_params().get('AssociationMode')

	def set_AssociationMode(self, AssociationMode):  # String
		self.add_query_param('AssociationMode', AssociationMode)
	def get_BindInstanceType(self): # String
		return self.get_query_params().get('BindInstanceType')

	def set_BindInstanceType(self, BindInstanceType):  # String
		self.add_query_param('BindInstanceType', BindInstanceType)
	def get_BindInstanceRegionId(self): # String
		return self.get_query_params().get('BindInstanceRegionId')

	def set_BindInstanceRegionId(self, BindInstanceRegionId):  # String
		self.add_query_param('BindInstanceRegionId', BindInstanceRegionId)
	def get_PrivateIpAddress(self): # String
		return self.get_query_params().get('PrivateIpAddress')

	def set_PrivateIpAddress(self, PrivateIpAddress):  # String
		self.add_query_param('PrivateIpAddress', PrivateIpAddress)
	def get_AnycastId(self): # String
		return self.get_query_params().get('AnycastId')

	def set_AnycastId(self, AnycastId):  # String
		self.add_query_param('AnycastId', AnycastId)
	def get_BindInstanceId(self): # String
		return self.get_query_params().get('BindInstanceId')

	def set_BindInstanceId(self, BindInstanceId):  # String
		self.add_query_param('BindInstanceId', BindInstanceId)
