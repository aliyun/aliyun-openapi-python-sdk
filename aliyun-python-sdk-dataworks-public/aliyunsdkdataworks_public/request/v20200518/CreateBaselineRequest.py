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

class CreateBaselineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateBaseline')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Owner(self): # String
		return self.get_body_params().get('Owner')

	def set_Owner(self, Owner):  # String
		self.add_body_params('Owner', Owner)
	def get_AlertMarginThreshold(self): # Integer
		return self.get_body_params().get('AlertMarginThreshold')

	def set_AlertMarginThreshold(self, AlertMarginThreshold):  # Integer
		self.add_body_params('AlertMarginThreshold', AlertMarginThreshold)
	def get_OvertimeSettingss(self): # RepeatList
		return self.get_body_params().get('OvertimeSettings')

	def set_OvertimeSettingss(self, OvertimeSettings):  # RepeatList
		for depth1 in range(len(OvertimeSettings)):
			if OvertimeSettings[depth1].get('Time') is not None:
				self.add_body_params('OvertimeSettings.' + str(depth1 + 1) + '.Time', OvertimeSettings[depth1].get('Time'))
			if OvertimeSettings[depth1].get('Cycle') is not None:
				self.add_body_params('OvertimeSettings.' + str(depth1 + 1) + '.Cycle', OvertimeSettings[depth1].get('Cycle'))
	def get_Priority(self): # Integer
		return self.get_body_params().get('Priority')

	def set_Priority(self, Priority):  # Integer
		self.add_body_params('Priority', Priority)
	def get_BaselineType(self): # String
		return self.get_body_params().get('BaselineType')

	def set_BaselineType(self, BaselineType):  # String
		self.add_body_params('BaselineType', BaselineType)
	def get_BaselineName(self): # String
		return self.get_body_params().get('BaselineName')

	def set_BaselineName(self, BaselineName):  # String
		self.add_body_params('BaselineName', BaselineName)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
	def get_NodeIds(self): # String
		return self.get_body_params().get('NodeIds')

	def set_NodeIds(self, NodeIds):  # String
		self.add_body_params('NodeIds', NodeIds)
