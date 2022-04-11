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
from aliyunsdkvod.endpoint import endpoint_data

class RegisterMediaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'RegisterMedia','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_TemplateGroupId(self): # String
		return self.get_query_params().get('TemplateGroupId')

	def set_TemplateGroupId(self, TemplateGroupId):  # String
		self.add_query_param('TemplateGroupId', TemplateGroupId)
	def get_RegisterMetadatas(self): # String
		return self.get_query_params().get('RegisterMetadatas')

	def set_RegisterMetadatas(self, RegisterMetadatas):  # String
		self.add_query_param('RegisterMetadatas', RegisterMetadatas)
	def get_WorkflowId(self): # String
		return self.get_query_params().get('WorkflowId')

	def set_WorkflowId(self, WorkflowId):  # String
		self.add_query_param('WorkflowId', WorkflowId)
