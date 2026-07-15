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
from aliyunsdkschedulerx2.endpoint import endpoint_data

class ManageSchedulerxJobSyncRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'schedulerx2', '2019-04-30', 'ManageSchedulerxJobSync','schedulerx2')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NamespaceSource(self): # String
		return self.get_body_params().get('NamespaceSource')

	def set_NamespaceSource(self, NamespaceSource):  # String
		self.add_body_params('NamespaceSource', NamespaceSource)
	def get_TargetNamespace(self): # String
		return self.get_body_params().get('TargetNamespace')

	def set_TargetNamespace(self, TargetNamespace):  # String
		self.add_body_params('TargetNamespace', TargetNamespace)
	def get_OriginalGroupId(self): # String
		return self.get_body_params().get('OriginalGroupId')

	def set_OriginalGroupId(self, OriginalGroupId):  # String
		self.add_body_params('OriginalGroupId', OriginalGroupId)
	def get_JobIdList(self): # String
		return self.get_body_params().get('JobIdList')

	def set_JobIdList(self, JobIdList):  # String
		self.add_body_params('JobIdList', JobIdList)
	def get_OriginalNamespace(self): # String
		return self.get_body_params().get('OriginalNamespace')

	def set_OriginalNamespace(self, OriginalNamespace):  # String
		self.add_body_params('OriginalNamespace', OriginalNamespace)
	def get_TargetGroupId(self): # String
		return self.get_body_params().get('TargetGroupId')

	def set_TargetGroupId(self, TargetGroupId):  # String
		self.add_body_params('TargetGroupId', TargetGroupId)
