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

class UpdateGroupTagByIdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Oam', '2017-01-01', 'UpdateGroupTagById')
		self.set_method('POST')

	def get_TagIds(self):
		return self.get_query_params().get('TagIds')

	def set_TagIds(self, TagIds):
		for depth1 in range(len(TagIds)):
			if TagIds[depth1].get('NewId') is not None:
				self.add_query_param('TagId.' + str(depth1 + 1) + '.NewId', TagIds[depth1].get('NewId'))
			if TagIds[depth1].get('OldId') is not None:
				self.add_query_param('TagId.' + str(depth1 + 1) + '.OldId', TagIds[depth1].get('OldId'))

	def get_GroupTagId(self):
		return self.get_query_params().get('GroupTagId')

	def set_GroupTagId(self,GroupTagId):
		self.add_query_param('GroupTagId',GroupTagId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)