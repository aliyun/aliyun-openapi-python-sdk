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
from aliyunsdktdsr.endpoint import endpoint_data

class CreateProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'tdsr', '2020-01-01', 'CreateProject')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BusinessUserIdList(self):
		return self.get_query_params().get('BusinessUserIdList')

	def set_BusinessUserIdList(self,BusinessUserIdList):
		self.add_query_param('BusinessUserIdList',BusinessUserIdList)

	def get_BuilderUserIdList(self):
		return self.get_query_params().get('BuilderUserIdList')

	def set_BuilderUserIdList(self,BuilderUserIdList):
		self.add_query_param('BuilderUserIdList',BuilderUserIdList)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_BusinessId(self):
		return self.get_query_params().get('BusinessId')

	def set_BusinessId(self,BusinessId):
		self.add_query_param('BusinessId',BusinessId)

	def get_GatherUserIdList(self):
		return self.get_query_params().get('GatherUserIdList')

	def set_GatherUserIdList(self,GatherUserIdList):
		self.add_query_param('GatherUserIdList',GatherUserIdList)