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
from aliyunsdkccc.endpoint import endpoint_data

class ModifyCabInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2017-07-05', 'ModifyCabInstance')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxConcurrentConversation(self):
		return self.get_query_params().get('MaxConcurrentConversation')

	def set_MaxConcurrentConversation(self,MaxConcurrentConversation):
		self.add_query_param('MaxConcurrentConversation',MaxConcurrentConversation)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_CallCenterInstanceId(self):
		return self.get_query_params().get('CallCenterInstanceId')

	def set_CallCenterInstanceId(self,CallCenterInstanceId):
		self.add_query_param('CallCenterInstanceId',CallCenterInstanceId)

	def get_InstanceDescription(self):
		return self.get_query_params().get('InstanceDescription')

	def set_InstanceDescription(self,InstanceDescription):
		self.add_query_param('InstanceDescription',InstanceDescription)