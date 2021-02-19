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
from aliyunsdkairec.endpoint import endpoint_data

class QueryRawDataRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2018-10-12', 'QueryRawData','airec')
		self.set_uri_pattern('/openapi/instances/[InstanceId]/tables/[Table]/raw-data')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ItemId(self):
		return self.get_query_params().get('ItemId')

	def set_ItemId(self,ItemId):
		self.add_query_param('ItemId',ItemId)

	def get_InstanceId(self):
		return self.get_path_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_path_param('InstanceId',InstanceId)

	def get_ItemType(self):
		return self.get_query_params().get('ItemType')

	def set_ItemType(self,ItemType):
		self.add_query_param('ItemType',ItemType)

	def get_UserType(self):
		return self.get_query_params().get('UserType')

	def set_UserType(self,UserType):
		self.add_query_param('UserType',UserType)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_Table(self):
		return self.get_path_params().get('Table')

	def set_Table(self,Table):
		self.add_path_param('Table',Table)