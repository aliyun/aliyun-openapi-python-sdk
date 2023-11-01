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

class GetHistogramsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'GetHistograms','cloud-siem')
		self.set_method('POST')

	def get_From(self): # Integer
		return self.get_body_params().get('From')

	def set_From(self, _From):  # Integer
		self.add_body_params('From', _From)
	def get_Query(self): # String
		return self.get_body_params().get('Query')

	def set_Query(self, Query):  # String
		self.add_body_params('Query', Query)
	def get_To(self): # Integer
		return self.get_body_params().get('To')

	def set_To(self, To):  # Integer
		self.add_body_params('To', To)
