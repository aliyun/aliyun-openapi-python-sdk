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
from aliyunsdksgw.endpoint import endpoint_data

class CreateGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'CreateGateway','hcs_sgw')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_GatewayClass(self): # String
		return self.get_query_params().get('GatewayClass')

	def set_GatewayClass(self, GatewayClass):  # String
		self.add_query_param('GatewayClass', GatewayClass)
	def get_PostPaid(self): # Boolean
		return self.get_query_params().get('PostPaid')

	def set_PostPaid(self, PostPaid):  # Boolean
		self.add_query_param('PostPaid', PostPaid)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_ReleaseAfterExpiration(self): # Boolean
		return self.get_query_params().get('ReleaseAfterExpiration')

	def set_ReleaseAfterExpiration(self, ReleaseAfterExpiration):  # Boolean
		self.add_query_param('ReleaseAfterExpiration', ReleaseAfterExpiration)
	def get_UntrustedEnvInstanceType(self): # String
		return self.get_query_params().get('UntrustedEnvInstanceType')

	def set_UntrustedEnvInstanceType(self, UntrustedEnvInstanceType):  # String
		self.add_query_param('UntrustedEnvInstanceType', UntrustedEnvInstanceType)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_StorageBundleId(self): # String
		return self.get_query_params().get('StorageBundleId')

	def set_StorageBundleId(self, StorageBundleId):  # String
		self.add_query_param('StorageBundleId', StorageBundleId)
	def get_ResourceRegionId(self): # String
		return self.get_query_params().get('ResourceRegionId')

	def set_ResourceRegionId(self, ResourceRegionId):  # String
		self.add_query_param('ResourceRegionId', ResourceRegionId)
	def get_UntrustedEnvId(self): # String
		return self.get_query_params().get('UntrustedEnvId')

	def set_UntrustedEnvId(self, UntrustedEnvId):  # String
		self.add_query_param('UntrustedEnvId', UntrustedEnvId)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_SecondaryVSwitchId(self): # String
		return self.get_query_params().get('SecondaryVSwitchId')

	def set_SecondaryVSwitchId(self, SecondaryVSwitchId):  # String
		self.add_query_param('SecondaryVSwitchId', SecondaryVSwitchId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Location(self): # String
		return self.get_query_params().get('Location')

	def set_Location(self, Location):  # String
		self.add_query_param('Location', Location)
	def get_Category(self): # String
		return self.get_query_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_query_param('Category', Category)
	def get_PublicNetworkBandwidth(self): # Integer
		return self.get_query_params().get('PublicNetworkBandwidth')

	def set_PublicNetworkBandwidth(self, PublicNetworkBandwidth):  # Integer
		self.add_query_param('PublicNetworkBandwidth', PublicNetworkBandwidth)
