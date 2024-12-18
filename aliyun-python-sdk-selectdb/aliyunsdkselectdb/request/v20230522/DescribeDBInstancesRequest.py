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
import json

class DescribeDBInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'selectdb', '2023-05-22', 'DescribeDBInstances')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_PageNumber(self): # Long
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_query_param('PageNumber', PageNumber)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_PageSize(self): # Long
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_query_param('PageSize', PageSize)
	def get_DBInstanceStatus(self): # String
		return self.get_query_params().get('DBInstanceStatus')

	def set_DBInstanceStatus(self, DBInstanceStatus):  # String
		self.add_query_param('DBInstanceStatus', DBInstanceStatus)
	def get_DBInstanceDescription(self): # String
		return self.get_query_params().get('DBInstanceDescription')

	def set_DBInstanceDescription(self, DBInstanceDescription):  # String
		self.add_query_param('DBInstanceDescription', DBInstanceDescription)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		self.add_query_param("Tag", json.dumps(Tag))
	def get_DBInstanceIds(self): # String
		return self.get_query_params().get('DBInstanceIds')

	def set_DBInstanceIds(self, DBInstanceIds):  # String
		self.add_query_param('DBInstanceIds', DBInstanceIds)
