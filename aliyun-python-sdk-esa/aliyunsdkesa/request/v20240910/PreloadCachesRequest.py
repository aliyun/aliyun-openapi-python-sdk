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

class PreloadCachesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'PreloadCaches')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Headers(self): # Map
		return self.get_query_params().get('Headers')

	def set_Headers(self, Headers):  # Map
		self.add_query_param("Headers", json.dumps(Headers))
	def get_SiteId(self): # Long
		return self.get_query_params().get('SiteId')

	def set_SiteId(self, SiteId):  # Long
		self.add_query_param('SiteId', SiteId)
	def get_Content(self): # Array
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # Array
		self.add_query_param("Content", json.dumps(Content))
