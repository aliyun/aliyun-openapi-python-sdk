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
from aliyunsdkidrsservice.endpoint import endpoint_data

class CreateTaskGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'CreateTaskGroup','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ExpireAt(self):
		return self.get_query_params().get('ExpireAt')

	def set_ExpireAt(self,ExpireAt):
		self.add_query_param('ExpireAt',ExpireAt)

	def get_Days(self):
		return self.get_query_params().get('Days')

	def set_Days(self, Days):
		for depth1 in range(len(Days)):
			if Days[depth1] is not None:
				self.add_query_param('Day.' + str(depth1 + 1) , Days[depth1])

	def get_RunnableTimeTo(self):
		return self.get_query_params().get('RunnableTimeTo')

	def set_RunnableTimeTo(self,RunnableTimeTo):
		self.add_query_param('RunnableTimeTo',RunnableTimeTo)

	def get_TriggerPeriod(self):
		return self.get_query_params().get('TriggerPeriod')

	def set_TriggerPeriod(self,TriggerPeriod):
		self.add_query_param('TriggerPeriod',TriggerPeriod)

	def get_GroupName(self):
		return self.get_query_params().get('GroupName')

	def set_GroupName(self,GroupName):
		self.add_query_param('GroupName',GroupName)

	def get_VideoUrls(self):
		return self.get_query_params().get('VideoUrls')

	def set_VideoUrls(self, VideoUrls):
		for depth1 in range(len(VideoUrls)):
			if VideoUrls[depth1] is not None:
				self.add_query_param('VideoUrl.' + str(depth1 + 1) , VideoUrls[depth1])

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_RunnableTimeFrom(self):
		return self.get_query_params().get('RunnableTimeFrom')

	def set_RunnableTimeFrom(self,RunnableTimeFrom):
		self.add_query_param('RunnableTimeFrom',RunnableTimeFrom)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)