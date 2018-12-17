# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeAlarmsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudesl', '2018-08-01', 'DescribeAlarms')

	def get_ErrorType(self):
		return self.get_query_params().get('ErrorType')

	def set_ErrorType(self,ErrorType):
		self.add_query_param('ErrorType',ErrorType)

	def get_ToAlarmTime(self):
		return self.get_query_params().get('ToAlarmTime')

	def set_ToAlarmTime(self,ToAlarmTime):
		self.add_query_param('ToAlarmTime',ToAlarmTime)

	def get_AlarmType(self):
		return self.get_query_params().get('AlarmType')

	def set_AlarmType(self,AlarmType):
		self.add_query_param('AlarmType',AlarmType)

	def get_FromAlarmTime(self):
		return self.get_query_params().get('FromAlarmTime')

	def set_FromAlarmTime(self,FromAlarmTime):
		self.add_query_param('FromAlarmTime',FromAlarmTime)

	def get_AlarmId(self):
		return self.get_query_params().get('AlarmId')

	def set_AlarmId(self,AlarmId):
		self.add_query_param('AlarmId',AlarmId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_StoreId(self):
		return self.get_query_params().get('StoreId')

	def set_StoreId(self,StoreId):
		self.add_query_param('StoreId',StoreId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_AlarmStatus(self):
		return self.get_query_params().get('AlarmStatus')

	def set_AlarmStatus(self,AlarmStatus):
		self.add_query_param('AlarmStatus',AlarmStatus)