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

class BatchCreateIntantSiteMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'BatchCreateIntantSiteMonitor','cms')
		self.set_method('POST')

	def get_TaskLists(self): # RepeatList
		return self.get_query_params().get('TaskList')

	def set_TaskLists(self, TaskList):  # RepeatList
		for depth1 in range(len(TaskList)):
			if TaskList[depth1].get('OptionsJson') is not None:
				self.add_query_param('TaskList.' + str(depth1 + 1) + '.OptionsJson', TaskList[depth1].get('OptionsJson'))
			if TaskList[depth1].get('Address') is not None:
				self.add_query_param('TaskList.' + str(depth1 + 1) + '.Address', TaskList[depth1].get('Address'))
			if TaskList[depth1].get('TaskType') is not None:
				self.add_query_param('TaskList.' + str(depth1 + 1) + '.TaskType', TaskList[depth1].get('TaskType'))
			if TaskList[depth1].get('TaskName') is not None:
				self.add_query_param('TaskList.' + str(depth1 + 1) + '.TaskName', TaskList[depth1].get('TaskName'))
			if TaskList[depth1].get('IspCities') is not None:
				self.add_query_param('TaskList.' + str(depth1 + 1) + '.IspCities', TaskList[depth1].get('IspCities'))
