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
class IndexVideoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'IndexVideo','imm')

	def get_GrabType(self):
		return self.get_query_params().get('GrabType')

	def set_GrabType(self,GrabType):
		self.add_query_param('GrabType',GrabType)

	def get_RemarksB(self):
		return self.get_query_params().get('RemarksB')

	def set_RemarksB(self,RemarksB):
		self.add_query_param('RemarksB',RemarksB)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_RemarksA(self):
		return self.get_query_params().get('RemarksA')

	def set_RemarksA(self,RemarksA):
		self.add_query_param('RemarksA',RemarksA)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_VideoUri(self):
		return self.get_query_params().get('VideoUri')

	def set_VideoUri(self,VideoUri):
		self.add_query_param('VideoUri',VideoUri)

	def get_SaveType(self):
		return self.get_query_params().get('SaveType')

	def set_SaveType(self,SaveType):
		self.add_query_param('SaveType',SaveType)

	def get_SetId(self):
		return self.get_query_params().get('SetId')

	def set_SetId(self,SetId):
		self.add_query_param('SetId',SetId)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_TgtUri(self):
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self,TgtUri):
		self.add_query_param('TgtUri',TgtUri)