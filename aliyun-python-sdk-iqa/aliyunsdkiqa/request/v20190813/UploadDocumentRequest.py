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

class UploadDocumentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'iqa', '2019-08-13', 'UploadDocument','iqa')

	def get_DocumentData(self):
		return self.get_body_params().get('DocumentData')

	def set_DocumentData(self,DocumentData):
		self.add_body_params('DocumentData', DocumentData)

	def get_DocumentFileUrl(self):
		return self.get_body_params().get('DocumentFileUrl')

	def set_DocumentFileUrl(self,DocumentFileUrl):
		self.add_body_params('DocumentFileUrl', DocumentFileUrl)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)