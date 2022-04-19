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

class ListTopicsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListTopics')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Owner(self):
		return self.get_body_params().get('Owner')

	def set_Owner(self,Owner):
		self.add_body_params('Owner', Owner)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_BeginTime(self):
		return self.get_body_params().get('BeginTime')

	def set_BeginTime(self,BeginTime):
		self.add_body_params('BeginTime', BeginTime)

	def get_TopicStatuses(self):
		return self.get_body_params().get('TopicStatuses')

	def set_TopicStatuses(self,TopicStatuses):
		self.add_body_params('TopicStatuses', TopicStatuses)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_InstanceId(self):
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_body_params('InstanceId', InstanceId)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_TopicTypes(self):
		return self.get_body_params().get('TopicTypes')

	def set_TopicTypes(self,TopicTypes):
		self.add_body_params('TopicTypes', TopicTypes)

	def get_NodeId(self):
		return self.get_body_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_body_params('NodeId', NodeId)