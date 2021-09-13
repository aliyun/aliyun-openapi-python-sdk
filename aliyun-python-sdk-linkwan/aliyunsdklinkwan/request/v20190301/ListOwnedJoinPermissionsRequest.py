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
from aliyunsdklinkwan.endpoint import endpoint_data

class ListOwnedJoinPermissionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2019-03-01', 'ListOwnedJoinPermissions','linkwan')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_FuzzyJoinEui(self):
		return self.get_query_params().get('FuzzyJoinEui')

	def set_FuzzyJoinEui(self,FuzzyJoinEui):
		self.add_query_param('FuzzyJoinEui',FuzzyJoinEui)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_FuzzyJoinPermissionName(self):
		return self.get_query_params().get('FuzzyJoinPermissionName')

	def set_FuzzyJoinPermissionName(self,FuzzyJoinPermissionName):
		self.add_query_param('FuzzyJoinPermissionName',FuzzyJoinPermissionName)

	def get_Offset(self):
		return self.get_query_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_query_param('Offset',Offset)

	def get_FuzzyRenterAliyunId(self):
		return self.get_query_params().get('FuzzyRenterAliyunId')

	def set_FuzzyRenterAliyunId(self,FuzzyRenterAliyunId):
		self.add_query_param('FuzzyRenterAliyunId',FuzzyRenterAliyunId)

	def get_Ascending(self):
		return self.get_query_params().get('Ascending')

	def set_Ascending(self,Ascending):
		self.add_query_param('Ascending',Ascending)

	def get_SortingField(self):
		return self.get_query_params().get('SortingField')

	def set_SortingField(self,SortingField):
		self.add_query_param('SortingField',SortingField)