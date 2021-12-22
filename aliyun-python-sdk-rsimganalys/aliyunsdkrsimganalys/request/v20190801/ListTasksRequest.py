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
from aliyunsdkrsimganalys.endpoint import endpoint_data

class ListTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rsimganalys', '2019-08-01', 'ListTasks','rsimganalys')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SubmitTime(self):
		return self.get_query_params().get('SubmitTime')

	def set_SubmitTime(self,SubmitTime):
		self.add_query_param('SubmitTime',SubmitTime)

	def get_RunStatus(self):
		return self.get_query_params().get('RunStatus')

	def set_RunStatus(self,RunStatus):
		self.add_query_param('RunStatus',RunStatus)

	def get_ProductType(self):
		return self.get_query_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_query_param('ProductType',ProductType)

	def get_PageNo(self):
		return self.get_query_params().get('PageNo')

	def set_PageNo(self,PageNo):
		self.add_query_param('PageNo',PageNo)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Appkey(self):
		return self.get_query_params().get('Appkey')

	def set_Appkey(self,Appkey):
		self.add_query_param('Appkey',Appkey)

	def get_JobName(self):
		return self.get_query_params().get('JobName')

	def set_JobName(self,JobName):
		self.add_query_param('JobName',JobName)