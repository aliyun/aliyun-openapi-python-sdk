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
from aliyunsdkcdn.endpoint import endpoint_data

class AddFCTriggerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'AddFCTrigger')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Notes(self):
		return self.get_body_params().get('Notes')

	def set_Notes(self,Notes):
		self.add_body_params('Notes', Notes)

	def get_EventMetaVersion(self):
		return self.get_body_params().get('EventMetaVersion')

	def set_EventMetaVersion(self,EventMetaVersion):
		self.add_body_params('EventMetaVersion', EventMetaVersion)

	def get_TriggerARN(self):
		return self.get_query_params().get('TriggerARN')

	def set_TriggerARN(self,TriggerARN):
		self.add_query_param('TriggerARN',TriggerARN)

	def get_SourceARN(self):
		return self.get_body_params().get('SourceARN')

	def set_SourceARN(self,SourceARN):
		self.add_body_params('SourceARN', SourceARN)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_RoleARN(self):
		return self.get_body_params().get('RoleARN')

	def set_RoleARN(self,RoleARN):
		self.add_body_params('RoleARN', RoleARN)

	def get_EventMetaName(self):
		return self.get_body_params().get('EventMetaName')

	def set_EventMetaName(self,EventMetaName):
		self.add_body_params('EventMetaName', EventMetaName)

	def get_FunctionARN(self):
		return self.get_body_params().get('FunctionARN')

	def set_FunctionARN(self,FunctionARN):
		self.add_body_params('FunctionARN', FunctionARN)