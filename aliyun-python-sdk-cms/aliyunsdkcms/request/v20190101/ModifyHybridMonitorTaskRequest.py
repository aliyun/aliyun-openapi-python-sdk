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

class ModifyHybridMonitorTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ModifyHybridMonitorTask','cms')
		self.set_method('POST')

	def get_TaskName(self): # String
		return self.get_query_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_query_param('TaskName', TaskName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_CollectInterval(self): # String
		return self.get_query_params().get('CollectInterval')

	def set_CollectInterval(self, CollectInterval):  # String
		self.add_query_param('CollectInterval', CollectInterval)
	def get_AttachLabelss(self): # RepeatList
		return self.get_query_params().get('AttachLabels')

	def set_AttachLabelss(self, AttachLabels):  # RepeatList
		for depth1 in range(len(AttachLabels)):
			if AttachLabels[depth1].get('Name') is not None:
				self.add_query_param('AttachLabels.' + str(depth1 + 1) + '.Name', AttachLabels[depth1].get('Name'))
			if AttachLabels[depth1].get('Value') is not None:
				self.add_query_param('AttachLabels.' + str(depth1 + 1) + '.Value', AttachLabels[depth1].get('Value'))
	def get_TaskId(self): # String
		return self.get_query_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_query_param('TaskId', TaskId)
	def get_SLSProcessConfig(self): # Struct
		return self.get_query_params().get('SLSProcessConfig')

	def set_SLSProcessConfig(self, SLSProcessConfig):  # Struct
		if SLSProcessConfig.get('Filter') is not None:
			if SLSProcessConfig.get('Filter').get('Filters') is not None:
				for index1, value1 in enumerate(SLSProcessConfig.get('Filter').get('Filters')):
					if value1.get('SLSKeyName') is not None:
						self.add_query_param('SLSProcessConfig.Filter.Filters.' + str(index1 + 1) + '.SLSKeyName', value1.get('SLSKeyName'))
					if value1.get('Value') is not None:
						self.add_query_param('SLSProcessConfig.Filter.Filters.' + str(index1 + 1) + '.Value', value1.get('Value'))
					if value1.get('Operator') is not None:
						self.add_query_param('SLSProcessConfig.Filter.Filters.' + str(index1 + 1) + '.Operator', value1.get('Operator'))
			if SLSProcessConfig.get('Filter').get('Relation') is not None:
				self.add_query_param('SLSProcessConfig.Filter.Relation', SLSProcessConfig.get('Filter').get('Relation'))
		if SLSProcessConfig.get('Express') is not None:
			for index1, value1 in enumerate(SLSProcessConfig.get('Express')):
				if value1.get('Alias') is not None:
					self.add_query_param('SLSProcessConfig.Express.' + str(index1 + 1) + '.Alias', value1.get('Alias'))
				if value1.get('Express') is not None:
					self.add_query_param('SLSProcessConfig.Express.' + str(index1 + 1) + '.Express', value1.get('Express'))
		if SLSProcessConfig.get('GroupBy') is not None:
			for index1, value1 in enumerate(SLSProcessConfig.get('GroupBy')):
				if value1.get('SLSKeyName') is not None:
					self.add_query_param('SLSProcessConfig.GroupBy.' + str(index1 + 1) + '.SLSKeyName', value1.get('SLSKeyName'))
				if value1.get('Alias') is not None:
					self.add_query_param('SLSProcessConfig.GroupBy.' + str(index1 + 1) + '.Alias', value1.get('Alias'))
		if SLSProcessConfig.get('Statistics') is not None:
			for index1, value1 in enumerate(SLSProcessConfig.get('Statistics')):
				if value1.get('SLSKeyName') is not None:
					self.add_query_param('SLSProcessConfig.Statistics.' + str(index1 + 1) + '.SLSKeyName', value1.get('SLSKeyName'))
				if value1.get('Function') is not None:
					self.add_query_param('SLSProcessConfig.Statistics.' + str(index1 + 1) + '.Function', value1.get('Function'))
				if value1.get('Alias') is not None:
					self.add_query_param('SLSProcessConfig.Statistics.' + str(index1 + 1) + '.Alias', value1.get('Alias'))
				if value1.get('Parameter2') is not None:
					self.add_query_param('SLSProcessConfig.Statistics.' + str(index1 + 1) + '.Parameter2', value1.get('Parameter2'))
				if value1.get('Parameter1') is not None:
					self.add_query_param('SLSProcessConfig.Statistics.' + str(index1 + 1) + '.Parameter1', value1.get('Parameter1'))
