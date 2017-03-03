# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
class RoaDubboApiRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Ft', '2015-02-02', 'RoaDubboApi')
		self.set_uri_pattern(self, '/RoaDubboApi')
		self.set_method(self, 'GET')

	def get_x-acs-success(self):
		return self.get_header().get('x-acs-success')

	def set_x-acs-success(self,x-acs-success):
		self.add_header('x-acs-success',x-acs-success)

	def get_x-acs-string-value(self):
		return self.get_header().get('x-acs-string-value')

	def set_x-acs-string-value(self,x-acs-string-value):
		self.add_header('x-acs-string-value',x-acs-string-value)