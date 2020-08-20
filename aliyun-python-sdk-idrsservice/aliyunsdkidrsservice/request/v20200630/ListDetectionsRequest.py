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

class ListDetectionsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'idrsservice', '2020-06-30', 'ListDetections','idrsservice')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CreateDateTo(self):
		return self.get_query_params().get('CreateDateTo')

	def set_CreateDateTo(self,CreateDateTo):
		self.add_query_param('CreateDateTo',CreateDateTo)

	def get_DepartmentId(self):
		return self.get_query_params().get('DepartmentId')

	def set_DepartmentId(self,DepartmentId):
		self.add_query_param('DepartmentId',DepartmentId)

	def get_RecordingType(self):
		return self.get_query_params().get('RecordingType')

	def set_RecordingType(self,RecordingType):
		self.add_query_param('RecordingType',RecordingType)

	def get_CreateDateFrom(self):
		return self.get_query_params().get('CreateDateFrom')

	def set_CreateDateFrom(self,CreateDateFrom):
		self.add_query_param('CreateDateFrom',CreateDateFrom)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_PageIndex(self):
		return self.get_query_params().get('PageIndex')

	def set_PageIndex(self,PageIndex):
		self.add_query_param('PageIndex',PageIndex)

	def get_RuleId(self):
		return self.get_query_params().get('RuleId')

	def set_RuleId(self,RuleId):
		self.add_query_param('RuleId',RuleId)