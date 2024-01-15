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
from aliyunsdkiot.endpoint import endpoint_data

class UpdateOTAJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'UpdateOTAJob','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UpgradeType(self):
		return self.get_query_params().get('UpgradeType')

	def set_UpgradeType(self,UpgradeType):
		self.add_query_param('UpgradeType',UpgradeType)

	def get_TimeoutInMinutes(self):
		return self.get_query_params().get('TimeoutInMinutes')

	def set_TimeoutInMinutes(self,TimeoutInMinutes):
		self.add_query_param('TimeoutInMinutes',TimeoutInMinutes)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_SrcVersionLists(self):
		return self.get_query_params().get('SrcVersionList')

	def set_SrcVersionLists(self, SrcVersionLists):
		for depth1 in range(len(SrcVersionLists)):
			if SrcVersionLists[depth1] is not None:
				self.add_query_param('SrcVersionList.' + str(depth1 + 1) , SrcVersionLists[depth1])

	def get_TargetSelection(self):
		return self.get_query_params().get('TargetSelection')

	def set_TargetSelection(self,TargetSelection):
		self.add_query_param('TargetSelection',TargetSelection)

	def get_Tagss(self):
		return self.get_query_params().get('Tags')

	def set_Tagss(self, Tagss):
		for depth1 in range(len(Tagss)):
			if Tagss[depth1].get('Value') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Value', Tagss[depth1].get('Value'))
			if Tagss[depth1].get('Key') is not None:
				self.add_query_param('Tags.' + str(depth1 + 1) + '.Key', Tagss[depth1].get('Key'))

	def get_MaximumPerMinute(self):
		return self.get_query_params().get('MaximumPerMinute')

	def set_MaximumPerMinute(self,MaximumPerMinute):
		self.add_query_param('MaximumPerMinute',MaximumPerMinute)