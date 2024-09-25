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

class UploadFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'UploadFile')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_UploadTaskName(self): # String
		return self.get_query_params().get('UploadTaskName')

	def set_UploadTaskName(self, UploadTaskName):  # String
		self.add_query_param('UploadTaskName', UploadTaskName)
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Url(self): # String
		return self.get_query_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_query_param('Url', Url)
