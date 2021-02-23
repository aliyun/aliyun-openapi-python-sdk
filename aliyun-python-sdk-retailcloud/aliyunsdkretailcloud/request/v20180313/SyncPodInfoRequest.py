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
from aliyunsdkretailcloud.endpoint import endpoint_data

class SyncPodInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'retailcloud', '2018-03-13', 'SyncPodInfo')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Reason(self):
		return self.get_query_params().get('Reason')

	def set_Reason(self,Reason):
		self.add_query_param('Reason',Reason)

	def get_RequestId(self):
		return self.get_query_params().get('RequestId')

	def set_RequestId(self,RequestId):
		self.add_query_param('RequestId',RequestId)

	def get_PodName(self):
		return self.get_query_params().get('PodName')

	def set_PodName(self,PodName):
		self.add_query_param('PodName',PodName)

	def get_SideCarType(self):
		return self.get_query_params().get('SideCarType')

	def set_SideCarType(self,SideCarType):
		self.add_query_param('SideCarType',SideCarType)

	def get_TaskId(self):
		return self.get_query_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_query_param('TaskId',TaskId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)