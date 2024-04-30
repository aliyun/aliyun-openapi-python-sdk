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
from aliyunsdkdcdn.endpoint import endpoint_data

class RefreshErObjectCachesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'RefreshErObjectCaches')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MergeDomainName(self): # String
		return self.get_query_params().get('MergeDomainName')

	def set_MergeDomainName(self, MergeDomainName):  # String
		self.add_query_param('MergeDomainName', MergeDomainName)
	def get_ObjectPath(self): # String
		return self.get_query_params().get('ObjectPath')

	def set_ObjectPath(self, ObjectPath):  # String
		self.add_query_param('ObjectPath', ObjectPath)
	def get_Force(self): # Boolean
		return self.get_query_params().get('Force')

	def set_Force(self, Force):  # Boolean
		self.add_query_param('Force', Force)
	def get_ObjectType(self): # String
		return self.get_query_params().get('ObjectType')

	def set_ObjectType(self, ObjectType):  # String
		self.add_query_param('ObjectType', ObjectType)
	def get_RoutineId(self): # String
		return self.get_query_params().get('RoutineId')

	def set_RoutineId(self, RoutineId):  # String
		self.add_query_param('RoutineId', RoutineId)
