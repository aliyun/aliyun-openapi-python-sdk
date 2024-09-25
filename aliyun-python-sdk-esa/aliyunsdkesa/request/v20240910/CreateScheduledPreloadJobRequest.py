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

class CreateScheduledPreloadJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'CreateScheduledPreloadJob')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_InsertWay(self): # String
		return self.get_body_params().get('InsertWay')

	def set_InsertWay(self, InsertWay):  # String
		self.add_body_params('InsertWay', InsertWay)
	def get_OssUrl(self): # String
		return self.get_body_params().get('OssUrl')

	def set_OssUrl(self, OssUrl):  # String
		self.add_body_params('OssUrl', OssUrl)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_SiteId(self): # Long
		return self.get_body_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_body_params('SiteId', SiteId)
	def get_UrlList(self): # String
		return self.get_body_params().get('UrlList')

	def set_UrlList(self, UrlList):  # String
		self.add_body_params('UrlList', UrlList)
