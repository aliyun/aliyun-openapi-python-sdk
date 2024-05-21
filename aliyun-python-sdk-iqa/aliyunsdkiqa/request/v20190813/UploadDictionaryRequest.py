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

class UploadDictionaryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'iqa', '2019-08-13', 'UploadDictionary','iqa')

	def get_DictionaryFileUrl(self):
		return self.get_body_params().get('DictionaryFileUrl')

	def set_DictionaryFileUrl(self,DictionaryFileUrl):
		self.add_body_params('DictionaryFileUrl', DictionaryFileUrl)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_DictionaryData(self):
		return self.get_body_params().get('DictionaryData')

	def set_DictionaryData(self,DictionaryData):
		self.add_body_params('DictionaryData', DictionaryData)