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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class ListAlertMessagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListAlertMessages')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AlertUser(self): # String
		return self.get_body_params().get('AlertUser')

	def set_AlertUser(self, AlertUser):  # String
		self.add_body_params('AlertUser', AlertUser)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_BeginTime(self): # String
		return self.get_body_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # String
		self.add_body_params('BeginTime', BeginTime)
	def get_AlertMethods(self): # String
		return self.get_body_params().get('AlertMethods')

	def set_AlertMethods(self, AlertMethods):  # String
		self.add_body_params('AlertMethods', AlertMethods)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_BaselineId(self): # Long
		return self.get_body_params().get('BaselineId')

	def set_BaselineId(self, BaselineId):  # Long
		self.add_body_params('BaselineId', BaselineId)
	def get_RemindId(self): # Long
		return self.get_body_params().get('RemindId')

	def set_RemindId(self, RemindId):  # Long
		self.add_body_params('RemindId', RemindId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_AlertRuleTypes(self): # String
		return self.get_body_params().get('AlertRuleTypes')

	def set_AlertRuleTypes(self, AlertRuleTypes):  # String
		self.add_body_params('AlertRuleTypes', AlertRuleTypes)
