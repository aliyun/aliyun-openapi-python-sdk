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

class ReConfigApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'ReConfigApplication','bpstudio')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Variables(self): # String
		return self.get_body_params().get('Variables')

	def set_Variables(self, Variables):  # String
		self.add_body_params('Variables', Variables)
	def get_AppId(self): # String
		return self.get_body_params().get('AppId')

	def set_AppId(self, AppId):  # String
		self.add_body_params('AppId', AppId)
