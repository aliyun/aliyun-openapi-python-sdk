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

class FindInstanceInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Buss', '2022-08-22', 'FindInstanceInfo')
		self.set_method('GET')

	def get_bussinessCode(self): # String
		return self.get_query_params().get('bussinessCode')

	def set_bussinessCode(self, bussinessCode):  # String
		self.add_query_param('bussinessCode', bussinessCode)
	def get_ip(self): # String
		return self.get_query_params().get('ip')

	def set_ip(self, ip):  # String
		self.add_query_param('ip', ip)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_extras(self): # Map
		return self.get_query_params().get('extras')

	def set_extras(self, extras):  # Map
		self.add_query_param("extras", json.dumps(extras))
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_userId(self): # String
		return self.get_query_params().get('userId')

	def set_userId(self, userId):  # String
		self.add_query_param('userId', userId)
	def get_url(self): # String
		return self.get_query_params().get('url')

	def set_url(self, url):  # String
		self.add_query_param('url', url)
	def get_needDNS(self): # Boolean
		return self.get_query_params().get('needDNS')

	def set_needDNS(self, needDNS):  # Boolean
		self.add_query_param('needDNS', needDNS)
	def get_domain(self): # String
		return self.get_query_params().get('domain')

	def set_domain(self, domain):  # String
		self.add_query_param('domain', domain)
