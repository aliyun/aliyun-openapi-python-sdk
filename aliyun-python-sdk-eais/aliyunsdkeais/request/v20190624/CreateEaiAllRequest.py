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
from aliyunsdkeais.endpoint import endpoint_data

class CreateEaiAllRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eais', '2019-06-24', 'CreateEaiAll','eais')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientImageId(self): # String
		return self.get_query_params().get('ClientImageId')

	def set_ClientImageId(self, ClientImageId):  # String
		self.add_query_param('ClientImageId', ClientImageId)
	def get_ClientSystemDiskCategory(self): # String
		return self.get_query_params().get('ClientSystemDiskCategory')

	def set_ClientSystemDiskCategory(self, ClientSystemDiskCategory):  # String
		self.add_query_param('ClientSystemDiskCategory', ClientSystemDiskCategory)
	def get_ClientInternetMaxBandwidthOut(self): # Integer
		return self.get_query_params().get('ClientInternetMaxBandwidthOut')

	def set_ClientInternetMaxBandwidthOut(self, ClientInternetMaxBandwidthOut):  # Integer
		self.add_query_param('ClientInternetMaxBandwidthOut', ClientInternetMaxBandwidthOut)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ClientInstanceName(self): # String
		return self.get_query_params().get('ClientInstanceName')

	def set_ClientInstanceName(self, ClientInstanceName):  # String
		self.add_query_param('ClientInstanceName', ClientInstanceName)
	def get_ClientInternetMaxBandwidthIn(self): # Integer
		return self.get_query_params().get('ClientInternetMaxBandwidthIn')

	def set_ClientInternetMaxBandwidthIn(self, ClientInternetMaxBandwidthIn):  # Integer
		self.add_query_param('ClientInternetMaxBandwidthIn', ClientInternetMaxBandwidthIn)
	def get_ClientSystemDiskSize(self): # Integer
		return self.get_query_params().get('ClientSystemDiskSize')

	def set_ClientSystemDiskSize(self, ClientSystemDiskSize):  # Integer
		self.add_query_param('ClientSystemDiskSize', ClientSystemDiskSize)
	def get_ClientVSwitchId(self): # String
		return self.get_query_params().get('ClientVSwitchId')

	def set_ClientVSwitchId(self, ClientVSwitchId):  # String
		self.add_query_param('ClientVSwitchId', ClientVSwitchId)
	def get_ClientPassword(self): # String
		return self.get_query_params().get('ClientPassword')

	def set_ClientPassword(self, ClientPassword):  # String
		self.add_query_param('ClientPassword', ClientPassword)
	def get_ClientInstanceType(self): # String
		return self.get_query_params().get('ClientInstanceType')

	def set_ClientInstanceType(self, ClientInstanceType):  # String
		self.add_query_param('ClientInstanceType', ClientInstanceType)
	def get_ClientSecurityGroupId(self): # String
		return self.get_query_params().get('ClientSecurityGroupId')

	def set_ClientSecurityGroupId(self, ClientSecurityGroupId):  # String
		self.add_query_param('ClientSecurityGroupId', ClientSecurityGroupId)
	def get_EaiInstanceType(self): # String
		return self.get_query_params().get('EaiInstanceType')

	def set_EaiInstanceType(self, EaiInstanceType):  # String
		self.add_query_param('EaiInstanceType', EaiInstanceType)
	def get_ClientZoneId(self): # String
		return self.get_query_params().get('ClientZoneId')

	def set_ClientZoneId(self, ClientZoneId):  # String
		self.add_query_param('ClientZoneId', ClientZoneId)
	def get_InstanceName(self): # String
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_query_param('InstanceName', InstanceName)
