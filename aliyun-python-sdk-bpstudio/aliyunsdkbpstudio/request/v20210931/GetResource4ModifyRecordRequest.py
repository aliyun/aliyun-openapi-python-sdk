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

class GetResource4ModifyRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BPStudio', '2021-09-31', 'GetResource4ModifyRecord','bpstudio')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_NextToken(self): # Long
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # Long
		self.add_body_params('NextToken', NextToken)
	def get_MaxResults(self): # Long
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Long
		self.add_body_params('MaxResults', MaxResults)
	def get_ApplicationId(self): # String
		return self.get_body_params().get('ApplicationId')

	def set_ApplicationId(self, ApplicationId):  # String
		self.add_body_params('ApplicationId', ApplicationId)
