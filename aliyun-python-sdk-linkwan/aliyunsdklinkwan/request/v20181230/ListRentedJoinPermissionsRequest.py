# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ListRentedJoinPermissionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'ListRentedJoinPermissions','linkwan')
		self.set_protocol_type('https');

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_Enabled(self):
		return self.get_body_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_body_params('Enabled', Enabled)

	def get_FuzzyJoinEui(self):
		return self.get_body_params().get('FuzzyJoinEui')

	def set_FuzzyJoinEui(self,FuzzyJoinEui):
		self.add_body_params('FuzzyJoinEui', FuzzyJoinEui)

	def get_Limit(self):
		return self.get_body_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_body_params('Limit', Limit)

	def get_FuzzyJoinPermissionName(self):
		return self.get_body_params().get('FuzzyJoinPermissionName')

	def set_FuzzyJoinPermissionName(self,FuzzyJoinPermissionName):
		self.add_body_params('FuzzyJoinPermissionName', FuzzyJoinPermissionName)

	def get_Offset(self):
		return self.get_body_params().get('Offset')

	def set_Offset(self,Offset):
		self.add_body_params('Offset', Offset)

	def get_BoundNodeGroup(self):
		return self.get_body_params().get('BoundNodeGroup')

	def set_BoundNodeGroup(self,BoundNodeGroup):
		self.add_body_params('BoundNodeGroup', BoundNodeGroup)

	def get_FuzzyOwnerAliyunId(self):
		return self.get_body_params().get('FuzzyOwnerAliyunId')

	def set_FuzzyOwnerAliyunId(self,FuzzyOwnerAliyunId):
		self.add_body_params('FuzzyOwnerAliyunId', FuzzyOwnerAliyunId)

	def get_SortingField(self):
		return self.get_body_params().get('SortingField')

	def set_SortingField(self,SortingField):
		self.add_body_params('SortingField', SortingField)

	def get_Ascending(self):
		return self.get_body_params().get('Ascending')

	def set_Ascending(self,Ascending):
		self.add_body_params('Ascending', Ascending)