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
from aliyunsdkpolardb.endpoint import endpoint_data

class EvaluateRegionResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'EvaluateRegionResource','polardb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_DBInstanceConnType(self): # String
		return self.get_query_params().get('DBInstanceConnType')

	def set_DBInstanceConnType(self, DBInstanceConnType):  # String
		self.add_query_param('DBInstanceConnType', DBInstanceConnType)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_DBNodeClass(self): # String
		return self.get_query_params().get('DBNodeClass')

	def set_DBNodeClass(self, DBNodeClass):  # String
		self.add_query_param('DBNodeClass', DBNodeClass)
	def get_DispenseMode(self): # String
		return self.get_query_params().get('DispenseMode')

	def set_DispenseMode(self, DispenseMode):  # String
		self.add_query_param('DispenseMode', DispenseMode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_NeedMaxScaleLink(self): # String
		return self.get_query_params().get('NeedMaxScaleLink')

	def set_NeedMaxScaleLink(self, NeedMaxScaleLink):  # String
		self.add_query_param('NeedMaxScaleLink', NeedMaxScaleLink)
	def get_DBType(self): # String
		return self.get_query_params().get('DBType')

	def set_DBType(self, DBType):  # String
		self.add_query_param('DBType', DBType)
	def get_DBVersion(self): # String
		return self.get_query_params().get('DBVersion')

	def set_DBVersion(self, DBVersion):  # String
		self.add_query_param('DBVersion', DBVersion)
	def get_SubDomain(self): # String
		return self.get_query_params().get('SubDomain')

	def set_SubDomain(self, SubDomain):  # String
		self.add_query_param('SubDomain', SubDomain)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
