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

class CreateJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateJob')
		self.set_method('POST')

	def get_GroupFileCountLimiter(self):
		return self.get_query_params().get('GroupFileCountLimiter')

	def set_GroupFileCountLimiter(self,GroupFileCountLimiter):
		self.add_query_param('GroupFileCountLimiter',GroupFileCountLimiter)

	def get_StartDate(self):
		return self.get_query_params().get('StartDate')

	def set_StartDate(self,StartDate):
		self.add_query_param('StartDate',StartDate)

	def get_GroupFileSizeLimiter(self):
		return self.get_query_params().get('GroupFileSizeLimiter')

	def set_GroupFileSizeLimiter(self,GroupFileSizeLimiter):
		self.add_query_param('GroupFileSizeLimiter',GroupFileSizeLimiter)

	def get_RunImmediate(self):
		return self.get_query_params().get('RunImmediate')

	def set_RunImmediate(self,RunImmediate):
		self.add_query_param('RunImmediate',RunImmediate)

	def get_SrcAddress(self):
		return self.get_query_params().get('SrcAddress')

	def set_SrcAddress(self,SrcAddress):
		self.add_query_param('SrcAddress',SrcAddress)

	def get_LastScanTime(self):
		return self.get_query_params().get('LastScanTime')

	def set_LastScanTime(self,LastScanTime):
		self.add_query_param('LastScanTime',LastScanTime)

	def get_IntervalInSecond(self):
		return self.get_query_params().get('IntervalInSecond')

	def set_IntervalInSecond(self,IntervalInSecond):
		self.add_query_param('IntervalInSecond',IntervalInSecond)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_RepeatCount(self):
		return self.get_query_params().get('RepeatCount')

	def set_RepeatCount(self,RepeatCount):
		self.add_query_param('RepeatCount',RepeatCount)

	def get_SpeedTimeTableLimiter(self):
		return self.get_query_params().get('SpeedTimeTableLimiter')

	def set_SpeedTimeTableLimiter(self,SpeedTimeTableLimiter):
		self.add_query_param('SpeedTimeTableLimiter',SpeedTimeTableLimiter)

	def get_NoNewRunIfAnyRunning(self):
		return self.get_query_params().get('NoNewRunIfAnyRunning')

	def set_NoNewRunIfAnyRunning(self,NoNewRunIfAnyRunning):
		self.add_query_param('NoNewRunIfAnyRunning',NoNewRunIfAnyRunning)

	def get_DestAddress(self):
		return self.get_query_params().get('DestAddress')

	def set_DestAddress(self,DestAddress):
		self.add_query_param('DestAddress',DestAddress)