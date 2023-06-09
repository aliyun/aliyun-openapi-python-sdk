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

class ListEventStreamingsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListEventStreamings')
		self.set_method('POST')

	def get_SourceArn(self): # String
		return self.get_body_params().get('SourceArn')

	def set_SourceArn(self, SourceArn):  # String
		self.add_body_params('SourceArn', SourceArn)
	def get_SinkArn(self): # String
		return self.get_body_params().get('SinkArn')

	def set_SinkArn(self, SinkArn):  # String
		self.add_body_params('SinkArn', SinkArn)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_Limit(self): # Integer
		return self.get_body_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_body_params('Limit', Limit)
	def get_NamePrefix(self): # String
		return self.get_body_params().get('NamePrefix')

	def set_NamePrefix(self, NamePrefix):  # String
		self.add_body_params('NamePrefix', NamePrefix)
