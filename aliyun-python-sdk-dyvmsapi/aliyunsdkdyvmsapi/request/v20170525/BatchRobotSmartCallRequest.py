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
from aliyunsdkdyvmsapi.endpoint import endpoint_data

class BatchRobotSmartCallRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'BatchRobotSmartCall','dyvms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_EarlyMediaAsr(self):
		return self.get_query_params().get('EarlyMediaAsr')

	def set_EarlyMediaAsr(self,EarlyMediaAsr):
		self.add_query_param('EarlyMediaAsr',EarlyMediaAsr)

	def get_TtsParamHead(self):
		return self.get_query_params().get('TtsParamHead')

	def set_TtsParamHead(self,TtsParamHead):
		self.add_query_param('TtsParamHead',TtsParamHead)

	def get_TaskName(self):
		return self.get_query_params().get('TaskName')

	def set_TaskName(self,TaskName):
		self.add_query_param('TaskName',TaskName)

	def get_TtsParam(self):
		return self.get_query_params().get('TtsParam')

	def set_TtsParam(self,TtsParam):
		self.add_query_param('TtsParam',TtsParam)

	def get_CalledNumber(self):
		return self.get_query_params().get('CalledNumber')

	def set_CalledNumber(self,CalledNumber):
		self.add_query_param('CalledNumber',CalledNumber)

	def get_CalledShowNumber(self):
		return self.get_query_params().get('CalledShowNumber')

	def set_CalledShowNumber(self,CalledShowNumber):
		self.add_query_param('CalledShowNumber',CalledShowNumber)

	def get_IsSelfLine(self):
		return self.get_query_params().get('IsSelfLine')

	def set_IsSelfLine(self,IsSelfLine):
		self.add_query_param('IsSelfLine',IsSelfLine)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_DialogId(self):
		return self.get_query_params().get('DialogId')

	def set_DialogId(self,DialogId):
		self.add_query_param('DialogId',DialogId)

	def get_ScheduleTime(self):
		return self.get_query_params().get('ScheduleTime')

	def set_ScheduleTime(self,ScheduleTime):
		self.add_query_param('ScheduleTime',ScheduleTime)

	def get_CorpName(self):
		return self.get_query_params().get('CorpName')

	def set_CorpName(self,CorpName):
		self.add_query_param('CorpName',CorpName)

	def get_ScheduleCall(self):
		return self.get_query_params().get('ScheduleCall')

	def set_ScheduleCall(self,ScheduleCall):
		self.add_query_param('ScheduleCall',ScheduleCall)