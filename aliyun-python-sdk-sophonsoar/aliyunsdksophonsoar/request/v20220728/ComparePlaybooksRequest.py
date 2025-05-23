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

class ComparePlaybooksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'ComparePlaybooks')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_OldPlaybookReleaseId(self): # Integer
		return self.get_query_params().get('OldPlaybookReleaseId')

	def set_OldPlaybookReleaseId(self, OldPlaybookReleaseId):  # Integer
		self.add_query_param('OldPlaybookReleaseId', OldPlaybookReleaseId)
	def get_NewPlaybookReleaseId(self): # Integer
		return self.get_query_params().get('NewPlaybookReleaseId')

	def set_NewPlaybookReleaseId(self, NewPlaybookReleaseId):  # Integer
		self.add_query_param('NewPlaybookReleaseId', NewPlaybookReleaseId)
	def get_PlaybookUuid(self): # String
		return self.get_query_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_query_param('PlaybookUuid', PlaybookUuid)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
