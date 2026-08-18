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

class RevertPlaybookReleaseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sophonsoar', '2022-07-28', 'RevertPlaybookRelease')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_PlaybookUuid(self): # String
		return self.get_body_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_body_params('PlaybookUuid', PlaybookUuid)
	def get_PlayReleaseId(self): # Integer
		return self.get_body_params().get('PlayReleaseId')

	def set_PlayReleaseId(self, PlayReleaseId):  # Integer
		self.add_body_params('PlayReleaseId', PlayReleaseId)
	def get_IsPublish(self): # Boolean
		return self.get_body_params().get('IsPublish')

	def set_IsPublish(self, IsPublish):  # Boolean
		self.add_body_params('IsPublish', IsPublish)
