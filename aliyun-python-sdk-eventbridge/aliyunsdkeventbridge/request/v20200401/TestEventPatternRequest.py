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

class TestEventPatternRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'TestEventPattern')
		self.set_method('POST')

	def get_EventPattern(self): # String
		return self.get_body_params().get('EventPattern')

	def set_EventPattern(self, EventPattern):  # String
		self.add_body_params('EventPattern', EventPattern)
	def get_Event(self): # String
		return self.get_body_params().get('Event')

	def set_Event(self, Event):  # String
		self.add_body_params('Event', Event)
