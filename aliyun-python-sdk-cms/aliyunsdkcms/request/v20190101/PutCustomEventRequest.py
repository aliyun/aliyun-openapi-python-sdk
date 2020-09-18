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

class PutCustomEventRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutCustomEvent','cms')
		self.set_method('POST')

	def get_EventInfos(self):
		return self.get_query_params().get('EventInfo')

	def set_EventInfos(self, EventInfos):
		for depth1 in range(len(EventInfos)):
			if EventInfos[depth1].get('GroupId') is not None:
				self.add_query_param('EventInfo.' + str(depth1 + 1) + '.GroupId', EventInfos[depth1].get('GroupId'))
			if EventInfos[depth1].get('Time') is not None:
				self.add_query_param('EventInfo.' + str(depth1 + 1) + '.Time', EventInfos[depth1].get('Time'))
			if EventInfos[depth1].get('EventName') is not None:
				self.add_query_param('EventInfo.' + str(depth1 + 1) + '.EventName', EventInfos[depth1].get('EventName'))
			if EventInfos[depth1].get('Content') is not None:
				self.add_query_param('EventInfo.' + str(depth1 + 1) + '.Content', EventInfos[depth1].get('Content'))