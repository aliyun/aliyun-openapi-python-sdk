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

from aliyunsdkcore.request import RoaRequest

class UploadFileByURLRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'grace', '2022-06-06', 'UploadFileByURL','grace')
		self.set_uri_pattern('/UploadFileByURL')
		self.set_method('POST')

	def get_type(self): # String
		return self.get_query_params().get('type')

	def set_type(self, type):  # String
		self.add_query_param('type', type)
	def get_url(self): # String
		return self.get_query_params().get('url')

	def set_url(self, url):  # String
		self.add_query_param('url', url)
	def get_displayName(self): # String
		return self.get_query_params().get('displayName')

	def set_displayName(self, displayName):  # String
		self.add_query_param('displayName', displayName)
