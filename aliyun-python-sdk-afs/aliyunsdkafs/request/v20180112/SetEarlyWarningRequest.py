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
class SetEarlyWarningRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'afs', '2018-01-12', 'SetEarlyWarning')

	def get_TimeEnd(self):
		return self.get_query_params().get('TimeEnd')

	def set_TimeEnd(self,TimeEnd):
		self.add_query_param('TimeEnd',TimeEnd)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_WarnOpen(self):
		return self.get_query_params().get('WarnOpen')

	def set_WarnOpen(self,WarnOpen):
		self.add_query_param('WarnOpen',WarnOpen)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_Title(self):
		return self.get_query_params().get('Title')

	def set_Title(self,Title):
		self.add_query_param('Title',Title)

	def get_TimeOpen(self):
		return self.get_query_params().get('TimeOpen')

	def set_TimeOpen(self,TimeOpen):
		self.add_query_param('TimeOpen',TimeOpen)

	def get_TimeBegin(self):
		return self.get_query_params().get('TimeBegin')

	def set_TimeBegin(self,TimeBegin):
		self.add_query_param('TimeBegin',TimeBegin)

	def get_Frequency(self):
		return self.get_query_params().get('Frequency')

	def set_Frequency(self,Frequency):
		self.add_query_param('Frequency',Frequency)