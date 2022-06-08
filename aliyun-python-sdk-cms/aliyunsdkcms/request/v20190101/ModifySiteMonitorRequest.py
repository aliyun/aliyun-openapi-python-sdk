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

class ModifySiteMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifySiteMonitor','cms')
		self.set_method('POST')

	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_AlertIds(self): # String
		return self.get_query_params().get('AlertIds')

	def set_AlertIds(self, AlertIds):  # String
		self.add_query_param('AlertIds', AlertIds)
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_IspCities(self): # String
		return self.get_query_params().get('IspCities')

	def set_IspCities(self, IspCities):  # String
		self.add_query_param('IspCities', IspCities)
	def get_OptionsJson(self): # String
		return self.get_query_params().get('OptionsJson')

	def set_OptionsJson(self, OptionsJson):  # String
		self.add_query_param('OptionsJson', OptionsJson)
	def get_IntervalUnit(self): # String
		return self.get_query_params().get('IntervalUnit')

	def set_IntervalUnit(self, IntervalUnit):  # String
		self.add_query_param('IntervalUnit', IntervalUnit)
	def get_Interval(self): # String
		return self.get_query_params().get('Interval')

	def set_Interval(self, Interval):  # String
		self.add_query_param('Interval', Interval)
