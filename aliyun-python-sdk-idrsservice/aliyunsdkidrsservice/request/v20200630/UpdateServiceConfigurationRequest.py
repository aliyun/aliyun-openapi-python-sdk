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
from aliyunsdkidrsservice.endpoint import endpoint_data

class UpdateServiceConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'UpdateServiceConfiguration','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TaskItemQueueSize(self):
		return self.get_query_params().get('TaskItemQueueSize')

	def set_TaskItemQueueSize(self,TaskItemQueueSize):
		self.add_query_param('TaskItemQueueSize',TaskItemQueueSize)

	def get_LiveRecordLayout(self):
		return self.get_query_params().get('LiveRecordLayout')

	def set_LiveRecordLayout(self,LiveRecordLayout):
		self.add_query_param('LiveRecordLayout',LiveRecordLayout)

	def get_ClientQueueSize(self):
		return self.get_query_params().get('ClientQueueSize')

	def set_ClientQueueSize(self,ClientQueueSize):
		self.add_query_param('ClientQueueSize',ClientQueueSize)

	def get_LiveRecordTaskProfile(self):
		return self.get_query_params().get('LiveRecordTaskProfile')

	def set_LiveRecordTaskProfile(self,LiveRecordTaskProfile):
		self.add_query_param('LiveRecordTaskProfile',LiveRecordTaskProfile)

	def get_LiveRecordAll(self):
		return self.get_query_params().get('LiveRecordAll')

	def set_LiveRecordAll(self,LiveRecordAll):
		self.add_query_param('LiveRecordAll',LiveRecordAll)

	def get_LiveRecordEveryOne(self):
		return self.get_query_params().get('LiveRecordEveryOne')

	def set_LiveRecordEveryOne(self,LiveRecordEveryOne):
		self.add_query_param('LiveRecordEveryOne',LiveRecordEveryOne)