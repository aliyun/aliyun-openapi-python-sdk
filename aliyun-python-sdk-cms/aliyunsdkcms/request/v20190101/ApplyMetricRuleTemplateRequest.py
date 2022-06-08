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

class ApplyMetricRuleTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'ApplyMetricRuleTemplate','cms')
		self.set_method('POST')

	def get_ApplyMode(self): # String
		return self.get_query_params().get('ApplyMode')

	def set_ApplyMode(self, ApplyMode):  # String
		self.add_query_param('ApplyMode', ApplyMode)
	def get_Webhook(self): # String
		return self.get_query_params().get('Webhook')

	def set_Webhook(self, Webhook):  # String
		self.add_query_param('Webhook', Webhook)
	def get_TemplateIds(self): # String
		return self.get_query_params().get('TemplateIds')

	def set_TemplateIds(self, TemplateIds):  # String
		self.add_query_param('TemplateIds', TemplateIds)
	def get_EnableEndTime(self): # Long
		return self.get_query_params().get('EnableEndTime')

	def set_EnableEndTime(self, EnableEndTime):  # Long
		self.add_query_param('EnableEndTime', EnableEndTime)
	def get_GroupId(self): # Long
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # Long
		self.add_query_param('GroupId', GroupId)
	def get_NotifyLevel(self): # Long
		return self.get_query_params().get('NotifyLevel')

	def set_NotifyLevel(self, NotifyLevel):  # Long
		self.add_query_param('NotifyLevel', NotifyLevel)
	def get_EnableStartTime(self): # Long
		return self.get_query_params().get('EnableStartTime')

	def set_EnableStartTime(self, EnableStartTime):  # Long
		self.add_query_param('EnableStartTime', EnableStartTime)
	def get_SilenceTime(self): # Long
		return self.get_query_params().get('SilenceTime')

	def set_SilenceTime(self, SilenceTime):  # Long
		self.add_query_param('SilenceTime', SilenceTime)
