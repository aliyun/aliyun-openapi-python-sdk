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
from aliyunsdkdms_enterprise.endpoint import endpoint_data
import json

class DeleteLhMembersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'DeleteLhMembers','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_ObjectType(self): # Integer
		return self.get_query_params().get('ObjectType')

	def set_ObjectType(self, ObjectType):  # Integer
		self.add_query_param('ObjectType', ObjectType)
	def get_ObjectId(self): # Long
		return self.get_query_params().get('ObjectId')

	def set_ObjectId(self, ObjectId):  # Long
		self.add_query_param('ObjectId', ObjectId)
	def get_MemberIds(self): # Array
		return self.get_query_params().get('MemberIds')

	def set_MemberIds(self, MemberIds):  # Array
		self.add_query_param("MemberIds", json.dumps(MemberIds))
