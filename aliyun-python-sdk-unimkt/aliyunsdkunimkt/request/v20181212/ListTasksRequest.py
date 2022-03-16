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
from aliyunsdkunimkt.endpoint import endpoint_data

class ListTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'UniMkt', '2018-12-12', 'ListTasks')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MarketingType(self): # Integer
		return self.get_body_params().get('MarketingType')

	def set_MarketingType(self, MarketingType):  # Integer
		self.add_body_params('MarketingType', MarketingType)
	def get_TaskType(self): # String
		return self.get_body_params().get('TaskType')

	def set_TaskType(self, TaskType):  # String
		self.add_body_params('TaskType', TaskType)
	def get_PageSize(self): # Long
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_body_params('PageSize', PageSize)
	def get_TaskName(self): # String
		return self.get_body_params().get('TaskName')

	def set_TaskName(self, TaskName):  # String
		self.add_body_params('TaskName', TaskName)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_PageIndex(self): # Long
		return self.get_body_params().get('PageIndex')

	def set_PageIndex(self, PageIndex):  # Long
		self.add_body_params('PageIndex', PageIndex)
	def get_BrandUserNick(self): # String
		return self.get_body_params().get('BrandUserNick')

	def set_BrandUserNick(self, BrandUserNick):  # String
		self.add_body_params('BrandUserNick', BrandUserNick)
	def get_ProxyUserNick(self): # String
		return self.get_body_params().get('ProxyUserNick')

	def set_ProxyUserNick(self, ProxyUserNick):  # String
		self.add_body_params('ProxyUserNick', ProxyUserNick)
	def get_StartTime(self): # String
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_body_params('StartTime', StartTime)
	def get_TaskId(self): # Long
		return self.get_body_params().get('TaskId')

	def set_TaskId(self, TaskId):  # Long
		self.add_body_params('TaskId', TaskId)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
